import uuid
from fastapi import APIRouter
from src.api.author.services import author_get_all, author_get_all_count, author_get_by_id, \
    author_create, author_update, author_delete

author_router = APIRouter(prefix="/author", tags=["Авторы"])


#
@author_router.get(path='/all',
                   status_code=200,
                   name='Получить всех авторов',
                   tags=['Авторы'],
                   description='Получает всех авторов')
async def get_author_get_all():
    content = await author_get_all()
    return content


#
@author_router.get(path='/count',
                   status_code=200,
                   name='Получить количество авторов',
                   tags=['Авторы'],
                   description='Получает количество авторов')
async def get_author_get_all_count():
    content = await author_get_all_count()
    return content


#
@author_router.get(path='/{guid}',
                   status_code=200,
                   name='Получить автора по GUID',
                   tags=['Авторы'],
                   description='Получить автора по GUID')
async def get_author_by_id(guid: uuid.UUID):
    content = await author_get_by_id(guid)
    return content


#
@author_router.post(path='/',
                    status_code=201,
                    name='Создать автора',
                    tags=['Авторы'],
                    description='Создает нового автора')
async def post_author(name_ru: str):
    content = await author_create(name_ru)
    return content


#
@author_router.put(path='/{guid}',
                   status_code=200,
                   name='Обновить автора',
                   tags=['Авторы'],
                   description='Обновляет автора по GUID')
async def put_author(guid: uuid.UUID, name_ru: str):
    content = await author_update(guid, name_ru)
    return content


#
@author_router.delete(path='/{guid}',
                      status_code=200,
                      name='Удалить автора',
                      tags=['Авторы'],
                      description='Удаляет автора по GUID')
async def delete_author(guid: uuid.UUID):
    content = await author_delete(guid)
    return content
