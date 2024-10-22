from fastapi import APIRouter
from src.api.stp.services import stp_get_all, stp_get_all_count, stp_get_by_id, stp_get_by_rosg, stp_get_count_by_rosg

stp_router = APIRouter(prefix="/stp", tags=["Полигоны"])

#
@stp_router.get(path='/all',
                status_code=200,
                name='Получить все Отчеты - Полигоны',
                tags=['Полигоны'],
                description='Получает все Отчеты - Полигоны')
async def get_stp_get_all():
    content = await stp_get_all()
    return content
#
#
#
@stp_router.get(path='/count',
                status_code=200,
                name='Получить количество Отчетов',
                tags=['Полигоны'],
                description='Получает количество Отчетов')
async def get_stp_get_all_count():
    content = await stp_get_all_count()
    return content


#
@stp_router.get(path='/{id}',
                  status_code=200,
                  name='Получить Отчеты по ID',
                  tags=['Полигоны'],
                  description='Получить Отчеты по ID')
async def get_stp_by_id(id: int):
    content = await stp_get_by_id(id)
    return (content)



@stp_router.get(path='/rosg/{rosg}',
                  status_code=200,
                  name='Получить Отчеты по ROSG',
                  tags=['Полигоны'],
                  description='Получить Отчеты по ROSG')
async def get_stp_by_rosg(rosg: str):
    content = await stp_get_by_rosg(rosg)
    return content

@stp_router.get(path='/rosg/count/{rosg}',
                  status_code=200,
                  name='Получить кол-во Отчетов по ROSG',
                  tags=['Полигоны'],
                  description='Получить кол-во Отчетов по ROSG')
async def get_count_stp_by_rosg(rosg: str):
    content = await stp_get_count_by_rosg(rosg)
    return content