# import json
# import os
# import hashlib

from sqlalchemy import select, func
from src import cfg
from src.db.db import async_session_maker
# from src.log import set_logger
from src.models import M_STA


async def sta_get_all():
    content = {"msg": cfg.MSG_ERROR}
    # log = set_logger(cfg.AREA_FILE_LOG)

    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_STA)
                # .order_by(M_NSI_AREA.name_ru)
            )
            _all = res.all()
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


async def sta_get_all_count():
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            res = await session.scalar(select(func.count(M_STA.id)))
            content = {"msg": cfg.MSG_OK, "count": res}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_STA.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def sta_get_by_id(id: int = 0):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            res = await session.get(M_STA, id)
            _all = res
            content = {"msg": cfg.MSG_OK, "count": 1, "data": _all}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_STA.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
        #     session.close()
    return content


async def sta_get_by_rosg(rosg: str = ''):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_STA)
                .where(M_STA.in_n_rosg == rosg)
            )
            _all = res.all()
            cnt = len(_all)
            content = {"msg": cfg.MSG_OK, "count": cnt, "data": _all}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_STA.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
        #     session.close()
    return content


async def sta_get_count_by_rosg(rosg: str = ''):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_STA)
                .where(M_STA.in_n_rosg == rosg)
            )
            _all = res.all()
            cnt = len(_all)
            content = {"msg": cfg.MSG_OK, "count": cnt}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_STA.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
        #     session.close()
    return content

# Получаем методы
async def sta_get_all_method():
    content = {"msg": cfg.MSG_ERROR}
    # log = set_logger(cfg.AREA_FILE_LOG)

    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_STA.method)
                .where(M_STA.method.is_not(None))  # Фильтруем NOT NULL
                .distinct()  # Добавляем distinct для получения уникальных значений
                .order_by(M_STA.method)
            )
            _all = res.all()
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
