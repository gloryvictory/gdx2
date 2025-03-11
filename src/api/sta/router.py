from fastapi import APIRouter
from src.api.sta.services import sta_get_all, sta_get_all_count, sta_get_by_id, sta_get_by_rosg, sta_get_count_by_rosg, \
    sta_get_all_method

sta_router = APIRouter(prefix="/sta", tags=["Полигоны"])

#
@sta_router.get(path='/all',
                status_code=200,
                name='Получить все Отчеты - Полигоны',
                tags=['Полигоны'],
                description='Получает все Отчеты - Полигоны')
async def get_sta_get_all():
    content = await sta_get_all()
    return content
#
#
#
@sta_router.get(path='/count',
                status_code=200,
                name='Получить количество Отчетов',
                tags=['Полигоны'],
                description='Получает количество Отчетов')
async def get_sta_get_all_count():
    content = await sta_get_all_count()
    return content


#
@sta_router.get(path='/{id}',
                  status_code=200,
                  name='Получить Отчеты по ID',
                  tags=['Полигоны'],
                  description='Получить Отчеты по ID')
async def get_sta_by_id(id: int):
    content = await sta_get_by_id(id)
    return (content)



@sta_router.get(path='/rosg/{rosg}',
                  status_code=200,
                  name='Получить Отчеты по ROSG',
                  tags=['Полигоны'],
                  description='Получить Отчеты по ROSG')
async def get_sta_by_rosg(rosg: str):
    content = await sta_get_by_rosg(rosg)
    return content

@sta_router.get(path='/rosg/count/{rosg}',
                  status_code=200,
                  name='Получить кол-во Отчетов по ROSG',
                  tags=['Полигоны'],
                  description='Получить кол-во Отчетов по ROSG')
async def get_count_sta_by_rosg(rosg: str):
    content = await sta_get_count_by_rosg(rosg)
    return content


@sta_router.get(path='/all/method/unique',
                status_code=200,
                name='Получить все уникальные методы для Отчеты - Полигоны',
                tags=['Полигоны'],
                description='Получает все Отчеты - Полигоны')
async def get_sta_get_all_method():
    content = await sta_get_all_method()
    return content