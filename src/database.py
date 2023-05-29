# Базу создавать так
# CREATE USER nsi WITH ENCRYPTED PASSWORD 'nsipwd';
# CREATE DATABASE nsi WITH OWNER nsi;
# GRANT ALL PRIVILEGES ON DATABASE nsi TO nsi;
# \c nsi;
# CREATE SCHEMA IF NOT EXISTS nsi AUTHORIZATION nsi;
# SET search_path to nsi;

# Возможно пригодиться
# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO nsi;
# GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO nsi;
# GRANT ALL PRIVILEGES ON ALL FUNCTIONS  IN SCHEMA public TO nsi;

from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from src.cfg import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base = declarative_base()

metadata = MetaData()

engine = create_async_engine(DATABASE_URL, poolclass=NullPool)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            session.close()
