# TRUNCATE TABLE table_name RESTART IDENTITY; # чтобы сбросить сиквенсы
# alembic revision --autogenerate -m "Init"
# alembic upgrade head
# alembic downgrade base

import asyncio
import sys
from logging.config import fileConfig

import alembic
from alembic import context
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config


from src.cfg import DB_DSN
from src.db.db import Base

from src.models import M_FILE, M_EXT, M_NSI_FIELD, M_NSI_LU, M_NSI_NGO, M_NSI_NGP, M_NSI_NGR,M_NSI_AREA, M_NSI_WELL, M_REPORT_TGF


config = context.config
config.set_main_option("sqlalchemy.url", DB_DSN)
print(DB_DSN)
# DATABASE_URL = f"postgresql://gdx2:gdx2pwd@localhost:5432/gdx2"
# print(DATABASE_URL)
DATABASE_URL = DB_DSN

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata


# sys.path = ['', '..'] + sys.path[1:]
# from src.database import Base

target_metadata = Base.metadata



def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""

    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
