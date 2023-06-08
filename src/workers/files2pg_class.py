import os
from datetime import datetime
import hashlib

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.cfg import DB_DSN
from src.database import engine
from src.models import FILE_M


# def db_get_connection():
#     engine = create_engine(DB_DSN)
#     # db = SqliteDatabase('test.db')
#     return engine


class Files2DB:
    '''
    Creation of class files2pg in the project
    '''

    def __init__(self):
        self.engine = db_get_connection()

    @staticmethod
    async def add(root, file):
        try:
            # print(f'root{root}')
            # print(file)
            file_split = os.path.splitext(file)
            file_ext = str(file_split[1]).replace(".", "")

            file_full_path = str(os.path.join(root, file))

            # session = Session(bind=db_get_connection())
            async with Session(engine) as session:
                new_src = FILE_M(root_folder=root, file_path=file_full_path)
                session.add(new_src)
                await session.commit()

            print(f"fuul path: {file_full_path}")
            # stat_file = os.stat(file_full_path)
            #
            # # _Files = Files()
            # file_name = file
            # file_path = file_full_path
            # file_folder = root
            # file_ext = file_ext.lower()
            # file_size = stat_file.st_size
            #
            # file_ctime = datetime.fromtimestamp(stat_file.st_ctime)
            # file_mtime = datetime.fromtimestamp(stat_file.st_mtime)
            #
            # date_c = datetime.fromtimestamp(stat_file.st_ctime).strftime('%Y-%m-%d')
            # date_m = datetime.fromtimestamp(stat_file.st_mtime).strftime('%Y-%m-%d')
            # date_u = datetime.now().strftime('%Y-%m-%d')
            #
            # # _Files.lastupdate = datetime.now()
            # str_without_root = root.replace(cfg.FOLDER_IN + os.sep, "")
            # str_root_folder = str_without_root.split(os.sep)[0]
            #
            # if len(str_root_folder):
            #     root_folder = str_root_folder
            # else:
            #     root_folder = ''
            #
            # str_ffp = str_without_root
            # fpath = str_ffp
            #
            # hash_object = hashlib.md5(str_ffp.encode())
            # fpath_md5 = hash_object.hexdigest()

            # _Files.save()
        except Exception as e:
            print("Exception occurred: " + str(e))  # , exc_info=True
