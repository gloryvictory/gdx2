import uuid
from fastapi import APIRouter
from src.api.pi.services import pi_get_all, pi_get_all_count, pi_get_by_id, \
    pi_create, pi_update, pi_delete

pi_router = APIRouter(prefix="/pi", tags=["Полезные ископаемые"])


#
@pi_router.get(path='/all',
               status_code=200,
               name='Получить все полезные ископаемые',
               tags=['Полезные ископаемые'],
               description='Получает все полезные ископаемые')
async def get_pi_get_all():
    content = await pi_get_all()
    return content


#
@pi_router.get(path='/count',
               status_code=200,
               name='Получить количество полезных ископаемых',
               tags=['Полезные ископаемые'],
               description='Получает количество полезных ископаемых')
async def get_pi_get_all_count():
    content = await pi_get_all_count()
    return content


#
@pi_router.get(path='/{guid}',
               status_code=200,
               name='Получить полезное ископаемое по GUID',
               tags=['Полезные ископаемые'],
               description='Получить полезное ископаемое по GUID')
async def get_pi_by_id(guid: uuid.UUID):
    content = await pi_get_by_id(guid)
    return content


#
@pi_router.post(path='/',
                status_code=201,
                name='Создать полезное ископаемое',
                tags=['Полезные ископаемые'],
                description='Создает новое полезное ископаемое')
async def post_pi(name_ru: str):
    content = await pi_create(name_ru)
    return content


#
@pi_router.put(path='/{guid}',
               status_code=200,
               name='Обновить полезное ископаемое',
               tags=['Полезные ископаемые'],
               description='Обновляет полезное ископаемое по GUID')
async def put_pi(guid: uuid.UUID, name_ru: str):
    content = await pi_update(guid, name_ru)
    return content


#
@pi_router.delete(path='/{guid}',
                  status_code=200,
                  name='Удалить полезное ископаемое',
                  tags=['Полезные ископаемые'],
                  description='Удаляет полезное ископаемое по GUID')
async def delete_pi(guid: uuid.UUID):
    content = await pi_delete(guid)
    return content
