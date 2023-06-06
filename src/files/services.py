from src.database import get_async_session
from src.files.folder2pg import folder2p
from src.models import FILE_M, FILE_SRC_M
from sqlalchemy import select


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
        cont_err = f"fail. can't read count from table ({FILE_M.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
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
        stmt = select(FILE_SRC_M).filter(FILE_SRC_M.folder_src == folder)
        # result = await session.execute(stmt)
        result = await session.execute(stmt)
        all_data = result.all()
        if len(all_data):
            print(f"Такой источник уже есть {folder}")
            content = {"msg": "error", "count": "0", "data": f"Такой источник уже есть {folder}"}
            print(content)
        else:
            new_src = FILE_SRC_M(folder_src=folder)
            session.add(new_src)
            await session.commit()
            folder2p(folder)
            all_count = 1
            content = {"msg": "Success", "count": all_count}
        return content
    except Exception as e:
        cont_err = f"fail. can't add to table ({FILE_M.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        pass
    return content


async def src_get_all(session):
    content = {"msg": f"Unknown error"}
    try:
        query = select(FILE_SRC_M)
        result = await session.execute(query)
        all_data = result.all()
        all_count = len(all_data)
        data_ = []
        for item in all_data:
            data_.append(item['FILE_SRC_M'])

        content = {
            "msg": "Success",
            "count": all_count,
            "data": data_
        }
        return content
    except Exception as e:
        cont_err = f"fail. can't read from table ({FILE_SRC_M.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        pass
    return content


async def src_get_by_id(_id: int, session):
    content = {"msg": f"Unknown error"}
    try:
        stmt = select(FILE_SRC_M).filter(FILE_SRC_M.id == _id)
        result = await session.execute(stmt)
        all_data = result.all()
        all_count = len(all_data)
        data_ = []
        for item in all_data:
            data_.append(item['FILE_SRC_M'])

        content = {
            "msg": "Success",
            "count": all_count,
            "data": data_
        }
        return content
    except Exception as e:
        cont_err = f" fail. can't read from table ({FILE_SRC_M.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        pass
    return content


