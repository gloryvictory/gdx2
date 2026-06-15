import uuid
from sqlalchemy import select, func
from src import cfg
from src.db.db import async_session_maker
# from src.log import set_logger
from src.models import M_R_ORG


async def org_get_all():
    content = {"msg": cfg.MSG_ERROR}
    # log = set_logger(cfg.AREA_FILE_LOG)

    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_R_ORG)
            )
            _all = res.all()
            cnt = len(_all)
            content = {"msg": cfg.MSG_OK, "count": cnt, "data": _all}
            # log.info("org load successfully")
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_R_ORG.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def org_get_all_count():
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            res = await session.scalar(select(func.count(M_R_ORG.guid)))
            content = {"msg": cfg.MSG_OK, "count": res}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_R_ORG.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def org_get_by_id(guid: uuid.UUID):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            res = await session.get(M_R_ORG, guid)
            content = {"msg": cfg.MSG_OK, "count": 1 if res else 0, "data": res}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_R_ORG.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def org_create(name_ru: str):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            new_org = M_R_ORG(name_ru=name_ru)
            session.add(new_org)
            await session.commit()
            await session.refresh(new_org)
            content = {"msg": cfg.MSG_OK, "count": 1, "data": new_org}
            return content
    except Exception as e:
        cont_err = f"fail. can't create record in table ({M_R_ORG.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def org_update(guid: uuid.UUID, name_ru: str):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            org = await session.get(M_R_ORG, guid)
            if org is None:
                content = {"msg": cfg.MSG_ERROR, "data": f"Org with guid {guid} not found"}
                return content
            org.name_ru = name_ru
            await session.commit()
            await session.refresh(org)
            content = {"msg": cfg.MSG_OK, "count": 1, "data": org}
            return content
    except Exception as e:
        cont_err = f"fail. can't update record in table ({M_R_ORG.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def org_delete(guid: uuid.UUID):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            org = await session.get(M_R_ORG, guid)
            if org is None:
                content = {"msg": cfg.MSG_ERROR, "data": f"Org with guid {guid} not found"}
                return content
            await session.delete(org)
            await session.commit()
            content = {"msg": cfg.MSG_OK, "count": 1, "data": f"Org with guid {guid} deleted"}
            return content
    except Exception as e:
        cont_err = f"fail. can't delete record from table ({M_R_ORG.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content
