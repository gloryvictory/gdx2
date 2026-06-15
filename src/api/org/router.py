import uuid
from fastapi import APIRouter
from src.api.org.services import org_get_all, org_get_all_count, org_get_by_id, \
    org_create, org_update, org_delete

org_router = APIRouter(prefix="/org", tags=["Организации"])


#
@org_router.get(path='/all',
                status_code=200,
                name='Получить все организации',
                tags=['Организации'],
                description='Получает все организации')
async def get_org_get_all():
    content = await org_get_all()
    return content


#
@org_router.get(path='/count',
                status_code=200,
                name='Получить количество организаций',
                tags=['Организации'],
                description='Получает количество организаций')
async def get_org_get_all_count():
    content = await org_get_all_count()
    return content


#
@org_router.get(path='/{guid}',
                status_code=200,
                name='Получить организацию по GUID',
                tags=['Организации'],
                description='Получить организацию по GUID')
async def get_org_by_id(guid: uuid.UUID):
    content = await org_get_by_id(guid)
    return content


#
@org_router.post(path='/',
                 status_code=201,
                 name='Создать организацию',
                 tags=['Организации'],
                 description='Создает новую организацию')
async def post_org(name_ru: str):
    content = await org_create(name_ru)
    return content


#
@org_router.put(path='/{guid}',
                status_code=200,
                name='Обновить организацию',
                tags=['Организации'],
                description='Обновляет организацию по GUID')
async def put_org(guid: uuid.UUID, name_ru: str):
    content = await org_update(guid, name_ru)
    return content


#
@org_router.delete(path='/{guid}',
                   status_code=200,
                   name='Удалить организацию',
                   tags=['Организации'],
                   description='Удаляет организацию по GUID')
async def delete_org(guid: uuid.UUID):
    content = await org_delete(guid)
    return content
