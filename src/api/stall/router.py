from fastapi import APIRouter
from src.api.stall.services import stall_get_all_method

stall_router = APIRouter(prefix="/stall", tags=["Все отчеты карты"])


#
@stall_router.get(path='/all/method/unique',
                status_code=200,
                name='Получить все уникальные методы для всех Отчетов',
                tags=['Все отчеты карты'],
                description='Получить все уникальные методы для всех Отчетов')
async def get_stall_get_all_method():
    content = await stall_get_all_method()
    return content