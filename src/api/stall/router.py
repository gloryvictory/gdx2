from fastapi import APIRouter
from src.api.stall.services import stall_get_all_method, stall_get_all_vid_iz, stall_get_all_god_nach, \
    stall_get_all_god_end, stall_get_all_tgf, stall_get_all_nom_1000, stall_get_all_org_isp, stall_get_all_scale

stall_router = APIRouter(prefix="/stall", tags=["Все отчеты карты"])


# Метод
@stall_router.get(path='/all/method/unique',
                status_code=200,
                name='Получить все уникальные методы для всех Отчетов',
                tags=['Все отчеты карты'],
                description='Получить все уникальные методы для всех Отчетов')
async def get_stall_get_all_method():
    content = await stall_get_all_method()
    return content

# Вид изученности
@stall_router.get(path='/all/vid_iz/unique',
                status_code=200,
                name='Получить все уникальные "Вид изученности" для всех Отчетов',
                tags=['Все отчеты карты'],
                description='Получить все уникальные "Вид изученности" для всех Отчетов')
async def get_stall_get_all_vid_iz():
    content = await stall_get_all_vid_iz()
    return content

# Год начала
@stall_router.get(path='/all/god_nach/unique',
                status_code=200,
                name='Получить все уникальные "Год начала" для всех Отчетов',
                tags=['Все отчеты карты'],
                description='Получить все уникальные "Год начала" для всех Отчетов')
async def get_stall_get_all_god_nach():
    content = await stall_get_all_god_nach()
    return content

@stall_router.get(path='/all/god_end/unique',
                status_code=200,
                name='Получить все уникальные "Год окончания" для всех Отчетов',
                tags=['Все отчеты карты'],
                description='Получить все уникальные "Год окончания" для всех Отчетов')
async def get_stall_get_all_god_end():
    content = await stall_get_all_god_end()
    return content

@stall_router.get(path='/all/tgf/unique',
                status_code=200,
                name='Получить все уникальные "ТГФ" для всех Отчетов',
                tags=['Все отчеты карты'],
                description='Получить все уникальные "ТГФ" для всех Отчетов')
async def get_stall_get_all_tgf():
    content = await stall_get_all_tgf()
    return content


@stall_router.get(path='/all/nom_1000/unique',
                status_code=200,
                name='Получить все уникальные "Лист" для всех Отчетов',
                tags=['Все отчеты карты'],
                description='Получить все уникальные "Лист" для всех Отчетов')
async def get_stall_get_all_nom_1000():
    content = await stall_get_all_nom_1000()
    return content


@stall_router.get(path='/all/org_isp/unique',
                status_code=200,
                name='Получить все уникальные "Организация" для всех Отчетов',
                tags=['Все отчеты карты'],
                description='Получить все уникальные "Организация" для всех Отчетов')
async def get_stall_get_all_org_isp():
    content = await stall_get_all_org_isp()
    return content


@stall_router.get(path='/all/scale/unique',
                status_code=200,
                name='Получить все уникальные "Масштаб" для всех Отчетов',
                tags=['Все отчеты карты'],
                description='Получить все уникальные "Масштаб" для всех Отчетов')
async def get_stall_get_all_scale():
    content = await stall_get_all_scale()
    return content

