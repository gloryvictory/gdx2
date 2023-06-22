#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author          : Viacheslav Zamaraev
#   email           : zamaraev@gmail.com
#   Script Name     : folder2pg.py
#   Created         : 06.06.2023
#   Last Modified	: 06.06.2023
#   Version		    : 1.0
#   PIP             :
#   RESULT          :
# Modifications	: 1.1 -
#               : 1.2 -
#
# Description   : folder to PG


import os  # Load the Library Module
import os.path
from datetime import datetime
# import csv
import logging as log
from multiprocessing.pool import Pool
from multiprocessing import JoinableQueue as Queue

from src import cfg


from src.examples.files2pg_class import Files2DB

global unsearched
unsearched = Queue()  # queue for hold the next directories for the processes

# global total_files
total_files = 0


def explore_path(path):
    # explore files and directories
    directories = []
    for filename in os.listdir(path):
        fullname = os.path.join(path, filename)
        if os.path.isdir(fullname):
            directories.append(fullname)
            print(f"fullname: {fullname}")
    return directories


async def parallel_worker():
    while not unsearched.empty():
        db_client = Files2DB()
        # files_stat_db = Files2DB_stat()

        # with Session(engine) as session:
        #     query = select(FILE_SRC_M)
        #     result = session.execute(query)
        #     all_data = result.all()
        #     all_count = len(all_data)
        #     print(f"Надено: {all_count}")

        path = unsearched.get()

        print(f"path: {path}")
        print(f"q: {unsearched.qsize()}")
        files_cnt = 0
        for root, dirs, files in os.walk(path):
            for file in files:
                db_client.add(root, file)
                files_cnt += 1

        str_msg = f"Files in folder {path} : {files_cnt}"

        # files_stat_db.add(path, files_cnt)

        global total_files
        total_files = total_files + files_cnt
        log.info(str_msg)
        print(str_msg)
        unsearched.task_done()


def folder2p(folder_in: str):
    time1 = datetime.now()
    print('Starting at :' + str(time1))
    str_msg = f"Total files: {total_files}"
    log.info(str_msg)
    print(str_msg)

    paths = explore_path(folder_in)
    for path in paths:
        unsearched.put(path)
    num_processes = int(cfg.NUMBER_PROCESS)
    with Pool(num_processes) as pool:
        for i in range(num_processes):
            pool.apply_async(parallel_worker())
    unsearched.join()

    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')
