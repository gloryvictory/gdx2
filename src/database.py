# Базу создавать так
# CREATE ROLE gdx2 WITH LOGIN SUPERUSER PASSWORD 'gdx2pwd';
# CREATE USER gdx2 WITH ENCRYPTED PASSWORD 'gdx2pwd';
# ALTER USER gdx2 WITH SUPERUSER;
# CREATE DATABASE gdx2 WITH OWNER gdx2;
# GRANT ALL PRIVILEGES ON DATABASE gdx2 TO gdx2;
#
# \c gdx2;
# ALTER ROLE gdx2 SET client_encoding TO 'utf8';
# CREATE SCHEMA IF NOT EXISTS gdx2 AUTHORIZATION gdx2;
# SET search_path to gdx2;
# CREATE EXTENSION hstore;
# CREATE EXTENSION postgis;
# GRANT ALL ON SCHEMA gdx2 TO gdx2;
# Возможно пригодиться
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from src.cfg import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER, DB_SCHEMA, CONVENTION

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print(DATABASE_URL)

Base = declarative_base()

# Default naming convention for all indexes and constraints
# See why this is important and how it would save your time:
# https://alembic.sqlalchemy.org/en/latest/naming.html


# Registry for all tables
# metadata = MetaData()

metadata = MetaData(schema=DB_SCHEMA, naming_convention=CONVENTION)
engine = create_async_engine(DATABASE_URL, poolclass=NullPool, echo=True)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         try:
#             yield session
#         except Exception as e:
#             str_err = "Exception occurred " + str(e)
#             print(str_err)
#         # finally:
#         #     if session:
#         #         session.close()


@asynccontextmanager
async def get_async_session():
    session = async_session_maker()
    try:
        yield session
    except Exception as e:
        print(e)
        await session.rollback()
    finally:
        await session.close()


def pg_async_session(func):
    async def wrapper(*args, **kwargs):
        async with get_async_session() as session:
            return await func(session, *args, **kwargs)
    return wrapper
