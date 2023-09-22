import json
import os
import hashlib

import geopandas
from sqlalchemy import text, insert, select, func

from src import cfg
from src.db.db import async_session_maker
from src.log import set_logger
from src.models import M_NSI_AREA


async def area_reload():
    content = {"msg": "Fail"}
    file_geojson = os.path.join(cfg.FOLDER_BASE, cfg.FOLDER_DATA, cfg.WELL_FILE_GEOJSON_IN)
    file_geojson_out = os.path.join(cfg.FOLDER_BASE, cfg.FOLDER_GEOJSON_OUT, cfg.AREA_FILE_GEOJSON_OUT)

    name_area = cfg.WELL_NAME_AREA_FIELD
    crs_out = cfg.CRS_OUT

    try:
        gdf = geopandas.read_file(file_geojson, driver="GeoJSON")
        log = set_logger(cfg.WELL_FILE_LOG)

        # gdf_area1 = gdf[name_area].unique() # получаем уникальные
        gdf_area1 = gdf.dissolve(by=name_area, as_index=False)
        gdf_area1 = gdf_area1.to_crs(crs=crs_out)
        gdf_area1 = gdf_area1.sort_values(by=name_area, ascending=True)

        for i in range(0, len(gdf_area1)):
            gdf_area1.loc[i, 'lon'] = gdf_area1.geometry.centroid.x.iloc[i]
            gdf_area1.loc[i, 'lat'] = gdf_area1.geometry.centroid.y.iloc[i]

        # gdf_area = sorted(gdf_area1) # Сортируем
        gdf_area1.to_file(file_geojson_out, driver='GeoJSON')

        async with async_session_maker() as session:
            stmt = text(f"TRUNCATE {M_NSI_AREA.__tablename__} RESTART IDENTITY;")
            await session.execute(stmt)

            cnt_all = len(gdf_area1)

            for i in range(0, cnt_all):
                print(f"{i}  of {cnt_all}")
                str_name = str(gdf_area1.loc[i, name_area]).lower()
                _name_ru = str_name
                hash_object = hashlib.md5(str_name.encode())
                hash_md5 = hash_object.hexdigest()
                _lon = gdf_area1.loc[i, 'lon']
                _lat = gdf_area1.loc[i, 'lat']
                _crs = crs_out
                _hash = hash_md5
                stmt = insert(M_NSI_AREA).values(
                    name_ru=_name_ru,
                    lon=_lon,
                    lat=_lat,
                    crs=_crs,
                    hash=_hash,
                    )
                await session.execute(stmt)
                await session.commit()
            count = await session.scalar(select(func.count(M_NSI_AREA.id)))
            content = {"msg": "Success", "count": count}
            log.info(f"Total area count {count}")
    except Exception as e:
        content = {"msg": f"reload fail. can't read file {file_geojson}"}
        print("Exception occurred " + str(e))

        # fastapi_logger.exception("update_user_password")
        return content
    return content


async def area_get_all():
    content = {"msg": f"error"}
    log = set_logger(cfg.AREA_FILE_LOG)

    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_NSI_AREA)
                .order_by(M_NSI_AREA.name_ru)
            )
            _all = res.all()
            cnt = len(_all)
            content = {"msg": "Success", "count": cnt, "data": _all}
            log.info("ngp load successfully")
            return content
    except Exception as e:
        cont_err = f"fail. can't read area from table ({M_NSI_AREA.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def area_get_all_count():
    content = {"msg": f"error"}
    try:
        async with async_session_maker() as session:
            res = await session.scalar(select(func.count(M_NSI_AREA.id)))
            content = {"msg": "Success", "count": res}
            return content
    except Exception as e:
        cont_err = f"fail. can't read ext from table ({M_NSI_AREA.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content

async def area_get_geojson_file():
    content = {"msg": "Success"}
    file_geojson_out = os.path.join(cfg.FOLDER_BASE, cfg.FOLDER_GEOJSON_OUT, cfg.AREA_FILE_GEOJSON_OUT)
    log = set_logger(cfg.AREA_FILE_LOG)
    log.info(f"Getting file {file_geojson_out}")
    try:
        with open(file_geojson_out, 'r', encoding="utf8") as fp:
            geojson_file = json.load(fp)
            return geojson_file

    except Exception as e:
        content = {"msg": f"reload fail. can't read file {file_geojson_out}"}
        str_err = "Exception occurred " + str(e)
        # print(str_err)
        log.info(str_err)
        return content
