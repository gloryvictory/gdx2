from datetime import datetime

from celery import Celery
from sqlalchemy import update

from src import cfg
from src.db.db import async_session_maker
from src.log import set_logger
from src.models import M_FILE

celery = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')
# celery = Celery('tasks', broker=cfg.REDIS_URL)


# запуск celery
# celery -A src.api.celery.tasks:celery worker --loglevel=INFO --pool=solo
# запуск flower
# celery -A src.api.celery.tasks:celery flower


@celery.task(serializer='pickle')
async def update_file_by_ngp_str(ngp_str: str, lat: float, lon: float, f_path_md5: str):
    try:
        async with async_session_maker() as session:
            time1 = datetime.now()
            log = set_logger(cfg.NGP_FILE_LOG)
            log.INFO(f"Обработка: {ngp_str}")

            # print(file.f_path)
            # f_path_md5 = f_path_md5
            stmt = (
                update(M_FILE)
                .where(M_FILE.f_path_md5 == f_path_md5)
                .values(ngp=ngp_str, lat=lat, lon=lon)
            )
            await session.execute(stmt)
            await session.commit()

            content = {"msg": "Success"}
            time2 = datetime.now()
            log.INFO(f"Обработано: {ngp_str}. Total time:  + {str(time2 - time1)}")
            return content
    except Exception as e:
        cont_err = f"fail. can't read or update data from table ({M_FILE.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content
