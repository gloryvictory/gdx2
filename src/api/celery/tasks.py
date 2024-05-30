import json
import re
import time
from datetime import datetime
import sqlalchemy
from sqlalchemy.orm import Session

from celery import Celery
from sqlalchemy import update, text, insert, select, func
from starlette.requests import Request

from src import cfg
from src.api.report.utils import str_clean, list_str_clean
from src.models import M_FILE, M_HISTORY_TASK, M_R_AUTHOR, M_REPORT_TGF, M_R_SUBRF, M_R_ORG, M_R_AREA, M_R_LIST, \
    M_R_FIELD, M_R_LU, M_R_PI, M_R_VID_RAB, M_HISTORY

# import asyncio
# from src.db.db import async_session_maker
# from src.log import set_logger
# from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


# celery = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')
celery = Celery('tasks', backend=cfg.REDIS_BACKEND, broker=cfg.REDIS_BROKER)

# celery = Celery('tasks', broker=cfg.REDIS_URL)
# волго-уральская	6
# западно-сибирская	49483
# лено-вилюйская	4
# лено-тунгусская	9
# мезенская	28788
# охотская	6
# прикаспийская	14
# притихоокеанская	8
# тимано-печорская	1136

# запуск celery
# celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo
# celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo --autoscale=10,3 --concurrency=10 -n worker1@%h
# запуск flower
# celery -A src.api.celery.tasks:celery flower
# Удалить все задачи
#  celery -A src.api.celery.tasks:celery  purge

# @celery.task(serializer='pickle')
# async def update_file_by_ngp_str(ngp_str: str, lat: float, lon: float, f_path_md5: str):
#     try:
#         async with async_session_maker() as session:
#             time1 = datetime.now()
#             log = set_logger(cfg.NGP_FILE_LOG)
#             log.INFO(f"Обработка: {ngp_str}")
#
#             # print(file.f_path)
#             # f_path_md5 = f_path_md5
#             stmt = (
#                 update(M_FILE)
#                 .where(M_FILE.f_path_md5 == f_path_md5)
#                 .values(ngp=ngp_str, lat=lat, lon=lon)
#             )
#             await session.execute(stmt)
#             await session.commit()
#
#             content = {"msg": "Success"}
#             time2 = datetime.now()
#             log.INFO(f"Обработано: {ngp_str}. Total time:  + {str(time2 - time1)}")
#             return content
#     except Exception as e:
#         cont_err = f"fail. can't read or update data from table ({M_FILE.__tablename__})"
#         content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
#         print(content)
#     finally:
#         if session is not None:
#             await session.close()
#     return content


#
# Рабочий вариант без Celery!!!
# async def update_file_by_ngp_str2(ngp_str: str, lat: float, lon: float, *args, **kwargs):
#     try:
#         print(f"Обработано: {ngp_str}.!!!!!!")
#         async with async_session_maker() as session:
#             time1 = datetime.now()
#             ngp_str_new = f"%{ngp_str}%"
#             stmt = (
#                 update(M_FILE)
#                 .where(M_FILE.f_path.ilike(ngp_str_new))
#                 .values(ngp=ngp_str, lat=lat, lon=lon)
#             )
#             await session.execute(stmt)
#             await session.commit()
#             time2 = datetime.now()
#             print(f"Обработано: {ngp_str}. Total time:  + {str(time2 - time1)}")
#     except Exception as e:
#         cont_err = f"fail. can't read or update data from table ({M_FILE.__tablename__})"
#         content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
#         print(content)
#     finally:
#         if session is not None:
#             await session.close()


# from src.cfg import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER, DB_SCHEMA, CONVENTION
# DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# print(DATABASE_URL)
# metadata = MetaData(schema=DB_SCHEMA, naming_convention=CONVENTION)
# engine = create_async_engine(DATABASE_URL, poolclass=NullPool, echo=True)
# async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# database = Database()
# engine = database.get_db_connection()
# session = database.get_db_session()

# celery_log = get_task_logger(__name__)

celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"]
)


# НГ провинции
# , lat: float, lon: float, *args, **kwargs
@celery.task(name="update_file_by_ngp")
def update_file_by_ngp_str2(uuid_session:str, ngp_str: str, lat: float, lon: float):
    # ngp_str: str = "qweqweqweqwe"
    # print(f"Обработано: {ngp_str} {lat} {lon}.!!!!!!")
    try:
        # print(f"Обработано: {ngp_str}.!!!!!!")
        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        # create session and add objects
        with Session(engine) as session:
            time1 = datetime.now()
            ngp_str_new = f"%{ngp_str}%"
            stmt = (
                update(M_FILE)
                .where(M_FILE.f_path.ilike(ngp_str_new))
                .values(ngp=ngp_str, lat=lat, lon=lon)
            )
            session.execute(stmt)
            session.commit()
            time2 = datetime.now()

            time_diff = time2 - time1
            time_obj = time.gmtime(time_diff.total_seconds())
            dt = time.strftime('%Y-%m-%d %H:%M:%S', time_obj)
            stmt = insert(M_HISTORY_TASK).values(task_id=uuid_session, task_type="update_file_by_ngp", task_name=ngp_str,time_start=time1, time_end=time2, time_duration=dt)
            session.execute(stmt)
            session.commit()

            print(f"Обработано: {ngp_str}  {lat} {lon}. Total time:  + {str(time2 - time1)}")
    except Exception as e:
        cont_err = f"fail. can't read or update data from table ({M_FILE.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            session.close()


# НГ Области
@celery.task(name="update_file_by_ngo")
def update_file_by_ngo_str2(uuid_session:str, ngo_str: str, lat: float, lon: float):
    # ngp_str: str = "qweqweqweqwe"
    # print(f"Обработано: {ngp_str} {lat} {lon}.!!!!!!")
    try:
        # print(f"Обработано: {ngp_str}.!!!!!!")
        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        # create session and add objects
        with Session(engine) as session:
            time1 = datetime.now()
            ngo_str_new = f"%{ngo_str}%"
            stmt = (
                update(M_FILE)
                .where(M_FILE.f_path.ilike(ngo_str_new))
                .values(ngo=ngo_str, lat=lat, lon=lon)
            )
            session.execute(stmt)
            session.commit()
            time2 = datetime.now()

            time_diff = time2 - time1
            time_obj = time.gmtime(time_diff.total_seconds())
            dt = time.strftime('%Y-%m-%d %H:%M:%S', time_obj)
            stmt = insert(M_HISTORY_TASK).values(task_id=uuid_session, task_type="update_file_by_ngo", task_name=ngo_str,time_start=time1, time_end=time2, time_duration=dt)
            session.execute(stmt)
            session.commit()

            print(f"Обработано: {ngo_str}  {lat} {lon}. Total time:  + {str(time2 - time1)}")
    except Exception as e:
        cont_err = f"fail. can't read or update data from table ({M_FILE.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            session.close()


# НГ Районы
@celery.task(name="update_file_by_ngr")
def update_file_by_ngr_str2(uuid_session:str, ngr_str: str, lat: float, lon: float):
    try:
        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        # create session and add objects
        with Session(engine) as session:
            time1 = datetime.now()
            ngr_str_new = f"%{ngr_str}%"
            stmt = (
                update(M_FILE)
                .where(M_FILE.f_path.ilike(ngr_str_new))
                .values(ngr=ngr_str, lat=lat, lon=lon)
            )
            session.execute(stmt)
            session.commit()
            time2 = datetime.now()
            time_diff = time2 - time1
            time_obj = time.gmtime(time_diff.total_seconds())
            dt = time.strftime('%Y-%m-%d %H:%M:%S', time_obj)
            stmt = insert(M_HISTORY_TASK).values(task_id=uuid_session, task_type="update_file_by_ngr", task_name=ngr_str,time_start=time1, time_end=time2, time_duration=dt)
            session.execute(stmt)
            session.commit()

            print(f"Обработано: {ngr_str}  {lat} {lon}. Total time:  + {str(time2 - time1)}")
    except Exception as e:
        cont_err = f"fail. can't read or update data from table ({M_FILE.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            session.close()

# Площади
@celery.task(name="update_file_by_area")
def update_file_by_area_str2(uuid_session:str, area: str, lat: float, lon: float):
    try:
        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        # create session and add objects
        with Session(engine) as session:
            time1 = datetime.now()
            area_str_new = f"%{area}%"
            stmt = (
                update(M_FILE)
                .where(M_FILE.f_path.ilike(area_str_new))
                .values(areaoil=area, lat=lat, lon=lon)
            )
            # print(stmt)
            session.execute(stmt)
            session.commit()
            time2 = datetime.now()
            time_diff = time2 - time1
            time_obj = time.gmtime(time_diff.total_seconds())
            dt = time.strftime('%Y-%m-%d %H:%M:%S', time_obj)
            stmt = insert(M_HISTORY_TASK).values(task_id=uuid_session, task_type="update_file_by_area",
                                                 task_name=area, time_start=time1, time_end=time2, time_duration=dt)
            session.execute(stmt)
            session.commit()
            print(f"Обработано: {area}  {lat} {lon}. Total time:  + {str(time2 - time1)}")
    except Exception as e:
        cont_err = f"fail. can't read or update data from table ({M_FILE.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            session.close()

# Месторождения
@celery.task(name="update_file_by_field")
def update_file_by_field_str2(uuid_session:str, field: str, lat: float, lon: float):
    try:
        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        # create session and add objects
        with Session(engine) as session:
            time1 = datetime.now()
            field_str_new = f"%{field}%"
            stmt = (
                update(M_FILE)
                .where(M_FILE.f_path.ilike(field_str_new))
                .values(field=field, lat=lat, lon=lon)
            )
            # print(stmt)
            session.execute(stmt)
            session.commit()
            time2 = datetime.now()
            time_diff = time2 - time1
            time_obj = time.gmtime(time_diff.total_seconds())
            dt = time.strftime('%Y-%m-%d %H:%M:%S', time_obj)
            stmt = insert(M_HISTORY_TASK).values(task_id=uuid_session, task_type="update_file_by_field",
                                                 task_name=field, time_start=time1, time_end=time2, time_duration=dt)
            session.execute(stmt)
            session.commit()
            print(f"Обработано: {field}  {lat} {lon}. Total time:  + {str(time2 - time1)}")
    except Exception as e:
        cont_err = f"fail. can't read or update data from table ({M_FILE.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            session.close()

# Скважины
@celery.task(name="update_file_by_well")
def update_file_by_well_str2(uuid_session:str, area: str, well: str, lat: float, lon: float):
    try:
        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        # create session and add objects
        with Session(engine) as session:
            time1 = datetime.now()
            field_str_new = f"%{area} {well}%"
            stmt = (
                update(M_FILE)
                .where(M_FILE.f_path.ilike(field_str_new))
                .values(areaoil=area, well=well, lat=lat, lon=lon)
            )
            # print(stmt)
            session.execute(stmt)
            session.commit()
            time2 = datetime.now()
            time_diff = time2 - time1
            time_obj = time.gmtime(time_diff.total_seconds())
            dt = time.strftime('%Y-%m-%d %H:%M:%S', time_obj)
            stmt = insert(M_HISTORY_TASK).values(task_id=uuid_session, task_type="update_file_by_well",
                                                 task_name=field_str_new, time_start=time1, time_end=time2, time_duration=dt)
            session.execute(stmt)
            session.commit()
            print(f"Обработано: {area} {well} {lat} {lon}. Total time:  + {str(time2 - time1)}")
    except Exception as e:
        cont_err = f"fail. can't read or update data from table ({M_FILE.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            session.close()


#
@celery.task(name="report_update_author")
def report_update_author():
    content = {"msg": "Fail"}
    try:
        authors = []
        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        with Session(engine) as session:
        # async with async_session_maker() as session:
            # truncate table
            stmt = text(f"TRUNCATE {M_R_AUTHOR.__tablename__} RESTART IDENTITY;")
            session.execute(stmt)
            session.commit()
            #
            res = session.scalars(
                select(M_REPORT_TGF.author_name)
                .where(M_REPORT_TGF.author_name != '')
                .order_by(M_REPORT_TGF.author_name)
            )
            _all = res.all()
            for author_name in _all:
                author_tmp = str_clean(author_name).lstrip()
                # print(author_tmp)
                if len(author_tmp) > 2:
                    result = re.match(r'^0-9', author_tmp)
                    result2 = re.match(r'[^\D]', author_tmp)
                    if not result or not result2:
                        authors.append(author_tmp)
            authors_str = ",".join(authors)
            authors2 = authors_str.split(",")
            authors3 = []
            # Обрабатываем список авторов и добавляем . если ее нет
            for author in authors2:
                if not author.startswith("<openpyxl"):
                    author_tmp1 = author.strip()
                    if len(author_tmp1) > 3 and (not author_tmp1.endswith(".") and author_tmp1[-1].isupper()):
                        author_tmp1 = author_tmp1 + "."
                    authors3.append(author_tmp1)

            authors_tmp2 = sorted(set(authors3))  # Получаем уникальные элементы
            for author in authors_tmp2:
                if len(author) > 2:
                    print(author)
                    stmt = insert(M_R_AUTHOR).values(
                        name_ru=author
                    )
                    session.execute(stmt)
                    session.commit()
            _cnt = len(authors_tmp2)
            content = {"msg": "Success", "count": _cnt, "data": authors_tmp2}
        return content
    except Exception as e:
        content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
        print("Exception occurred " + str(e))
        return content

@celery.task(name="report_update_subrf")
def report_update_subrf():
    content = {"msg": "Fail"}
    try:
        subrfs = []
        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        with Session(engine) as session:
            # truncate table
            stmt = text(f"TRUNCATE {M_R_SUBRF.__tablename__} RESTART IDENTITY;")
            session.execute(stmt)
            session.commit()
            #
            res = session.scalars(
                select(M_REPORT_TGF.subrf_name)
                .where(M_REPORT_TGF.subrf_name != '')
                .order_by(M_REPORT_TGF.subrf_name)
            )
            _all = res.all()
            for subrf_name in _all:
                subrf_tmp = str_clean(subrf_name).lstrip()
                if len(subrf_tmp) > 2:
                    subrfs.append(subrf_tmp)
            subrfs_str = ",".join(subrfs)
            subrfs2 = subrfs_str.split(",")
            subrfs3 = []
            # Обрабатываем список авторов и добавляем . если ее нет
            for subrf in subrfs2:
                if not subrf.startswith("<openpyxl"):
                    subrf_tmp1 = subrf.strip()
                    subrfs3.append(subrf_tmp1)

            subrfs_tmp2 = sorted(set(subrfs3))  # Получаем уникальные элементы
            for subrf in subrfs_tmp2:
                if len(subrf) > 2:
                    stmt = insert(M_R_SUBRF).values(
                        name_ru=subrf
                    )
                    session.execute(stmt)
                    session.commit()
            _cnt = len(subrfs_tmp2)
            content = {"msg": "Success", "count": _cnt, "data": subrfs_tmp2}
        return content
    except Exception as e:
        content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
        print("Exception occurred " + str(e))
        return content

@celery.task(name="report_update_org")
def report_update_org():
    content = {"msg": "Fail"}
    try:
        orgs = []
        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        with Session(engine) as session:
            stmt = text(f"TRUNCATE {M_R_ORG.__tablename__} RESTART IDENTITY;")
            session.execute(stmt)
            session.commit()
            #
            res = session.scalars(
                select(M_REPORT_TGF.org_name)
                .where(M_REPORT_TGF.org_name != '')
                .order_by(M_REPORT_TGF.org_name)
            )
            _all = res.all()
            for org_name in _all:
                org_tmp = str_clean(org_name).lstrip()
                if len(org_tmp) > 2:
                    orgs.append(org_tmp)
            orgs_str = ",".join(orgs)
            orgs2 = orgs_str.split(",")
            orgs3 = []
            # Обрабатываем список авторов и добавляем . если ее нет
            for org in orgs2:
                org_tmp1 = org.strip()
                if not org_tmp1.startswith("<openpyxl"):
                    orgs3.append(org_tmp1)

            orgs_tmp2 = sorted(set(orgs3))  # Получаем уникальные элементы
            for org in orgs_tmp2:
                if len(org) > 2:
                    stmt = insert(M_R_ORG).values(
                        name_ru=org
                    )
                    session.execute(stmt)
                    session.commit()
            _cnt = len(orgs_tmp2)
            content = {"msg": "Success", "count": _cnt, "data": orgs_tmp2}
        return content
    except Exception as e:
        content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
        print("Exception occurred " + str(e))
        return content


@celery.task(name="report_update_area")
def report_update_area():
    content = {"msg": "Fail"}
    try:
        areas = []
        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        with Session(engine) as session:
            stmt = text(f"TRUNCATE {M_R_AREA.__tablename__} RESTART IDENTITY;")
            session.execute(stmt)
            session.commit()
            res = session.scalars(
                select(M_REPORT_TGF.areaoil)
                .where(M_REPORT_TGF.areaoil != '')
                .order_by(M_REPORT_TGF.areaoil)
            )
            _all = res.all()
            for area_name in _all:
                area_tmp = str_clean(area_name).lstrip()
                if len(area_tmp) > 2:
                    areas.append(area_tmp)
            areas_str = ",".join(areas)
            areas2 = areas_str.split(",")
            areas3 = []
            for area in areas2:
                area_tmp1 = area.strip()
                if not area_tmp1.startswith("<openpyxl"):
                    areas3.append(area_tmp1)
            areas_tmp2 = sorted(set(areas3))  # Получаем уникальные элементы
            for area in areas_tmp2:
                if len(area) > 2:
                    stmt = insert(M_R_AREA).values(
                        name_ru=area
                    )
                    session.execute(stmt)
                    session.commit()
            _cnt = len(areas_tmp2)
            content = {"msg": "Success", "count": _cnt, "data": areas_tmp2}
        return content
    except Exception as e:
        content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
        print("Exception occurred " + str(e))
        return content

@celery.task(name="report_update_list")
def report_update_list():
    content = {"msg": "Fail"}
    try:
        lists = []
        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        with Session(engine) as session:            # truncate table
            stmt = text(f"TRUNCATE {M_R_LIST.__tablename__} RESTART IDENTITY;")
            session.execute(stmt)
            session.commit()
            #
            res = session.scalars(
                select(M_REPORT_TGF.list_name)
                .where(M_REPORT_TGF.list_name != '')
                .order_by(M_REPORT_TGF.list_name)
            )
            _all = res.all()
            for list_name in _all:
                list_tmp = list_str_clean(list_name)
                # print(author_tmp)
                if len(list_tmp) > 2:
                    lists.append(list_tmp)
            lists_str = ",".join(lists)
            lists2 = lists_str.split(",")
            lists3 = []
            # Обрабатываем список авторов и добавляем . если ее нет
            for author in lists2:
                author_tmp1 = author.strip()
                lists3.append(author_tmp1)

            lists_tmp2 = sorted(set(lists3))  # Получаем уникальные элементы
            for list in lists_tmp2:
                if len(list) > 2:
                    stmt = insert(M_R_LIST).values(
                        name_ru=list
                    )
                    session.execute(stmt)
                    session.commit()
            _cnt = len(lists_tmp2)
            content = {"msg": "Success", "count": _cnt, "data": lists_tmp2}
        return content
    except Exception as e:
        content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
        print("Exception occurred " + str(e))
        return content

@celery.task(name="report_update_field")
def report_update_field():
    content = {"msg": "Fail"}
    try:
        fields = []
        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        with Session(engine) as session:
        # truncate table
            stmt = text(f"TRUNCATE {M_R_FIELD.__tablename__} RESTART IDENTITY;")
            session.execute(stmt)
            session.commit()
            #
            res = session.scalars(
                select(M_REPORT_TGF.field)
                .where(M_REPORT_TGF.field != '')
                .order_by(M_REPORT_TGF.field)
            )
            _all = res.all()
            for field_name in _all:
                field_tmp = str_clean(field_name).lstrip()
                if len(field_tmp) > 2:
                    fields.append(field_tmp)
            fields_str = ",".join(fields)
            fields2 = fields_str.split(",")
            fields3 = []
            for field in fields2:
                field_tmp1 = field.strip()
                if not field_tmp1.startswith("<openpyxl"):
                    fields3.append(field_tmp1)

            fields_tmp2 = sorted(set(fields3))  # Получаем уникальные элементы
            for field in fields_tmp2:
                if len(field) > 2:
                    stmt = insert(M_R_FIELD).values(
                        name_ru=field
                    )
                    session.execute(stmt)
                    session.commit()
            _cnt = len(fields_tmp2)
            content = {"msg": "Success", "count": _cnt, "data": fields_tmp2}
        # log.info("ngp load successfully")
        return content
    except Exception as e:
        content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
        print("Exception occurred " + str(e))
        # fastapi_logger.exception("update_user_password")
        return content

@celery.task(name="report_update_lu")
def report_update_lu():
    content = {"msg": "Fail"}
    try:
        lus = []
        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        with Session(engine) as session:
            # truncate table
            stmt = text(f"TRUNCATE {M_R_LU.__tablename__} RESTART IDENTITY;")
            session.execute(stmt)
            session.commit()
            #
            res = session.scalars(
                select(M_REPORT_TGF.lu)
                .where(M_REPORT_TGF.lu != '')
                .order_by(M_REPORT_TGF.lu)
            )
            _all = res.all()
            for lu_name in _all:
                lu_tmp = str_clean(lu_name).lstrip()
                if len(lu_tmp) > 2:
                    lus.append(lu_tmp)
            lus_str = ",".join(lus)
            lus2 = lus_str.split(",")
            lus3 = []
            for lu in lus2:
                lu_tmp1 = lu.strip()
                if not lu_tmp1.startswith("<openpyxl"):
                    lus3.append(lu_tmp1)

            lus_tmp2 = sorted(set(lus3))  # Получаем уникальные элементы
            for lu in lus_tmp2:
                if len(lu) > 2:
                    stmt = insert(M_R_LU).values(
                        name_ru=lu
                    )
                    session.execute(stmt)
                    session.commit()
            _cnt = len(lus_tmp2)
            content = {"msg": "Success", "count": _cnt, "data": lus_tmp2}
        return content
    except Exception as e:
        content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
        print("Exception occurred " + str(e))
        return content


@celery.task(name="report_update_pi")
def report_update_pi():
    content = {"msg": "Fail"}
    try:
        pis = []
        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        with Session(engine) as session:
            # truncate table
            stmt = text(f"TRUNCATE {M_R_PI.__tablename__} RESTART IDENTITY;")
            session.execute(stmt)
            session.commit()
            #
            res = session.scalars(
                select(M_REPORT_TGF.pi_name)
                .where(M_REPORT_TGF.pi_name != '')
                .order_by(M_REPORT_TGF.pi_name)
            )
            _all = res.all()
            for pi_name in _all:
                pi_tmp = str_clean(pi_name).lstrip()
                if len(pi_tmp) > 2:
                    pis.append(pi_tmp)
            pis_str = ",".join(pis)
            pis2 = pis_str.split(",")
            pis3 = []
            for pi in pis2:
                pi_tmp1 = pi.strip()
                if not pi_tmp1.startswith("<openpyxl"):
                    pis3.append(pi_tmp1)

            pis_tmp2 = sorted(set(pis3))  # Получаем уникальные элементы
            for pi in pis_tmp2:
                if len(pi) > 2:
                    stmt = insert(M_R_PI).values(
                        name_ru=pi
                    )
                    session.execute(stmt)
                    session.commit()
            _cnt = len(pis_tmp2)
            content = {"msg": "Success", "count": _cnt, "data": pis_tmp2}
        return content
    except Exception as e:
        content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
        print("Exception occurred " + str(e))
        return content



@celery.task(name="report_update_vid_rab")
def report_update_vid_rab():
    content = {"msg": "Fail"}
    try:
        vid_rabs = []
        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        with Session(engine) as session:
            stmt = text(f"TRUNCATE {M_R_VID_RAB.__tablename__} RESTART IDENTITY;")
            session.execute(stmt)
            session.commit()
            #
            res = session.scalars(
                select(M_REPORT_TGF.vid_rab)
                .where(M_REPORT_TGF.vid_rab != '')
                .order_by(M_REPORT_TGF.vid_rab)
            )
            _all = res.all()
            for vid_rab_name in _all:
                vid_rab_tmp = str_clean(vid_rab_name).lstrip()
                if len(vid_rab_tmp) > 2:
                    vid_rabs.append(vid_rab_tmp)
            vid_rabs_str = ",".join(vid_rabs)
            vid_rabs2 = vid_rabs_str.split(",")
            vid_rabs3 = []
            for vid_rab in vid_rabs2:
                vid_rab_tmp1 = vid_rab.strip()
                if not vid_rab_tmp1.startswith("<openpyxl"):
                    vid_rabs3.append(vid_rab_tmp1)

            vid_rabs_tmp2 = sorted(set(vid_rabs3))  # Получаем уникальные элементы
            for vid_rab in vid_rabs_tmp2:
                if len(vid_rab) > 2:
                    stmt = insert(M_R_VID_RAB).values(
                        name_ru=vid_rab
                    )
                    session.execute(stmt)
                    session.commit()
            _cnt = len(vid_rabs_tmp2)
            content = {"msg": "Success", "count": _cnt, "data": vid_rabs_tmp2}
        return content
    except Exception as e:
        content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
        print("Exception occurred " + str(e))
        return content

@celery.task(name="report_index_create_task")
def report_index_create_task():
    content = {"msg": "Fail"}

    try:
        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        with Session(engine) as session:
            print(f"Удаляем индекс {cfg.REPORT_FTS_INDEX}")
            stmt = text(f"DROP INDEX IF EXISTS {cfg.REPORT_FTS_INDEX};")
            res = session.execute(stmt)
            print(res)

            print(f"Создаем TSVector ...")
            stmt = text(
                f"UPDATE {M_REPORT_TGF.__tablename__} SET {M_REPORT_TGF.report_fts.key} = TO_TSVECTOR('russian', {M_REPORT_TGF.report_name.key} ||' '|| {M_REPORT_TGF.org_name.key} ) ;")
            res = session.execute(stmt)
            print(res)

            print(f"Создаем индекс ...")
            stmt = text(
                f"CREATE INDEX IF NOT EXISTS {cfg.REPORT_FTS_INDEX} ON {M_REPORT_TGF.__tablename__} USING GIN ({M_REPORT_TGF.report_fts.key});")
            print(stmt)
            res = session.execute(stmt)
            print(res)
            session.commit()
        print("OK")
        content = {"msg": "Success", "count": 0}

    except Exception as e:
        content = {"msg": f"can't create index {cfg.REPORT_FTS_INDEX}"}
        print("Exception occurred " + str(e))
        return content
    finally:
        if session is not None:
            session.close()
    return content

@celery.task(name="report_update_history")
def report_update_history(query_str: str, client_host: str):
    try:

        engine = sqlalchemy.create_engine(cfg.DB_DSN2)
        with Session(engine) as session:
            stmt = insert(M_HISTORY).values(
                search_str=query_str,
                addr_ip=client_host
            )
            session.execute(stmt)
            session.commit()
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"ERROR in report_update_history!!!", "err": str(e)}
        print(str_err)
