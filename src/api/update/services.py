import json
import os
from datetime import datetime

from sqlalchemy import insert, text, select, update, func

from src import cfg
from src.api.celery.tasks import update_file_by_ngp_str
from src.db.db import async_session_maker
from src.log import set_logger
from src.models import M_NSI_NGP, M_FILE


def get_ngp_name(ngp_in: str):
    ngp_str = ngp_in.replace("пнгп", "")
    ngp_str = ngp_str.replace("нгп", "")
    return ngp_str.lower().strip()


async def update_by_ngp():
    content = {"msg": f"error"}
    log = set_logger(cfg.NGP_FILE_LOG)
    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_NSI_NGP)
                .order_by(M_NSI_NGP.name_ru)
            )
            _all = res.all()
            cnt = len(_all)
            for ngp in _all:
                ngp_str = get_ngp_name(ngp.name_ru)
                lat = float(ngp.lat)
                lon = float(ngp.lon)
                print(ngp_str)
                await update_file_by_ngp(ngp_str, lat, lon)

            content = {"msg": "Success", "count": cnt, "data": _all}

            return content
    except Exception as e:
        cont_err = f"fail. can't read ngp from table ({M_NSI_NGP.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def update_file_by_ngp(ngp_str: str, lat: float, lon: float):
    content = {"msg": f"error"}
    try:
        async with async_session_maker() as session:
            time1 = datetime.now()
            # log = set_logger(cfg.NGP_FILE_LOG)
            print(f"Обработка: {ngp_str}")
            # log.INFO(f"Обработка: {ngp_str}")
            # через полнотекстовый поиск (но он выдает больше результатов, т.к. для него Частная и Частный одно и то же)
            # res = await session.scalars(
            #     select(M_FILE)
            #     .where(M_FILE.file_path_fts.match(ngp_str, postgresql_regconfig='russian'))
            #     .order_by(M_FILE.f_path)
            # )
            ngp_str_new = f"%{ngp_str}%"
            res = await session.scalars(
                select(M_FILE)
                .where(M_FILE.f_path.ilike(ngp_str_new) ) # lower(f.f_path) like LOWER('%частная%')
                .order_by(M_FILE.f_path)
            )
            # func.lower(M_FILE.f_path)
            # .where(M_FILE.file_path_fts.match(ngp_str, postgresql_regconfig='russian'))

            _all = res.all()
            cnt = len(_all)
            for file in _all:
                f_path_md5 = file.f_path_md5
                update_file_by_ngp_str.delay(ngp_str, lat, lon, f_path_md5)
                # print(file.f_path)
                # f_path_md5 = file.f_path_md5
                # stmt = (
                #     update(M_FILE)
                #     .where(M_FILE.f_path_md5 == f_path_md5)
                #     .values(ngp=ngp_str, lat=lat, lon=lon)
                # )
                # await session.execute(stmt)
                # await session.commit()

            content = {"msg": "Success"}
            time2 = datetime.now()
            print(f"Обработано: {ngp_str}. Total time:  + {str(time2 - time1)}")
            return content
    except Exception as e:
        cont_err = f"fail. can't read file from table ({M_NSI_NGP.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content
