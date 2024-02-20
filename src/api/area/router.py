from fastapi import APIRouter

from src.api.area.services import area_reload, area_get_all, area_get_all_count, area_get_geojson_file

area_router = APIRouter(prefix="/area", tags=["Площади"])

#
@area_router.get(path='/all',
                 status_code=200,
                 name='Получить список Площадей',
                 tags=['Площади'],
                 description='Получает список Площадей и координаты центров')
async def get_area_get_all():
    content = await area_get_all()
    return content
#
#
#
@area_router.get(path='/count',
                 status_code=200,
                 name='Получить количество Площадей',
                 tags=['Площади'],
                 description='Получает количество Площадей')
async def get_area_get_all_count():
    content = await area_get_all_count()
    return content
#
#

@area_router.get(path='/reload',
                 status_code=200,
                 name='Обновить список Площадей',
                 tags=['Площади'],
                 description='Загружает список Площадей из GeoJSON скважин (файла или сервиса)')
async def get_area_reload():
    # return JSONResponse(content={"msg": "area"})
    content_json =  await area_reload()
    return content_json


@area_router.get(path='/geojson',
                   status_code=200,
                   name='Получить файл в формате GeoJSON',
                   tags=['Площади'],
                   description='Получить файл в формате GeoJSON')
async def get_area_geojson():
    content_json = await area_get_geojson_file()
    return content_json
