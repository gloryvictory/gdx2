import uuid
from fastapi import APIRouter
from src.api.vid_rab.services import vid_rab_get_all, vid_rab_get_all_count, vid_rab_get_by_id, \
    vid_rab_create, vid_rab_update, vid_rab_delete

vid_rab_router = APIRouter(prefix="/vid_rab", tags=["Виды работ"])


#
@vid_rab_router.get(path='/all',
                    status_code=200,
                    name='Получить все виды работ',
                    tags=['Виды работ'],
                    description='Получает все виды работ')
async def get_vid_rab_get_all():
    content = await vid_rab_get_all()
    return content


#
@vid_rab_router.get(path='/count',
                    status_code=200,
                    name='Получить количество видов работ',
                    tags=['Виды работ'],
                    description='Получает количество видов работ')
async def get_vid_rab_get_all_count():
    content = await vid_rab_get_all_count()
    return content


#
@vid_rab_router.get(path='/{guid}',
                    status_code=200,
                    name='Получить вид работ по GUID',
                    tags=['Виды работ'],
                    description='Получить вид работ по GUID')
async def get_vid_rab_by_id(guid: uuid.UUID):
    content = await vid_rab_get_by_id(guid)
    return content


#
@vid_rab_router.post(path='/',
                     status_code=201,
                     name='Создать вид работ',
                     tags=['Виды работ'],
                     description='Создает новый вид работ')
async def post_vid_rab(name_ru: str):
    content = await vid_rab_create(name_ru)
    return content


#
@vid_rab_router.put(path='/{guid}',
                    status_code=200,
                    name='Обновить вид работ',
                    tags=['Виды работ'],
                    description='Обновляет вид работ по GUID')
async def put_vid_rab(guid: uuid.UUID, name_ru: str):
    content = await vid_rab_update(guid, name_ru)
    return content


#
@vid_rab_router.delete(path='/{guid}',
                       status_code=200,
                       name='Удалить вид работ',
                       tags=['Виды работ'],
                       description='Удаляет вид работ по GUID')
async def delete_vid_rab(guid: uuid.UUID):
    content = await vid_rab_delete(guid)
    return content
