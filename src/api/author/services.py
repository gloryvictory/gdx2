from sqlalchemy import select

from src.db.db import async_session_maker
from src.models import M_AUTHOR


async def author_get_all():
    content = {"msg": "Fail"}
    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_AUTHOR.author_name)
                .order_by(M_AUTHOR.author_name)
            )
            _all = res.all()
            _cnt = len(_all)
            content = {"msg": "Success", "count": _cnt, "data": _all}
        return content
    except Exception as e:
        content = {"msg": "Fail", "data": f"Can't get all from {M_AUTHOR.__tablename__}... "}
        print("Exception occurred " + str(e))
        # fastapi_logger.exception("update_user_password")
        return content
