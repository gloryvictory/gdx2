import json
import os
import hashlib
from typing import Any

import geopandas
from sqlalchemy import text, insert, select, func

from src import cfg
from src.db.db import async_session_maker
from src.log import set_logger
from src.models import M_NSI_LU


#TODO добавить номер лицензии


async def lu_reload():
    content = {"msg": "Success"}
    file_geojson = os.path.join(cfg.FOLDER_BASE, cfg.FOLDER_DATA, cfg.LU_FILE_GEOJSON_IN)
    file_geojson_out = os.path.join(cfg.FOLDER_BASE, cfg.FOLDER_GEOJSON_OUT, cfg.LU_FILE_GEOJSON_OUT)
    name_field = cfg.LU_NAME_FIELD  # 'name_ru'
    nom_lic = cfg.LU_NOM_LIC_FIELD # nom_lic
    crs_out = cfg.CRS_OUT

    try:
        gdf = geopandas.read_file(file_geojson, driver="GeoJSON")
        # MultiPolygon to Polygon
        gdf = gdf.explode(column='geometry', ignore_index=True, index_parts=False)
        # Объединяем два контура одного месторождения с одинаковым наименованием
        gdf = gdf.dissolve(by=name_field, as_index=False)

        gdf = gdf.to_crs(gdf.estimate_utm_crs())
        gdf['centroid'] = gdf.centroid



        gdf1 = gdf[[name_field, 'centroid', nom_lic]]
        gdf1.set_geometry("centroid")
        gdf1 = gdf1.rename(columns={'centroid': 'geom'}).set_geometry('geom')
        gdf1 = gdf1.to_crs(crs=crs_out)

        gdf1.to_file(file_geojson_out, driver='GeoJSON')

        cnt_gdf = len(gdf1)
        for i in range(0, len(gdf1)):
            gdf1.loc[i, 'lon'] = gdf1.geometry.centroid.x.iloc[i]
            gdf1.loc[i, 'lat'] = gdf1.geometry.centroid.y.iloc[i]
        log = set_logger(cfg.LU_FILE_LOG)

        log.info(gdf1)

        async with async_session_maker() as session:
            # await M_NSI_NGP.objects.delete(each=True)
            stmt = text(f"TRUNCATE {M_NSI_LU.__tablename__} RESTART IDENTITY;")
            await session.execute(stmt)

            for i in range(0, len(gdf1)):
                str_name = str(gdf1.loc[i, name_field]).lower()
                _name_ru = str_name
                str_nom_lic= str(gdf1.loc[i, nom_lic]).lower()

                hash_object = hashlib.md5(str_name.encode())
                hash_md5 = hash_object.hexdigest()
                _lon = gdf1.loc[i, 'lon']
                _lat = gdf1.loc[i, 'lat']
                _crs = crs_out
                _hash = hash_md5

                stmt = insert(M_NSI_LU).values(name_ru=_name_ru, lon=_lon, lat=_lat, crs=_crs, hash=_hash, nom_lic=str_nom_lic)
                await session.execute(stmt)
                await session.commit()
            count = await session.scalar(select(func.count(M_NSI_LU.id)))
            content = {"msg": "Success", "count": count}
            log.info(f"Total LU count {count}")
    except Exception as e:
        content = {"msg": f"reload fail. can't read file {file_geojson}"}
        print("Exception occurred " + str(e))

        # fastapi_logger.exception("update_user_password")
        return content
    finally:
        if session is not None:
            await session.close()
    return content



async def lu_get_all():
    content = {"msg": f"error"}
    log = set_logger(cfg.NGP_FILE_LOG)

    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_NSI_LU)
                .order_by(M_NSI_LU.name_ru)
            )
            _all = res.all()
            cnt = len(_all)
            content = {"msg": "Success", "count": cnt, "data": _all}
            log.info("ngp load successfully")
            return content
    except Exception as e:
        cont_err = f"fail. can't read ngp from table ({M_NSI_LU.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content



async def lu_get_all_count():
    content = {"msg": f"error"}
    try:
        async with async_session_maker() as session:
            res = await session.scalar(select(func.count(M_NSI_LU.id)))
            content = {"msg": "Success", "count": res}
            return content
    except Exception as e:
        cont_err = f"fail. can't read ext from table ({M_NSI_LU.__tablename__})"
        content = {"msg": "error", "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content
#
async def lu_get_geojson_file():
    content = {"msg": "Success"}
    file_geojson_out = os.path.join(cfg.FOLDER_BASE, cfg.FOLDER_GEOJSON_OUT, cfg.LU_FILE_GEOJSON_OUT)
    log = set_logger(cfg.LU_FILE_LOG)
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
