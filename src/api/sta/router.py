from fastapi import APIRouter
from src.api.sta.services import sta_get_all, sta_get_all_count, sta_get_by_id, sta_get_by_rosg, sta_get_count_by_rosg

sta_router = APIRouter(prefix="/sta", tags=["Точки"])

#
@sta_router.get(path='/all',
                status_code=200,
                name='Получить все Отчеты - Точки',
                tags=['Точки'],
                description='Получает все Отчеты - Точки')
async def get_sta_get_all():
    content = await sta_get_all()
    return content
#
#
#
@sta_router.get(path='/count',
                status_code=200,
                name='Получить количество Отчетов',
                tags=['Точки'],
                description='Получает количество Отчетов')
async def get_sta_get_all_count():
    content = await sta_get_all_count()
    return content


#
@sta_router.get(path='/{id}',
                  status_code=200,
                  name='Получить Отчеты по ID',
                  tags=['Точки'],
                  description='Получить Отчеты по ID')
async def get_sta_by_id(id: int):
    content = await sta_get_by_id(id)
    return (content)



@sta_router.get(path='/rosg/{rosg}',
                  status_code=200,
                  name='Получить Отчеты по ROSG',
                  tags=['Точки'],
                  description='Получить Отчеты по ROSG')
async def get_sta_by_rosg(rosg: str):
    content = await sta_get_by_rosg(rosg)
    return content

@sta_router.get(path='/rosg/count/{rosg}',
                  status_code=200,
                  name='Получить кол-во Отчетов по ROSG',
                  tags=['Точки'],
                  description='Получить кол-во Отчетов по ROSG')
async def get_count_sta_by_rosg(rosg: str):
    content = await sta_get_count_by_rosg(rosg)
    return content