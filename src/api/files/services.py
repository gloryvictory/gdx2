from sqlalchemy import select, func

from src.db.db import get_async_session, async_session_maker
# from src.cfg import DB_DSN_ASYNCIO
# from src.database import get_async_session
# from src.files.files2pg import folder2pg
# from src.models import FILE_M, FILE_SRC_M
from src.models import M_FILE


async def files_get_count():
    content = {"msg": f"Unknown error"}
    # log = set_logger(settings.WELL_FILE_LOG)
    try:
        async with async_session_maker() as session:
            res = await session.scalar(select(func.count(M_FILE.id)))
            content = {"msg": "Success", "count": res}
            session.close()
            return content
    except Exception as e:
        cont_err = f"fail. can't read count from table ({M_FILE.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        pass
        # if session is not None:
        #     session.close()
    return content


async def files_get_all():
    content = {"msg": f"Unknown error"}
    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_FILE)
            )
            _all = res.all()
            cnt = len(_all)
            # ss = []
            # for row in res.all():
            #     ss.append(row[0].to_read_model())
            # res2 = [row.to_read_model() for row in res.all()]

            content = {"msg": "Success", "count": cnt, "data": _all}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_FILE.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def files_get_all_limit_offset(limit: int = 100, offset: int = 0):
    content = {"msg": f"Unknown error"}
    # log = set_logger(settings.WELL_FILE_LOG)
    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_FILE)
                .limit(limit)
                .offset(offset)
            )
            _all = res.all()
            cnt = len(_all)
            content = {"msg": "Success", "count": cnt, "data": _all}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_FILE.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def files_get_by_id(_id: int = 0):
    content = {"msg": f"Unknown error"}
    try:
        async with async_session_maker() as session:
            res = await session.get(M_FILE, _id)
            _all = res
            content = {"msg": "Success", "count": 1, "data": _all}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_FILE.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
        #     session.close()
    return content


async def src_get_all():
    content = {"msg": f"Unknown error"}
    try:
        async with async_session_maker() as session:
            # stmt = (
            #     select(M_FILE.f_root)
            #     .distinct()
            #     .order_by(M_FILE.f_root)
            # )
            # result = session.execute(stmt).columns(M_FILE.f_root).all()
            res = await session.scalars(
                select(M_FILE.f_root)
                .distinct()
                .order_by(M_FILE.f_root)
            )
            _all = res.all()
            cnt = len(_all)
            content = {"msg": "Success", "count": cnt, "data": _all}
            return content
    except Exception as e:
        cont_err = f"fail. can't read table ({M_FILE.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
        #     session.close()
    return content

#
# async def src_add(folder, session):
#     content = {"msg": f"Unknown error"}
#     # log = set_logger(settings.WELL_FILE_LOG)
#     try:
#         print(folder)
#         stmt = select(FILE_SRC_M).filter(FILE_SRC_M.folder_src == folder)
#         # result = await session.execute(stmt)
#         result = await session.execute(stmt)
#         all_data = result.all()
#         if len(all_data):
#             print(f"Такой источник уже есть {folder}")
#             content = {"msg": "error", "count": "0", "data": f"Такой источник уже есть {folder}"}
#             print(content)
#         else:
#             new_src = FILE_SRC_M(folder_src=folder)
#             session.add(new_src)
#             await session.commit()
#
#             # folder2p(folder)
#             await folder2pg(folder, DB_DSN_ASYNCIO)
#
#             all_count = 1
#             content = {"msg": "Success", "count": all_count}
#         return content
#     except Exception as e:
#         cont_err = f"fail. can't add to table ({FILE_M.__tablename__})"
#         content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
#         print(content)
#     finally:
#         pass
#     return content
#
#
# async def src_get_all(session):
#     content = {"msg": f"Unknown error"}
#     try:
#         query = select(FILE_SRC_M)
#         result = await session.execute(query)
#         all_data = result.all()
#         all_count = len(all_data)
#         data_ = []
#         for item in all_data:
#             data_.append(item['FILE_SRC_M'])
#
#         content = {
#             "msg": "Success",
#             "count": all_count,
#             "data": data_
#         }
#         return content
#     except Exception as e:
#         cont_err = f"fail. can't read from table ({FILE_SRC_M.__tablename__})"
#         content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
#         print(content)
#     finally:
#         pass
#     return content
#
#
# async def src_get_by_id(_id: int, session):
#     content = {"msg": f"Unknown error"}
#     try:
#         stmt = select(FILE_SRC_M).filter(FILE_SRC_M.id == _id)
#         result = await session.execute(stmt)
#         all_data = result.all()
#         all_count = len(all_data)
#         data_ = []
#         for item in all_data:
#             data_.append(item['FILE_SRC_M'])
#
#         content = {
#             "msg": "Success",
#             "count": all_count,
#             "data": data_
#         }
#         return content
#     except Exception as e:
#         cont_err = f" fail. can't read from table ({FILE_SRC_M.__tablename__})"
#         content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
#         print(content)
#     finally:
#         pass
#     return content


# async def fetch_all(db: AsyncSession, skip: int = 0, limit: int = 20):
#     result = await db.execute(select(Task).order_by(Task.time.desc()).limit(20))
#     return result.scalars().all()
