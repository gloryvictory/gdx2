from logging.config import fileConfig
from os import environ

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# sys.path.append('src/files')
import sys
import os
sys.path.append(os.path.join(sys.path[0], 'src'))

from src.database import metadata

sys.path = ['', '..'] + sys.path[1:]

# sys.path = ['', '..'] + sys.path[1:]
# # from src.models import FILE_M
# import src.models

# , FILE_SRC_M

# import os
# import sys
#
# cur_src = os.path.join(sys.path[0], 'src')
# sys.path.append(cur_src)
# print(f"cur: {cur_src}")
# olddir = os.getcwd()
# os.chdir('src')
# from src.files.models import FILE_M
#
# os.chdir(olddir)


# sys.path.insert(0, '../src')

# from src.models import BaseClass

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

section = config.config_ini_section
config.set_section_option(section, "DB_USER", environ.get("DB_USER"))
config.set_section_option(section, "DB_PASS", environ.get("DB_PASS"))
config.set_section_option(section, "DB_NAME", environ.get("DB_NAME"))
config.set_section_option(section, "DB_HOST", environ.get("DB_HOST"))
config.set_section_option(section, "DB_PORT", environ.get("DB_PORT"))

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s:%(DB_PORT)s/%(DB_NAME)s?async_fallback=True"
# print(f"postgresql+asyncpg://{environ.get('DB_USER')}:{environ.get('DB_PASS')}@{environ.get('DB_HOST')}:{environ.get('DB_PORT')}/{environ.get('DB_NAME')}")
print(SQLALCHEMY_DATABASE_URL) 

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = [metadata]


# print(f"metadata: {target_metadata}")
# , FILE_SRC_M.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


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


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    configuration['sqlalchemy.url'] = SQLALCHEMY_DATABASE_URL
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    # connectable = engine_from_config(
    #     config.get_section(config.config_ini_section, {}),
    #     prefix="sqlalchemy.",
    #     poolclass=pool.NullPool,
    # )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
