import uuid
from sqlalchemy import select, func
from src import cfg
from src.db.db import async_session_maker
# from src.log import set_logger
from src.models import M_R_AUTHOR


async def author_get_all():
    content = {"msg": cfg.MSG_ERROR}
    # log = set_logger(cfg.AREA_FILE_LOG)

    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_R_AUTHOR)
            )
            _all = res.all()
            cnt = len(_all)
            content = {"msg": cfg.MSG_OK, "count": cnt, "data": _all}
            # log.info("author load successfully")
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_R_AUTHOR.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def author_get_all_count():
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            res = await session.scalar(select(func.count(M_R_AUTHOR.guid)))
            content = {"msg": cfg.MSG_OK, "count": res}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_R_AUTHOR.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def author_get_by_id(guid: uuid.UUID):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            res = await session.get(M_R_AUTHOR, guid)
            content = {"msg": cfg.MSG_OK, "count": 1 if res else 0, "data": res}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_R_AUTHOR.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def author_create(name_ru: str):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            new_author = M_R_AUTHOR(name_ru=name_ru)
            session.add(new_author)
            await session.commit()
            await session.refresh(new_author)
            content = {"msg": cfg.MSG_OK, "count": 1, "data": new_author}
            return content
    except Exception as e:
        cont_err = f"fail. can't create record in table ({M_R_AUTHOR.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def author_update(guid: uuid.UUID, name_ru: str):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            author = await session.get(M_R_AUTHOR, guid)
            if author is None:
                content = {"msg": cfg.MSG_ERROR, "data": f"Author with guid {guid} not found"}
                return content
            author.name_ru = name_ru
            await session.commit()
            await session.refresh(author)
            content = {"msg": cfg.MSG_OK, "count": 1, "data": author}
            return content
    except Exception as e:
        cont_err = f"fail. can't update record in table ({M_R_AUTHOR.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def author_delete(guid: uuid.UUID):
    content = {"msg": cfg.MSG_ERROR}
    try:
        async with async_session_maker() as session:
            author = await session.get(M_R_AUTHOR, guid)
            if author is None:
                content = {"msg": cfg.MSG_ERROR, "data": f"Author with guid {guid} not found"}
                return content
            await session.delete(author)
            await session.commit()
            content = {"msg": cfg.MSG_OK, "count": 1, "data": f"Author with guid {guid} deleted"}
            return content
    except Exception as e:
        cont_err = f"fail. can't delete record from table ({M_R_AUTHOR.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content
