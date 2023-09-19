from typing import List

from fastapi import APIRouter

from src.api.field.services import fields_reload, fields_get_all, fields_get_all_count, fields_get_geojson_file

fields_router = APIRouter(prefix="/field", tags=["Месторождения"])


@fields_router.get(path='/all',
                   status_code=200,
                   # response_model=List[s_field],
                   name='Получить список Месторождений',
                   tags=['Месторождения'],
                   description='Получает список месторождений и координаты центров')
async def get_fields_get_all():
    content = await fields_get_all()
    return content


@fields_router.get(path='/count',
                   status_code=200,
                   name='Получить количество Месторождений',
                   tags=['Месторождения'],
                   description='Получает количество месторождений')
async def get_fields_get_count():
    content = await fields_get_all_count()
    return content


@fields_router.get(path='/reload',
                   status_code=200,
                   name='Обновить список Месторождений',
                   tags=['Месторождения'],
                   description='Загружает список месторождений и координаты центров из GeoJSON (файла или сервиса)')
async def get_fields_reload():
    content_json = await fields_reload()
    return content_json


# #
@fields_router.get(path='/geojson',
                   status_code=200,
                   name='Получить файл в формате GeoJSON',
                   tags=['Месторождения'],
                   description='Получить файл в формате GeoJSON')
async def get_fields_get_geojson():
    # content_json = await fields_reload()
    content_json = await fields_get_geojson_file()
    return content_json
