import asyncio
import hashlib
import asyncpg
import os  # Load the Library Module
import os.path
from datetime import datetime
import logging as log
from multiprocessing import JoinableQueue as Queue

# from asyncio import sleep
# import csv
# from multiprocessing import Lock
# from multiprocessing.pool import Pool
# from src import cfg

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


async def db_insert(db_pool, root_folder: str, root: str, file: str):
    # conn = await asyncpg.connect("postgresql://gdx2:gdx2pwd@localhost:5432/gdx2")
    try:
        f_root = root_folder
        f_name = file
        file_split = os.path.splitext(file)
        f_ext = str(file_split[1]).replace(".", "").lower()
        f_path = str(os.path.join(root, file))
        f_folder = root

        stat_file = os.stat(f_folder)

        f_size = stat_file.st_size
        f_ctime = datetime.fromtimestamp(stat_file.st_ctime)
        f_mtime = datetime.fromtimestamp(stat_file.st_mtime)
        f_atime = datetime.fromtimestamp(stat_file.st_atime)
        hash_object = hashlib.md5(f_path.encode())
        f_path_md5 = hash_object.hexdigest()
        lastupdate = datetime.now()

        QUERY = "INSERT INTO file (f_root, f_path, f_folder, f_name, f_ext, f_size, f_ctime, f_mtime, f_atime, f_path_md5, lastupdate ) VALUES ($1,$2, $3, $4, $5, $6, $7, $8, $9, $10, $11)"

        await db_pool.fetch(QUERY, f_root, f_path, f_folder, f_name, f_ext, f_size, f_ctime, f_mtime, f_atime, f_path_md5, lastupdate )
        print(f_path)

        # root_folder: str = Column(TEXT, index=True, )
        # file_path: str = Column(TEXT, index=True, )
        # file_folder: str = Column(TEXT, index=True, )
        # file_name: str = Column(String(length=255), index=True, )
        # file_ext: str = Column(String(length=11), index=True, )
        # file_size: int = Column(BigInteger)
        # file_ctime: str = Column(TIMESTAMP, default=datetime.now)
        # file_mtime: str = Column(TIMESTAMP, default=datetime.now)
        # date_c: str = Column(String(length=11))
        # date_m: str = Column(String(length=11))
        # date_u: str = Column(String(length=11))
        # fpath: str = Column(TEXT)
        # fpath_md5: str = Column(TEXT)
        # file_text: str = Column(TEXT)
        # field: str = Column(String(length=255), index=True, )
        # areaoil: str = Column(String(length=255), index=True, )
        # lu: str = Column(String(length=255), index=True, )
        # well: str = Column(String(length=255), index=True, )
        # lat: float = Column(Float)
        # lon: float = Column(Float)
        # report_name: str = Column(TEXT, index=True, )
        # report_text: str = Column(TEXT)
        # report_author: str = Column(TEXT, index=True, )
        # report_year: int = Column(Integer, index=True, )
        # report_tgf: str = Column(TEXT)
        # is_deleted: bool = Column(Boolean, default=False)
        # lastupdate: datetime = Column(TIMESTAMP, default=datetime.now)
        # file_path_fts: str = Column(TSVECTOR)

    except Exception as e:
        # file_ext
        print(f_path)
        # print(file_ext)
        print("Exception occurred: " + str(e))  # , exc_info=True


def folder_get_files_count(path: str):
    files_cnt = 0
    for root, dirs, files in os.walk(path):
        for _ in files:
            files_cnt += 1
    return files_cnt


async def folder2pg(root_folder: str):
    global total_files
    db_pool = await asyncpg.create_pool("postgresql://gdx2:gdx2pwd@localhost:5432/gdx2")
    paths = explore_path(root_folder)
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
                tasks.append(asyncio.create_task(db_insert(db_pool, root_folder, root, file)))
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
    # global root_folder
    root_folder = f"C:\\TEMP"
    await folder2pg(root_folder)
    # await folder2pg("C:\\")
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
