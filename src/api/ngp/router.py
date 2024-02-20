from typing import List

from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.api.ngp.services import ngp_reload, ngp_get_all, ngp_get_all_count, ngp_get_geojson


ngp_router = APIRouter(prefix="/ngp", tags=["НГ Провинции"])


@ngp_router.get(path='/all',
                status_code=200,
                name='Получить список НГ Провинций',
                tags=['НГ Провинции'],
                description='Получает список НГ Провинций и координаты центров')
async def get_all():
    content = await ngp_get_all()
    return content


@ngp_router.get(path='/count',
                status_code=200,
                name='Получить количество НГ Провинций',
                tags=['НГ Провинции'],
                description='Получает количество НГ Провинций')
async def get_all_count():
    content = await ngp_get_all_count()
    return content


@ngp_router.get(path='/geojson',
                status_code=200,
                name='Получить файл в формате GeoJSON',
                tags=['НГ Провинции'],
                description='Получить файл в формате GeoJSON')
async def get_geojson():
    content_json = await ngp_get_geojson()
    return JSONResponse(content=content_json)


@ngp_router.get(path='/reload',
                status_code=200,
                name='Обновить список НГ Провинций',
                tags=['НГ Провинции'],
                description='Загружает список НГ Провинций и координаты центров из GeoJSON (файла или сервиса)')
async def get_ngp_reload():
    content_json = await ngp_reload()
    return content_json
