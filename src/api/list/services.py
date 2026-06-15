import uuid
from sqlalchemy import select, func
from src import cfg
from src.db.db import async_session_maker
# from src.log import set_logger
from src.models import M_R_LIST


async def list_get_all():
    content = {"msg": cfg.MSG_ERROR}
    # log = set_logger(cfg.AREA_FILE_LOG)

    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_R_LIST)
            )
            _all = res.all()
            cnt = len(_all)
            content = {"msg": cfg.MSG_OK, "count": cnt, "data": _all}
            # log.info("list load successfully")
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_R_LIST.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def list_get_all_count():
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            res = await session.scalar(select(func.count(M_R_LIST.guid)))
            content = {"msg": cfg.MSG_OK, "count": res}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_R_LIST.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def list_get_by_id(guid: uuid.UUID):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            res = await session.get(M_R_LIST, guid)
            content = {"msg": cfg.MSG_OK, "count": 1 if res else 0, "data": res}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_R_LIST.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def list_create(name_ru: str):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            new_list = M_R_LIST(name_ru=name_ru)
            session.add(new_list)
            await session.commit()
            await session.refresh(new_list)
            content = {"msg": cfg.MSG_OK, "count": 1, "data": new_list}
            return content
    except Exception as e:
        cont_err = f"fail. can't create record in table ({M_R_LIST.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def list_update(guid: uuid.UUID, name_ru: str):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            item = await session.get(M_R_LIST, guid)
            if item is None:
                content = {"msg": cfg.MSG_ERROR, "data": f"List with guid {guid} not found"}
                return content
            item.name_ru = name_ru
            await session.commit()
            await session.refresh(item)
            content = {"msg": cfg.MSG_OK, "count": 1, "data": item}
            return content
    except Exception as e:
        cont_err = f"fail. can't update record in table ({M_R_LIST.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def list_delete(guid: uuid.UUID):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            item = await session.get(M_R_LIST, guid)
            if item is None:
                content = {"msg": cfg.MSG_ERROR, "data": f"List with guid {guid} not found"}
                return content
            await session.delete(item)
            await session.commit()
            content = {"msg": cfg.MSG_OK, "count": 1, "data": f"List with guid {guid} deleted"}
            return content
    except Exception as e:
        cont_err = f"fail. can't delete record from table ({M_R_LIST.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content
