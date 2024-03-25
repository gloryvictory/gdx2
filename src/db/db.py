from sqlalchemy import MetaData, NullPool
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.cfg import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER, DB_SCHEMA, CONVENTION

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print(DATABASE_URL)

metadata = MetaData(schema=DB_SCHEMA, naming_convention=CONVENTION)
engine = create_async_engine(DATABASE_URL, poolclass=NullPool, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_async_session():
    async with async_session_maker() as session:
        yield session


# @asynccontextmanager
# async def get_async_session():
#     session = async_session_maker()
#     try:
#         yield session
#     except Exception as e:
#         print(e)
#         await session.rollback()
#     finally:
#         await session.close()


def pg_async_session(func):
    async def wrapper(*args, **kwargs):
        async with get_async_session() as session:
            return await func(session, *args, **kwargs)
    return wrapper

