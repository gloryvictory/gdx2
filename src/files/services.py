from src.database import get_async_session
from src.models import FILE_M, FILE_SRC_M


async def files_get_all_count():
    content = {"msg": f"Unknown error"}
    # log = set_logger(settings.WELL_FILE_LOG)
    try:
        async with get_async_session() as session:
            all_count = await session.query(FILE_M).count()
            content = {"msg": "Success", "count": all_count}
            session.close()
            return content
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"reload fail. can't read count from table ({FILE_M.__tablename__})", "err": str(e)}
        print(str_err)
        # log.info(str_err)
    finally:
        pass
        # if session is not None:
        #     session.close()
    return content


async def src_add(folder, session):
    content = {"msg": f"Unknown error"}
    # log = set_logger(settings.WELL_FILE_LOG)
    try:
        print(folder)
        new_src = FILE_SRC_M(folder_src=folder)
        session.add(new_src)
        await session.commit()

        all_count = 1
        content = {"msg": "Success", "count": all_count}
        return content
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"reload fail. can't read count from table ({FILE_M.__tablename__})", "err": str(e)}
        print(str_err)
    finally:
        pass
        # if session is not None:
        #     session.close()
    return content
