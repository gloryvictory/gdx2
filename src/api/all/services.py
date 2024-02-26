from sqlalchemy import text, insert, select, func
from src.db.db import async_session_maker
from src.models import M_NSI_AREA, M_NSI_NGP, M_NSI_NGO, M_NSI_NGR, M_NSI_FIELD, M_NSI_LU


async def get_all_objects():
    content = {"msg": "Fail"}
    all_data = []
    cnt = 0
    try:

        content = {"msg": "Success", "count": 111111}
        async with async_session_maker() as session:
            #  НГП
            res = await session.scalars(
                select(M_NSI_NGP)
                .order_by(M_NSI_NGP.name_ru)
            )
            _all = res.all()
            for current in _all:
                _current = {
                    "name_ru": current.name_ru,
                    "obj": "НГП",
                    "len": len(current.name_ru),
                    "lat": current.lat,
                    "lon": current.lon,
                }
                all_data.append(_current)

            _cnt = len(all_data)
            # НГО
            res = await session.scalars(
                select(M_NSI_NGO)
                .order_by(M_NSI_NGO.name_ru)
            )
            _all = res.all()
            for current in _all:
                _current = {
                    "name_ru": current.name_ru,
                    "obj": "НГО",
                    "len": len(current.name_ru),
                    "lat": current.lat,
                    "lon": current.lon,
                }
                all_data.append(_current)
            # НГР
            res = await session.scalars(
                select(M_NSI_NGR)
                .order_by(M_NSI_NGR.name_ru)
            )
            _all = res.all()
            for current in _all:
                _current = {
                    "name_ru": current.name_ru,
                    "obj": "НГР",
                    "len": len(current.name_ru),
                    "lat": current.lat,
                    "lon": current.lon,
                }
                all_data.append(_current)
            # Месторождения
            res = await session.scalars(
                select(M_NSI_FIELD)
                .order_by(M_NSI_FIELD.name_ru)
            )
            _all = res.all()
            for current in _all:
                _current = {
                    "name_ru": current.name_ru,
                    "obj": "Месторождение",
                    "len": len(current.name_ru),
                    "lat": current.lat,
                    "lon": current.lon,
                }
                all_data.append(_current)
            # ЛУ
            res = await session.scalars(
                select(M_NSI_LU)
                .order_by(M_NSI_LU.name_ru)
            )
            _all = res.all()
            for current in _all:
                _current = {
                    "name_ru": current.name_ru,
                    "obj": "ЛУ",
                    "len": len(current.name_ru),
                    "lat": current.lat,
                    "lon": current.lon,
                }
                all_data.append(_current)
            # Площади
            res = await session.scalars(
                select(M_NSI_AREA)
                .order_by(M_NSI_AREA.name_ru)
            )
            _all = res.all()
            for current in _all:
                _current = {
                    "name_ru": current.name_ru,
                    "obj": "Площадь",
                    "len": len(current.name_ru),
                    "lat": current.lat,
                    "lon": current.lon,
                }
                all_data.append(_current)


            _cnt = len(all_data)
            cnt = cnt + _cnt
            content = {"msg": "Success", "count": cnt, "data": all_data}
            # log.info("ngp load successfully")
            return content
    except Exception as e:
        content = {"msg": f"reload fail. can't... "}
        print("Exception occurred " + str(e))

        # fastapi_logger.exception("update_user_password")
        return content
