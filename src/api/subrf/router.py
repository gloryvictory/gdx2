import uuid
from fastapi import APIRouter
from src.api.subrf.services import subrf_get_all, subrf_get_all_count, subrf_get_by_id, \
    subrf_create, subrf_update, subrf_delete

subrf_router = APIRouter(prefix="/subrf", tags=["Субъекты РФ"])


#
@subrf_router.get(path='/all',
                  status_code=200,
                  name='Получить все субъекты РФ',
                  tags=['Субъекты РФ'],
                  description='Получает все субъекты РФ')
async def get_subrf_get_all():
    content = await subrf_get_all()
    return content


#
@subrf_router.get(path='/count',
                  status_code=200,
                  name='Получить количество субъектов РФ',
                  tags=['Субъекты РФ'],
                  description='Получает количество субъектов РФ')
async def get_subrf_get_all_count():
    content = await subrf_get_all_count()
    return content


#
@subrf_router.get(path='/{guid}',
                  status_code=200,
                  name='Получить субъект РФ по GUID',
                  tags=['Субъекты РФ'],
                  description='Получить субъект РФ по GUID')
async def get_subrf_by_id(guid: uuid.UUID):
    content = await subrf_get_by_id(guid)
    return content


#
@subrf_router.post(path='/',
                   status_code=201,
                   name='Создать субъект РФ',
                   tags=['Субъекты РФ'],
                   description='Создает новый субъект РФ')
async def post_subrf(name_ru: str):
    content = await subrf_create(name_ru)
    return content


#
@subrf_router.put(path='/{guid}',
                  status_code=200,
                  name='Обновить субъект РФ',
                  tags=['Субъекты РФ'],
                  description='Обновляет субъект РФ по GUID')
async def put_subrf(guid: uuid.UUID, name_ru: str):
    content = await subrf_update(guid, name_ru)
    return content


#
@subrf_router.delete(path='/{guid}',
                     status_code=200,
                     name='Удалить субъект РФ',
                     tags=['Субъекты РФ'],
                     description='Удаляет субъект РФ по GUID')
async def delete_subrf(guid: uuid.UUID):
    content = await subrf_delete(guid)
    return content
