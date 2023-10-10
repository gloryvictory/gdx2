from fastapi import APIRouter

from src.api.update.services import update_by_ngp

update_router = APIRouter(prefix="/update", tags=["Обновление таблицы с файлами координатами"])


@update_router.get(path='/ngp',
                status_code=200,
                name='Обновить по НГ Провинциям',
                tags=['Обновление таблицы с файлами координатами'],
                description='Обновить по НГ Провинциям')
async def get_update_by_ngp():
    content = await update_by_ngp()
    return content

