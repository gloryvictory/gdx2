import uuid
from fastapi import APIRouter
from src.api.list.services import list_get_all, list_get_all_count, list_get_by_id, \
    list_create, list_update, list_delete

list_router = APIRouter(prefix="/list", tags=["Листы карты"])


#
@list_router.get(path='/all',
                 status_code=200,
                 name='Получить все листы карты',
                 tags=['Листы карты'],
                 description='Получает все листы карты')
async def get_list_get_all():
    content = await list_get_all()
    return content


#
@list_router.get(path='/count',
                 status_code=200,
                 name='Получить количество листов карты',
                 tags=['Листы карты'],
                 description='Получает количество листов карты')
async def get_list_get_all_count():
    content = await list_get_all_count()
    return content


#
@list_router.get(path='/{guid}',
                 status_code=200,
                 name='Получить лист карты по GUID',
                 tags=['Листы карты'],
                 description='Получить лист карты по GUID')
async def get_list_by_id(guid: uuid.UUID):
    content = await list_get_by_id(guid)
    return content


#
@list_router.post(path='/',
                  status_code=201,
                  name='Создать лист карты',
                  tags=['Листы карты'],
                  description='Создает новый лист карты')
async def post_list(name_ru: str):
    content = await list_create(name_ru)
    return content


#
@list_router.put(path='/{guid}',
                 status_code=200,
                 name='Обновить лист карты',
                 tags=['Листы карты'],
                 description='Обновляет лист карты по GUID')
async def put_list(guid: uuid.UUID, name_ru: str):
    content = await list_update(guid, name_ru)
    return content


#
@list_router.delete(path='/{guid}',
                    status_code=200,
                    name='Удалить лист карты',
                    tags=['Листы карты'],
                    description='Удаляет лист карты по GUID')
async def delete_list(guid: uuid.UUID):
    content = await list_delete(guid)
    return content
