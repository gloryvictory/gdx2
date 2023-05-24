import databases
import sqlalchemy
import ormar

from src import cfg
from src.log import set_logger


engine = sqlalchemy.create_engine(cfg.DB_DSN)
database = databases.Database(cfg.DB_DSN)
metadata = sqlalchemy.MetaData(schema=cfg.DB_SCHEMA)


async def db_get_connection():
    database_ = database
    # metadata.create_all(engine)
    if not database_.is_connected:
        print(f"connecting... {database_.url}")
        await database_.connect()
    return database_


def main():
    log = set_logger()
    print(cfg.DB_DSN)
    db_connect =  db_get_connection()
    print(f"connecting... {db_connect.__name__}")


if __name__ == "__main__":
    main()

import databases
import sqlalchemy



