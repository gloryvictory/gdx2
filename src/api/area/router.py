import uuid
from fastapi import APIRouter
from src.api.area.services import area_get_all, area_get_all_count, area_get_by_id, \
    area_create, area_update, area_delete

area_router = APIRouter(prefix="/area", tags=["Площади"])


#
@area_router.get(path='/all',
                 status_code=200,
                 name='Получить все площади',
                 tags=['Площади'],
                 description='Получает все площади')
async def get_area_get_all():
    content = await area_get_all()
    return content


#
@area_router.get(path='/count',
                 status_code=200,
                 name='Получить количество площадей',
                 tags=['Площади'],
                 description='Получает количество площадей')
async def get_area_get_all_count():
    content = await area_get_all_count()
    return content


#
@area_router.get(path='/{guid}',
                 status_code=200,
                 name='Получить площадь по GUID',
                 tags=['Площади'],
                 description='Получить площадь по GUID')
async def get_area_by_id(guid: uuid.UUID):
    content = await area_get_by_id(guid)
    return content


#
@area_router.post(path='/',
                  status_code=201,
                  name='Создать площадь',
                  tags=['Площади'],
                  description='Создает новую площадь')
async def post_area(name_ru: str):
    content = await area_create(name_ru)
    return content


#
@area_router.put(path='/{guid}',
                 status_code=200,
                 name='Обновить площадь',
                 tags=['Площади'],
                 description='Обновляет площадь по GUID')
async def put_area(guid: uuid.UUID, name_ru: str):
    content = await area_update(guid, name_ru)
    return content


#
@area_router.delete(path='/{guid}',
                    status_code=200,
                    name='Удалить площадь',
                    tags=['Площади'],
                    description='Удаляет площадь по GUID')
async def delete_area(guid: uuid.UUID):
    content = await area_delete(guid)
    return content
