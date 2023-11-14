import json
import os
from datetime import datetime

from sqlalchemy import insert, text, select, update, func

from src import cfg
from src.api.celery.tasks import update_file_by_ngp_str2, update_file_by_ngo_str2, update_file_by_ngr_str2, \
    update_file_by_area_str2
from src.db.db import async_session_maker
from src.log import set_logger
from src.models import M_NSI_NGP, M_FILE, M_NSI_NGO, M_NSI_NGR, M_NSI_AREA


# НГ провинции
def get_ngp_name(ngp_in: str):
    ngp_str = ngp_in.replace("пнгп", "")
    ngp_str = ngp_str.replace("нгп", "")
    return ngp_str.lower().strip()


async def update_by_ngp():
    content = {"msg": f"error"}
    # log = set_logger(cfg.NGP_FILE_LOG)

    try:
        time1 = datetime.now()
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_NSI_NGP)
                .order_by(M_NSI_NGP.name_ru)
            )
            _all = res.all()
            cnt = len(_all)
            if cfg.DEVENV.startswith("dev"):
                print("Development mode!!!")
                ngp = _all[0]
                ngp_str = get_ngp_name(ngp.name_ru)
                lat = float(ngp.lat)
                lon = float(ngp.lon)
                print(ngp_str)
                update_file_by_ngp_str2.delay(ngp_str, lat, lon)
            else:
                for ngp in _all:
                    ngp_str = get_ngp_name(ngp.name_ru)
                    lat = float(ngp.lat)
                    lon = float(ngp.lon)
                    print(ngp_str)
                    update_file_by_ngp_str2.delay(ngp_str, lat, lon)
            content = {"msg": "Success", "count": cnt, "data": _all}
        time2 = datetime.now()
        print(f"Обработаны все НГП: Total time:  + {str(time2 - time1)}")
        return content
    except Exception as e:
        cont_err = f"fail. can't read ngp from table ({M_NSI_NGP.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


# НГ Области

def get_ngo_name(ngo_in: str):
    ngo_str = ngo_in.replace(" пнго", "")
    ngo_str = ngo_str.replace(" нго", "")
    ngo_str = ngo_str.replace(" пго", "")
    ngo_str = ngo_str.replace(" снго", "")
    ngo_str = ngo_str.replace(" сно", "")
    ngo_str = ngo_str.replace(" спнго", "")
    ngo_str = ngo_str.replace(" гно", "")
    ngo_str = ngo_str.replace("  нг", "")
    ngo_str = ngo_str.replace("пнго ", "")
    return ngo_str.lower().strip()


async def update_by_ngo():
    content = {"msg": f"error"}
    try:
        time1 = datetime.now()
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_NSI_NGO)
                .order_by(M_NSI_NGO.name_ru)
            )
            _all = res.all()
            cnt = len(_all)
            if cfg.DEVENV.startswith("dev"):
                print("Development mode!!!")
                ngo = _all[0]
                ngo_str = get_ngo_name(ngo.name_ru)
                lat = float(ngo.lat)
                lon = float(ngo.lon)
                print(f"{ngo_str} {lat} {lon}")
                update_file_by_ngo_str2.delay(ngo_str, lat, lon)
            else:
                for ngo in _all:
                    ngo_str = get_ngo_name(ngo.name_ru)

                    lat = float(ngo.lat)
                    lon = float(ngo.lon)
                    print(f"{ngo_str} {lat} {lon}")
                    update_file_by_ngo_str2.delay(ngo_str, lat, lon)
            content = {"msg": "Success", "count": cnt, "data": _all}
        time2 = datetime.now()
        print(f"Обработаны все НГО: Total time:  + {str(time2 - time1)}")
        return content
    except Exception as e:
        cont_err = f"fail. can't read ngp from table ({M_NSI_NGO.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content

# НГ Районы
def get_ngr_name(ngr_in: str):
    ngr_str = ngr_in.replace(" пнгр", "")
    ngr_str = ngr_str.replace("пнгр ", "")
    ngr_str = ngr_str.replace(" нр", "")
    ngr_str = ngr_str.replace(" гр", "")
    ngr_str = ngr_str.replace(" нгр", "")
    ngr_str = ngr_str.replace(" снгр", "")
    ngr_str = ngr_str.replace(" спнгр", "")
    ngr_str = ngr_str.replace("нгр ", "")
    ngr_str = ngr_str.replace(" нг", "")
    ngr_str = ngr_str.replace(" пгр", "")
    ngr_str = ngr_str.replace("", "")
    return ngr_str.lower().strip()


async def update_by_ngr():
    content = {"msg": f"error"}
    try:
        time1 = datetime.now()
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_NSI_NGR)
                .order_by(M_NSI_NGR.name_ru)
            )
            _all = res.all()
            cnt = len(_all)
            if cfg.DEVENV.startswith("dev"):
                print("Development mode!!!")
                ngr = _all[1]
                ngr_str = get_area_name(ngr.name_ru)
                # проверяем что НГР не пустая
                if len(ngr_str) > 3:
                    lat = float(ngr.lat)
                    lon = float(ngr.lon)
                    # print(f"{ngr.name_ru} {lat} {lon}")
                    print(f"{ngr_str} {lat} {lon}")
                    update_file_by_ngr_str2.delay(ngr_str, lat, lon)
            else:
                for ngr in _all:
                    ngr_str = get_area_name(ngr.name_ru)
                    # проверяем что НГР не пустая
                    if len(ngr_str) > 3:
                        lat = float(ngr.lat)
                        lon = float(ngr.lon)
                        # print(f"{ngr_str} {lat} {lon}")
                        print(f"{ngr_str}")
                        update_file_by_ngr_str2.delay(ngr_str, lat, lon)
            content = {"msg": "Success", "count": cnt, "data": _all}
        time2 = datetime.now()
        print(f"Обработаны все НГР: Total time:  + {str(time2 - time1)}")
        return content
    except Exception as e:
        cont_err = f"fail. can't read ngp from table ({M_NSI_NGR.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content

# Площади
def get_area_name(area: str):
    area_str = area.replace("  ", "")
    return area_str.lower().strip()


async def update_by_area():
    content = {"msg": f"error"}
    try:
        time1 = datetime.now()
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_NSI_AREA)
                .order_by(M_NSI_AREA.name_ru)
            )
            _all = res.all()
            cnt = len(_all)
            if cfg.DEVENV.startswith("dev"):
                print("Development mode!!!")
                area = _all[0]
                area_str = get_area_name(area.name_ru)
                # проверяем что Площадь не пустая
                if len(area_str) > 3:
                    lat = float(area.lat)
                    lon = float(area.lon)
                    # print(f"{ngr.name_ru} {lat} {lon}")
                    print(f"{area_str} {lat} {lon}")
                    update_file_by_area_str2.delay(area_str, lat, lon)
            else:
                for area in _all:
                    area_str = get_area_name(area.name_ru)
                    # проверяем что Площадь не пустая
                    if len(area_str) > 3:
                        lat = float(area.lat)
                        lon = float(area.lon)
                        # print(f"{ngr_str} {lat} {lon}")
                        print(f"{area_str}")
                        update_file_by_area_str2.delay(area_str, lat, lon)
            content = {"msg": "Success", "count": cnt, "data": _all}
        time2 = datetime.now()
        print(f"Обработаны все НГР: Total time:  + {str(time2 - time1)}")
        return content
    except Exception as e:
        cont_err = f"fail. can't read ngp from table ({M_NSI_NGR.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


















# await update_file_by_ngp_str2(ngp_str, lat, lon)
# result = update_file_by_ngp_str2.delay(ngp_str, lat, lon)
# while not result.ready():
#     pass
# print(result.get())

# async with async_session_maker() as session:
#     time1 = datetime.now()
#     # log = set_logger(cfg.NGP_FILE_LOG)
#     print(f"Обработка: {ngp_str}")
#     # log.INFO(f"Обработка: {ngp_str}")
#     # через полнотекстовый поиск (но он выдает больше результатов, т.к. для него Частная и Частный одно и то же)
#     # res = await session.scalars(
#     #     select(M_FILE)
#     #     .where(M_FILE.file_path_fts.match(ngp_str, postgresql_regconfig='russian'))
#     #     .order_by(M_FILE.f_path)
#     # )
#
#     update_file_by_ngp_str2.delay(ngp_str, lat, lon)
#
# ngp_str_new = f"%{ngp_str}%"
# res = await session.scalars(
#     select(M_FILE)
#     .where(M_FILE.f_path.ilike(ngp_str_new) ) # lower(f.f_path) like LOWER('%частная%')
#     .order_by(M_FILE.f_path)
# )
# # func.lower(M_FILE.f_path)
# # .where(M_FILE.file_path_fts.match(ngp_str, postgresql_regconfig='russian'))
#
# _all = res.all()
# cnt = len(_all)
# for file in _all:
#     f_path_md5 = file.f_path_md5
#     update_file_by_ngp_str.delay(ngp_str, lat, lon, f_path_md5)
#     # print(file.f_path)
#     # f_path_md5 = file.f_path_md5
#     # stmt = (
#     #     update(M_FILE)
#     #     .where(M_FILE.f_path_md5 == f_path_md5)
#     #     .values(ngp=ngp_str, lat=lat, lon=lon)
#     # )
#     # await session.execute(stmt)
#     # await session.commit()
