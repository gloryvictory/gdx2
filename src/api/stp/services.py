from sqlalchemy import select, func
from src import cfg
from src.db.db import async_session_maker
from src.models import M_STP


async def stp_get_all():
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_STP) # .order_by(M_NSI_AREA.name_ru)
            )
            _all = res.all()
            cnt = len(_all)
            content = {"msg": cfg.MSG_OK, "count": cnt, "data": _all}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_STP.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def stp_get_all_count():
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            res = await session.scalar(select(func.count(M_STP.id)))
            content = {"msg": cfg.MSG_OK, "count": res}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_STP.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def stp_get_by_id(id: int = 0):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            res = await session.get(M_STP, id)
            _all = res
            content = {"msg": cfg.MSG_OK, "count": 1, "data": _all}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_STP.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
        #     session.close()
    return content


async def stp_get_by_rosg(rosg: str = ''):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_STP)
                .where(M_STP.in_n_rosg == rosg)
            )
            _all = res.all()
            cnt = len(_all)
            content = {"msg": cfg.MSG_OK, "count": cnt, "data": _all}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_STP.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
        #     session.close()
    return content


async def stp_get_count_by_rosg(rosg: str = ''):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_STP)
                .where(M_STP.in_n_rosg == rosg)
            )
            _all = res.all()
            cnt = len(_all)
            content = {"msg": cfg.MSG_OK, "count": cnt}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_STP.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
        #     session.close()
    return content
