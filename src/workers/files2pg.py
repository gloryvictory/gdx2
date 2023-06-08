import asyncio
from asyncio import sleep
import asyncpg

import os  # Load the Library Module
import os.path
from datetime import datetime
# import csv
import logging as log
# from multiprocessing import Lock
from multiprocessing.pool import Pool
from multiprocessing import JoinableQueue as Queue

from src import cfg

global unsearched
unsearched = Queue()  # queue for hold the next directories for the processes

global total_files
total_files = 0  # global total_files


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
        path = unsearched.get()
        print(f"path: {path}")
        print(f"q: {unsearched.qsize()}")
        files_cnt = 0
        for root, dirs, files in os.walk(path):
            for file in files:
                print(f"{root}+ '\\'+ {file}")
                # db_client.add(root, file)
                # await db_insert(root, file)
                # conn = await asyncpg.connect()
                files_cnt += 1
        str_msg = f"Files in folder {path} : {files_cnt}"
        # files_stat_db.add(path, files_cnt)
        global total_files
        total_files = total_files + files_cnt
        log.info(str_msg)
        print(str_msg)
        unsearched.task_done()


async def db_insert(db_pool, root: str, file: str):
    # conn = await asyncpg.connect("postgresql://gdx2:gdx2pwd@localhost:5432/gdx2")
    file_split = os.path.splitext(file)
    file_ext = str(file_split[1]).replace(".", "")
    file_full_path = str(os.path.join(root, file))
    QUERY = "INSERT INTO file (file_path, file_ext) VALUES ($1,$2)"

    await db_pool.fetch(QUERY, file_full_path, file_ext)
    print(file_full_path)


def folder_get_files_count(path: str):
    files_cnt = 0
    for root, dirs, files in os.walk(path):
        for _ in files:
            files_cnt += 1
    return files_cnt


async def folder2pg(folder_in: str):
    global total_files
    db_pool = await asyncpg.create_pool("postgresql://gdx2:gdx2pwd@localhost:5432/gdx2")
    paths = explore_path(folder_in)
    chunk = 200
    tasks = []
    pended = 0
    # for path in paths:
    #     unsearched.put(path)

    for path in paths:
        files_cnt = folder_get_files_count(path)
        for root, dirs, files in os.walk(path):
            for file in files:
                print(f"{root}\{file}")
                tasks.append(asyncio.create_task(db_insert(db_pool, root, file)))
                pended += 1
                total_files += 1
                if len(tasks) == chunk or pended == files_cnt:
                    await asyncio.gather(*tasks)
                    tasks = []
                    print(pended)


# async def make_request(db_pool):
#     QUERY = "INSERT INTO test VALUES ($1,$2,$3)"
#     await db_pool.fetch(QUERY, 1, "some striing", 3)
#     await sleep(.1)


async def main():
    # global db_pool
    # db_pool = await asyncpg.create_pool("postgresql://gdx2:gdx2pwd@localhost:5432/gdx2")
    time1 = datetime.now()
    print('Starting at :' + str(time1))
    str_msg = f"Total files: {total_files}"
    log.info(str_msg)
    print(str_msg)
    # await folder2pg("C:\\TEMP\\Geodex_files\\")
    await folder2pg("C:\\TEMP")
    # chunk = 200
    # tasks = []
    # pended = 0

    # for x in range(10_000):
    #     tasks.append(asyncio.create_task(make_request(db_pool)))
    #     pended += 1
    #     if len(tasks) == chunk or pended == 10000:
    #         await asyncio.gather(*tasks)
    #         tasks = []
    #         print(pended)

    time2 = datetime.now()
    print(f"Total files: {total_files}")
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
