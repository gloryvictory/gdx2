import logging
import pymongo
from urllib.parse import quote_plus
import pandas as pd
import smbclient
import shutil
import os
from datetime import date, timedelta
import datetime
import time
from sw_inventory_dm_config import csv_config
from sw_inventory_dm_config import smb_config
from sw_inventory_dm_config import mng_config
from sw_inventory_dm_config import db_config
from airflow import DAG
import pendulum
from airflow.operators.python import PythonOperator
from airflow.models.baseoperator import chain

log = logging.getLogger(__name__)

with DAG(
        dag_id='load_swstats_2mng',
        schedule_interval='1 0/12 * * *',
        start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
        catchup=False,
        tags=['zsniigg', 'sw_stats'],
) as dag:
    def PGWrite(SQLQuery):
        from airflow.hooks.postgres_hook import PostgresHook
        import psycopg2
        log.info('using connection '+db_config['dbcon'])
        isspghook = PostgresHook(postgres_conn_id=db_config['dbcon'])
        dbcon = isspghook.get_conn()
        dbcursor = dbcon.cursor()
        print(SQLQuery)
        dbcursor.execute(SQLQuery)
        dbcon.commit()
        dbcursor.close()
        dbcon.close()

    def copyfromsmbtolocal(**kwargs):
        if not os.path.isdir(kwargs['localfolder']):
            os.makedirs(kwargs['localfolder'])
        for smbfile in kwargs['smbfiles']:
            remotefile = kwargs['remotepath']+'\\'+smbfile
            localfile = (kwargs['localfolder'] + "//" + smbfile)
            with smbclient.open_file(remotefile, "rb") as remote_fh:
                with open(localfile, "wb") as local_fh:
                    shutil.copyfileobj(remote_fh, local_fh)
                    log.info('copying file '+smbfile)
            smbclient.remove(kwargs['remotepath']+ '//'+ smbfile)
            log.info('remove file from smb '+smbfile)

    def load_df_mongo(dataframe, mng_collection):
        import json
        dateformattopg = '%d.%m.%Y %H:%M:%S'
        mnguri = "mongodb://" + quote_plus(mng_config['mnguser']) + ":" + quote_plus(mng_config['mngpswd']) + "@" + \
                mng_config['mngsrvhost'] + ":" + mng_config['mngsrvport'] + "/?authSource=" + \
                mng_config['mngdbname'] + "&authMechanism=SCRAM-SHA-256"
        mngclient = pymongo.MongoClient(mnguri)
        mngdb = mngclient[mng_config['mngdbname']]
        mngcollection = mngdb[mng_collection]
        dataframe.insert(1, "LoadTS", str(datetime.datetime.now().strftime(dateformattopg)), True)
        dataframe.insert(2, "Source", 'Index script', True)
        jsondata = json.loads(dataframe.to_json(orient="records"))
        return mngcollection.insert_many(jsondata)

    def clear_df_data(dataframe):
        dataframe['TimeStamp'] = pd.to_datetime(dataframe['TimeStamp'])
        return dataframe

    def select_mongo_df(**kwargs):
        import json
        paramdistinct = kwargs['paramdistinct']
        paramquery = kwargs['paramquery']
        print(paramquery)
        mnguri = "mongodb://" + quote_plus(mng_config['mnguser']) + ":" + quote_plus(mng_config['mngpswd']) + "@" + \
                 mng_config['mngsrvhost'] + ":" + mng_config['mngsrvport'] + "/?authSource=" + \
                 mng_config['mngdbname'] + "&authMechanism=SCRAM-SHA-256"
        mngclient = pymongo.MongoClient(mnguri)
        mngdb = mngclient[mng_config['mngdbname']]
        if len(paramdistinct) < 1:
            mngcollection = mngdb[mng_config['mngcol']].find(paramquery)
        else:
            mngcollection = mngdb[mng_config['mngcol']].find(paramquery).distinct(paramdistinct)
        return mngcollection

    def getmsecsfromdate(**kwargs):
        import datetime
        import time
        datestring = kwargs['datestring']
        return round(time.mktime(datetime.datetime.strptime(datestring, "%Y/%m/%d").timetuple()) * 1000)

    def PGRead(SQLQuery):
        from airflow.hooks.postgres_hook import PostgresHook
        import psycopg2
        log.info('using connection '+db_config['dbcon'])
        isspghook = PostgresHook(postgres_conn_id=db_config['dbcon'])
        dbcon = isspghook.get_conn()

        dbcursor = dbcon.cursor()
        dbcursor.execute(SQLQuery)
        dbresult = dbcursor.fetchall()
        dbcon.commit()
        dbcursor.close()
        dbcon.close()
        return dbresult

    def getyesterday(**kwargs):
        from datetime import date, timedelta
        datequery = 'SELECT max("date") FROM "sw_inventory_dm"."dm"'
        maxdate = PGRead(datequery)
        yesterday = maxdate[0][0]
        if yesterday == None:
            log.info('No records in PG database')
            yesterday = date.today() - timedelta(days=16500)
        else:
            yesterday = maxdate[0][0] + timedelta(hours=24)
        return getmsecsfromdate(datestring=yesterday.strftime("%Y/%m/%d")) - 7200000

    def gettoday(**kwargs):
        return getmsecsfromdate(datestring=datetime.datetime.now().strftime("%Y/%m/%d")) - 7200000

    def getusersfrommng(**kwargs):
        from operator import is_not
        from functools import partial

        #            fromdict = {"$gt": kwargs['yesterday']}
        #            todict = {"$lte": kwargs['today']}
        timedict = {"$gt": kwargs['yesterday'], "$lte": kwargs['today']}

        paramquery = {"TimeStamp": timedict}
        mngcollection = select_mongo_df(paramquery=paramquery, paramdistinct="UserSAM")
        mngcollection = list(filter(partial(is_not, None), mngcollection))
        return mngcollection

    def getdatafromdf(**kwargs):
        collection = []
        mngdf = kwargs['datdaframe']
        mngdf['TimeStamp'] = pd.to_datetime(mngdf['TimeStamp'], unit = 'ms')
        mngdf['TimeStamp'] = mngdf['TimeStamp'] + pd.Timedelta(hours = 5) #utz to local time
        username = mngdf.loc[0]['UserSAM'] # username - UserSAM, wich ownes loaded image
        computername = mngdf.loc[0]['Computer'] # username - UserSAM, wich ownes loaded image
        execs = mngdf["ExecName"].drop_duplicates()
        mngdf["Date"] = mngdf["TimeStamp"].dt.date
        workingdates = mngdf["Date"].drop_duplicates()
        for workingdate in workingdates:
            date_mngdf = mngdf.loc[mngdf["Date"] == workingdate]
            execs = date_mngdf["ExecName"].drop_duplicates()
            for execn in execs: #execn - name of executed image
                execimagesitems = date_mngdf.loc[date_mngdf['ExecName'] == execn]
                pidcount = date_mngdf.groupby(['TimeStamp','ExecName']).size().max() # pidcount count of simulationasly loaded images
                execminutes = execimagesitems.count().TimeStamp*5 #execminutes - minutes at day
                log.info("On computer " + computername + " for image " + execn + " owned by user " + username + " with simulateneously PID count " + str(pidcount) + " taken " + str(execminutes) + " minutes at " +  str(workingdate))
                collection.append({"User": username, "Image": execn, "Time": execminutes, "Date": workingdate, "ImCount": pidcount, "Computer": computername})
        return collection

    def makeinsertquery(**kwargs):
        item = kwargs['item']
        return 'INSERT INTO "sw_inventory_dm"."dm" VALUES ('+"'" + item['Date'].strftime("%Y-%m-%d") + "','" + item['Computer'] + "','" + item['User'] + "'," + str(item['ImCount']) + ",'"  + item['Image'] + "'," + str(item['Time']) + ");"


    def extract_data(**kwargs):
        smbclient.ClientConfig(username=smb_config['smbuser'], password=smb_config['smbpwd'])
        smbclient.register_session(smb_config['smbsrv'], username=smb_config['smbuser'], password=smb_config['smbpwd'])
        remotepath = r'\\'+smb_config['smbsrv']+'\\' + smb_config['smbshare']+'\\' + smb_config['smbfldr']
        smbfiles = smbclient.listdir(remotepath)
#        log.info('copying files '+smbfiles)
        copyfromsmbtolocal(localfolder = csv_config['localfolder'],smbfiles = smbfiles, remotepath = remotepath)
        localfiles = os.listdir(csv_config['localfolder'])
#        print(csv_config['localfolder'])
#        print(localfiles)

        for localfile in localfiles:
            log.info('prcessing local file '+localfile)
            xldoc = csv_config['localfolder']+'//'+localfile
            print(xldoc)
            loadedxl = pd.read_csv(xldoc, encoding='utf-16', delimiter=';')
            loadedxl = clear_df_data(loadedxl)
            load_df_mongo(loadedxl, mng_config['mngcol'])
            os.remove(xldoc)

    def makedatamart(**kwargs):
        ti = kwargs['ti']
        datequery = 'SELECT max("date") FROM "sw_inventory_dm"."dm"'
        maxdate = PGRead(datequery)
        yesterday = maxdate[0][0]
        print(maxdate[0][0])
        if yesterday == None:
            print('No records')
            yesterday = date.today() - timedelta(days=16500)
        getmsecsfromdate(datestring = yesterday.strftime("%Y/%m/%d"))-7200000

        today = gettoday()
        yesterday = getyesterday()
        print(yesterday)
        #print(maxdate)
        timedict = {"$gt": yesterday,"$lte": today}
        paramquery = {"TimeStamp":timedict}
        distusers = getusersfrommng(today = today, yesterday = yesterday)
        len(distusers)
        distusers

        data2load = []
        for distuser in distusers:
            userdict = { "UserSAM" : distuser }
            paramquery = { "UserSAM" : distuser ,"TimeStamp":timedict}
            paramquery
            mngcollection = select_mongo_df(paramquery = paramquery, paramdistinct = "")
            mngdf =  pd.DataFrame(list(mngcollection))
            mngdf.drop('_id', axis=1, inplace=True)
            data2load.append(getdatafromdf(datdaframe = mngdf))
        print(data2load)
        sqlinsertquery = ''
        for items2load in data2load:
            for item2load in items2load:
                sqlinsertquery = sqlinsertquery + makeinsertquery(item = item2load)
                log.info(makeinsertquery(item = item2load))
        ti.xcom_push('data2load', sqlinsertquery)

    def loaddatamart(**kwargs):
        ti = kwargs['ti']
        sqlinsertquery = ti.xcom_pull(key='data2load')
        print(sqlinsertquery)
        PGWrite(sqlinsertquery)

    extract_data = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )
    makedatamart = PythonOperator(
        task_id='makedatamart',
        python_callable=makedatamart,
    )
    loaddatamart = PythonOperator(
        task_id='loaddatamart',
        python_callable=loaddatamart,
    )


    chain(extract_data,makedatamart,loaddatamart)
