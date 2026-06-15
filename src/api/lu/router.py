import uuid
from fastapi import APIRouter
from src.api.lu.services import lu_get_all, lu_get_all_count, lu_get_by_id, \
    lu_create, lu_update, lu_delete

lu_router = APIRouter(prefix="/lu", tags=["Лицензионные участки"])


#
@lu_router.get(path='/all',
               status_code=200,
               name='Получить все лицензионные участки',
               tags=['Лицензионные участки'],
               description='Получает все лицензионные участки')
async def get_lu_get_all():
    content = await lu_get_all()
    return content


#
@lu_router.get(path='/count',
               status_code=200,
               name='Получить количество лицензионных участков',
               tags=['Лицензионные участки'],
               description='Получает количество лицензионных участков')
async def get_lu_get_all_count():
    content = await lu_get_all_count()
    return content


#
@lu_router.get(path='/{guid}',
               status_code=200,
               name='Получить лицензионный участок по GUID',
               tags=['Лицензионные участки'],
               description='Получить лицензионный участок по GUID')
async def get_lu_by_id(guid: uuid.UUID):
    content = await lu_get_by_id(guid)
    return content


#
@lu_router.post(path='/',
                status_code=201,
                name='Создать лицензионный участок',
                tags=['Лицензионные участки'],
                description='Создает новый лицензионный участок')
async def post_lu(name_ru: str):
    content = await lu_create(name_ru)
    return content


#
@lu_router.put(path='/{guid}',
               status_code=200,
               name='Обновить лицензионный участок',
               tags=['Лицензионные участки'],
               description='Обновляет лицензионный участок по GUID')
async def put_lu(guid: uuid.UUID, name_ru: str):
    content = await lu_update(guid, name_ru)
    return content


#
@lu_router.delete(path='/{guid}',
                  status_code=200,
                  name='Удалить лицензионный участок',
                  tags=['Лицензионные участки'],
                  description='Удаляет лицензионный участок по GUID')
async def delete_lu(guid: uuid.UUID):
    content = await lu_delete(guid)
    return content
