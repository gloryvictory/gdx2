import json
import os
import hashlib

import geopandas
from sqlalchemy import text, insert, select

from src import cfg
from src.db.db import async_session_maker
from src.log import set_logger
from src.models import M_NSI_NGR, M_FILE
from sqlalchemy.sql.expression import func

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

async def fulltext_search(search_str:str):
    content = {"msg": "Success"}
    str_query_local = search_str.strip().lower().replace(" ", "&")
    try:
        async with async_session_maker() as session:
            print(str_query_local)
            res = await session.scalars(select(M_FILE).where(
                M_FILE.file_path_fts.match(str_query_local, postgresql_regconfig='russian'))
            )
            _all = res.all()
            cnt = len(_all)
            content = {"msg": "Success", "count": cnt, "data": _all}
            # stmt = text(f"SELECT *\
            # FROM {M_FILE.__tablename__}\
            # WHERE {M_FILE.file_path_fts.key} @@ to_tsquery('{str_query_local}')\
            # ORDER BY ts_rank({M_FILE.file_path_fts.key}, plainto_tsquery('{str_query_local}'));")
            # # ORDER BY rank;
            # print(stmt)
            # res = await session.execute(stmt)
            # result = res.all()
            # _len = len(result)
            # print(result)
            # content = {"msg": "Success", "count": _len, "data": result}

    except Exception as e:
        content = {"msg": f"can't search in index {cfg.FILE_FTS_INDEX}"}
        print("Exception occurred " + str(e))
        return content
    finally:
        if session is not None:
            await session.close()
    return content

