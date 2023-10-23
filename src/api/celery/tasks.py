from datetime import datetime
import asyncio

import sqlalchemy
from sqlalchemy.orm import Session

from celery import Celery
from sqlalchemy import update, MetaData, NullPool
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src import cfg
from src.db.db import async_session_maker
from src.log import set_logger
from src.models import M_FILE

celery = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

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


# , lat: float, lon: float, *args, **kwargs
@celery.task(name="update_file_by_ngp")
def update_file_by_ngp_str2(ngp_str: str, lat: float, lon: float):
    # ngp_str: str = "qweqweqweqwe"
    print(f"Обработано: {ngp_str} {lat} {lon}.!!!!!!")
    try:
        print(f"Обработано: {ngp_str}.!!!!!!")
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
            print(f"Обработано: {ngp_str}. Total time:  + {str(time2 - time1)}")
    except Exception as e:
        cont_err = f"fail. can't read or update data from table ({M_FILE.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            session.close()
