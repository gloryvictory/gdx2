import json
import os
import hashlib
from typing import Any

import geopandas
from sqlalchemy import text, insert, select, func

from src import cfg
from src.db.db import async_session_maker
from src.log import set_logger
from src.models import M_NSI_WELL


async def well_reload():
    content = {"msg": "Fail"}
    file_geojson = os.path.join(cfg.FOLDER_BASE, cfg.FOLDER_DATA, cfg.WELL_FILE_GEOJSON_IN)
    file_geojson_out = os.path.join(cfg.FOLDER_BASE, cfg.FOLDER_GEOJSON_OUT, cfg.WELL_FILE_GEOJSON_OUT)
    name_well = cfg.WELL_NAME_FIELD  # 'name_ru'
    name_area = cfg.WELL_NAME_AREA_FIELD
    crs_out = cfg.CRS_OUT

    try:
        gdf = geopandas.read_file(file_geojson, driver="GeoJSON")
        gdf1 = gdf.to_crs(crs=crs_out)
        gdf1.to_file(file_geojson_out, driver='GeoJSON')

        log = set_logger(cfg.WELL_FILE_LOG)

        log.info(gdf1)

        cnt_all = len(gdf1)

        cnt_areas = len(gdf1['pl'].unique())
        print(f"Count of AREAS : {cnt_areas}")

        async with async_session_maker() as session:
            # await M_NSI_NGP.objects.delete(each=True)
            stmt = text(f"TRUNCATE {M_NSI_WELL.__tablename__} RESTART IDENTITY;")
            await session.execute(stmt)

            for i in range(0, cnt_all):
                print(f"{i}  of {cnt_all}")

                str_name = str(gdf1.loc[i, name_well]).lower()
                str_name_area = str(gdf1.loc[i, name_area]).lower()
                _name_ru = str_name

                str_name_well_uniq = str(str_name_area + " " + str_name).lower().encode() # Получаем уникальное сочетание Площадь + №скважины
                hash_object = hashlib.md5(str_name_well_uniq)
                hash_md5 = hash_object.hexdigest()

                _lon = gdf1.geometry.x.iloc[i]
                _lat = gdf1.geometry.y.iloc[i]
                _crs = crs_out
                _hash = hash_md5

                stmt = insert(M_NSI_WELL).values(
                    name_ru=str_name,
                    lon=_lon,
                    lat=_lat,
                    crs=crs_out,
                    hash=hash_md5,
                    area=str_name_area)
                await session.execute(stmt)
                await session.commit()
            count = await session.scalar(select(func.count(M_NSI_WELL.id)))
            content = {"msg": "Success", "count": count}
            log.info(f"well {str_name}, pl: {str_name_area}")
    except Exception as e:
        content = {"msg": f"reload fail. can't read file {file_geojson}"}
        print("Exception occurred " + str(e))
        return content
    finally:
        if session is not None:
            await session.close()
    return content



async def well_get_all():
    content = {"msg": f"error"}
    log = set_logger(cfg.WELL_FILE_LOG)
    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_NSI_WELL)
                .order_by(M_NSI_WELL.name_ru)
            )
            _all = res.all()
            cnt = len(_all)
            content = {"msg": "Success", "count": cnt, "data": _all}
            log.info("ngp load successfully")
            return content
    except Exception as e:
        cont_err = f"fail. can't read well from table ({M_NSI_WELL.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def well_get_all_count():
    content = {"msg": f"error"}
    try:
        async with async_session_maker() as session:
            res = await session.scalar(select(func.count(M_NSI_WELL.id)))
            content = {"msg": "Success", "count": res}
            return content
    except Exception as e:
        cont_err = f"fail. can't read ext from table ({M_NSI_WELL.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content

async def well_get_geojson_file():
    content = {"msg": "Success"}
    file_geojson_out = os.path.join(cfg.FOLDER_BASE, cfg.FOLDER_GEOJSON_OUT, cfg.WELL_FILE_GEOJSON_OUT)
    log = set_logger(cfg.WELL_FILE_LOG)
    log.info(f"Getting file {file_geojson_out}")
    try:
        with open(file_geojson_out, 'r', encoding="utf8") as fp:
            geojson_file = json.load(fp)
            return geojson_file

    except Exception as e:
        content = {"msg": f"reload fail. can't read file {file_geojson_out}"}
        str_err = "Exception occurred " + str(e)
        log.info(str_err)
        return content
#
#
async def well_get_by_area(area: str):
    content = {"msg": f"error"}
    log = set_logger(cfg.WELL_FILE_LOG)
    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_NSI_WELL)
                .where(M_NSI_WELL.area==area)
                .order_by(M_NSI_WELL.name_ru)
            )
            _all = res.all()
            cnt = len(_all)
            content = {"msg": "Success", "count": cnt, "data": _all}
            log.info("ngp load successfully")
            return content
    except Exception as e:
        cont_err = f"fail. can't read well from table ({M_NSI_WELL.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content

async def well_get_area_count(area: str):
    content = {"msg": f"error"}
    try:
        async with async_session_maker() as session:
            # M_NSI_WELL.area == area
            res = await session.scalar(select(func.count(M_NSI_WELL.id)).where(M_NSI_WELL.area==area))
            content = {"msg": "Success", "count": res}
            return content
    except Exception as e:
        cont_err = f"fail. can't read ext from table ({M_NSI_WELL.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content
#
#
# async def well_get_area_count(area: str):