import json
import os
import hashlib

import geopandas
from sqlalchemy import text, insert, select, func

from src import cfg
from src.db.db import async_session_maker
from src.log import set_logger
from src.models import M_NSI_NGR, M_FILE


# M_NSI_NGR
async def index_create():
    content = {"msg": "Success"}

    try:
        async with async_session_maker() as session:
            print(f"Удаляем индекс {cfg.FILE_FTS_INDEX}")
            stmt = text(f"DROP INDEX IF EXISTS {cfg.FILE_FTS_INDEX};")
            res = await session.execute(stmt)
            print(res)

            print(f"Создаем TSVector ...")
            stmt = text(f"UPDATE FILE SET {M_FILE.file_path_fts.key} = TO_TSVECTOR(COALESCE({M_FILE.f_path.key},''));")
            res = await session.execute(stmt)
            print(res)

            print(f"Создаем индекс ...")
            stmt = text(f"CREATE INDEX IF NOT EXISTS {cfg.FILE_FTS_INDEX} ON {M_FILE.__tablename__} USING GIN ({M_FILE.file_path_fts.key});")
            res = await session.execute(stmt)
            print(res)


        print("OK")
        content = {"msg": "Success", "count": 0}

    except Exception as e:
        content = {"msg": f"can't create index {cfg.FILE_FTS_INDEX}"}
        print("Exception occurred " + str(e))
        return content
    finally:
        if session is not None:
            await session.close()
    return content

