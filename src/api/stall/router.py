from fastapi import APIRouter
from src.api.stall.services import stall_get_all_method, stall_get_all_vid_iz, stall_get_all_god_nach

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