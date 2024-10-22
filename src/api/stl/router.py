from fastapi import APIRouter
from src.api.stl.services import stl_get_all, stl_get_all_count, stl_get_by_id, stl_get_by_rosg, stl_get_count_by_rosg

stl_router = APIRouter(prefix="/stl", tags=["Линии"])

#
@stl_router.get(path='/all',
                status_code=200,
                name='Получить все Отчеты - Линии',
                tags=['Линии'],
                description='Получает все Отчеты - Линии')
async def get_stl_get_all():
    content = await stl_get_all()
    return content
#
#
#
@stl_router.get(path='/count',
                status_code=200,
                name='Получить количество Отчетов',
                tags=['Линии'],
                description='Получает количество Отчетов')
async def get_stl_get_all_count():
    content = await stl_get_all_count()
    return content


#
@stl_router.get(path='/{id}',
                  status_code=200,
                  name='Получить Отчеты по ID',
                  tags=['Линии'],
                  description='Получить Отчеты по ID')
async def get_stl_by_id(id: int):
    content = await stl_get_by_id(id)
    return (content)



@stl_router.get(path='/rosg/{rosg}',
                  status_code=200,
                  name='Получить Отчеты по ROSG',
                  tags=['Линии'],
                  description='Получить Отчеты по ROSG')
async def get_stl_by_rosg(rosg: str):
    content = await stl_get_by_rosg(rosg)
    return content

@stl_router.get(path='/rosg/count/{rosg}',
                  status_code=200,
                  name='Получить кол-во Отчетов по ROSG',
                  tags=['Линии'],
                  description='Получить кол-во Отчетов по ROSG')
async def get_count_stl_by_rosg(rosg: str):
    content = await stl_get_count_by_rosg(rosg)
    return content