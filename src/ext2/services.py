from sqlalchemy import insert, func, select

from src.models import EXT_M

from src.database import pg_async_session, get_async_session


@pg_async_session
async def ext_get_all_count(pg_async_session):
    content = {"msg": f"Unknown error"}
    stmt = select(EXT_M).filter()
    result = await pg_async_session.execute(stmt)

    return len(result.scalars().all())

# async def ext_get_all_count():
#     async with get_async_session() as session:
#         content = {"msg": f"Unknown error"}
#         stmt = select(EXT_M).filter()
#         result = await session.execute(stmt)
#
#         return len(result.scalars().all())

