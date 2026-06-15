import uuid
from fastapi import APIRouter
from src.api.field.services import field_get_all, field_get_all_count, field_get_by_id, \
    field_create, field_update, field_delete

field_router = APIRouter(prefix="/field", tags=["Месторождения"])


#
@field_router.get(path='/all',
                  status_code=200,
                  name='Получить все месторождения',
                  tags=['Месторождения'],
                  description='Получает все месторождения')
async def get_field_get_all():
    content = await field_get_all()
    return content


#
@field_router.get(path='/count',
                  status_code=200,
                  name='Получить количество месторождений',
                  tags=['Месторождения'],
                  description='Получает количество месторождений')
async def get_field_get_all_count():
    content = await field_get_all_count()
    return content


#
@field_router.get(path='/{guid}',
                  status_code=200,
                  name='Получить месторождение по GUID',
                  tags=['Месторождения'],
                  description='Получить месторождение по GUID')
async def get_field_by_id(guid: uuid.UUID):
    content = await field_get_by_id(guid)
    return content


#
@field_router.post(path='/',
                   status_code=201,
                   name='Создать месторождение',
                   tags=['Месторождения'],
                   description='Создает новое месторождение')
async def post_field(name_ru: str):
    content = await field_create(name_ru)
    return content


#
@field_router.put(path='/{guid}',
                  status_code=200,
                  name='Обновить месторождение',
                  tags=['Месторождения'],
                  description='Обновляет месторождение по GUID')
async def put_field(guid: uuid.UUID, name_ru: str):
    content = await field_update(guid, name_ru)
    return content


#
@field_router.delete(path='/{guid}',
                     status_code=200,
                     name='Удалить месторождение',
                     tags=['Месторождения'],
                     description='Удаляет месторождение по GUID')
async def delete_field(guid: uuid.UUID):
    content = await field_delete(guid)
    return content
