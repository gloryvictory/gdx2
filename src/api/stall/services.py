# import json
# import os
# import hashlib

from sqlalchemy import select, func
from src import cfg
from src.db.db import async_session_maker
# from src.log import set_logger
from src.models import M_STA, M_STL, M_STP


# Получаем методы
async def stall_get_all_method():
    content = {"msg": cfg.MSG_ERROR}
    # log = set_logger(cfg.AREA_FILE_LOG)

    try:
        async with async_session_maker() as session:
            res_sta = await session.scalars(
                select(M_STA.method)
                .where(M_STA.method.is_not(None))  # Фильтруем NOT NULL
                .distinct()  # Добавляем distinct для получения уникальных значений
                .order_by(M_STA.method)
            )
            _all_sta = res_sta.all()

            res_stl = await session.scalars(
                select(M_STL.method)
                .where(M_STL.method.is_not(None))  # Фильтруем NOT NULL
                .distinct()  # Добавляем distinct для получения уникальных значений
                .order_by(M_STL.method)
            )
            _all_stl = res_stl.all()

            res_stp = await session.scalars(
                select(M_STP.method)
                .where(M_STP.method.is_not(None))  # Фильтруем NOT NULL
                .distinct()  # Добавляем distinct для получения уникальных значений
                .order_by(M_STP.method)
            )
            _all_stp = res_stp.all()

            all_stall = _all_sta + _all_stl + _all_stp
            all_uniq = set(all_stall)
            _all: list = sorted(all_uniq)  # sorted возвращает новый отсортированный список
            cnt = len(_all)
            content = {"msg": cfg.MSG_OK, "count": cnt, "data": _all}
            # log.info("ngp load successfully")
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_STA.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


# Получаем Вид изученности
async def stall_get_all_vid_iz():
    content = {"msg": cfg.MSG_ERROR}
    # log = set_logger(cfg.AREA_FILE_LOG)

    try:
        async with async_session_maker() as session:
            res_sta = await session.scalars(
                select(M_STA.vid_iz)
                .where(M_STA.vid_iz.is_not(None))  # Фильтруем NOT NULL
                .distinct()  # Добавляем distinct для получения уникальных значений
                .order_by(M_STA.vid_iz)
            )
            _all_sta = res_sta.all()

            res_stl = await session.scalars(
                select(M_STL.vid_iz)
                .where(M_STL.vid_iz.is_not(None))  # Фильтруем NOT NULL
                .distinct()  # Добавляем distinct для получения уникальных значений
                .order_by(M_STL.vid_iz)
            )
            _all_stl = res_stl.all()

            res_stp = await session.scalars(
                select(M_STP.vid_iz)
                .where(M_STP.vid_iz.is_not(None))  # Фильтруем NOT NULL
                .distinct()  # Добавляем distinct для получения уникальных значений
                .order_by(M_STP.vid_iz)
            )
            _all_stp = res_stp.all()

            all_stall = _all_sta + _all_stl + _all_stp
            all_uniq = set(all_stall)
            _all: list = sorted(all_uniq)  # sorted возвращает новый отсортированный список
            cnt = len(_all)
            content = {"msg": cfg.MSG_OK, "count": cnt, "data": _all}
            # log.info("ngp load successfully")
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_STA.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content

# Получаем Год начала
async def stall_get_all_god_nach():
    content = {"msg": cfg.MSG_ERROR}
    # log = set_logger(cfg.AREA_FILE_LOG)

    try:
        async with async_session_maker() as session:
            res_sta = await session.scalars(
                select(M_STA.god_nach)
                .where(M_STA.god_nach.is_not(None))  # Фильтруем NOT NULL
                .distinct()  # Добавляем distinct для получения уникальных значений
                .order_by(M_STA.god_nach)
            )
            _all_sta = res_sta.all()

            res_stl = await session.scalars(
                select(M_STL.god_nach)
                .where(M_STL.god_nach.is_not(None))  # Фильтруем NOT NULL
                .distinct()  # Добавляем distinct для получения уникальных значений
                .order_by(M_STL.god_nach)
            )
            _all_stl = res_stl.all()

            res_stp = await session.scalars(
                select(M_STP.god_nach)
                .where(M_STP.god_nach.is_not(None))  # Фильтруем NOT NULL
                .distinct()  # Добавляем distinct для получения уникальных значений
                .order_by(M_STP.god_nach)
            )
            _all_stp = res_stp.all()

            all_stall = _all_sta + _all_stl + _all_stp
            all_uniq = set(all_stall)
            _all: list = sorted(all_uniq)  # sorted возвращает новый отсортированный список
            cnt = len(_all)
            content = {"msg": cfg.MSG_OK, "count": cnt, "data": _all}
            # log.info("ngp load successfully")
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_STA.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content





