from fastapi import APIRouter

from src.api.update.services import update_by_ngp, update_by_ngo, update_by_ngr, update_by_area

update_router = APIRouter(prefix="/update", tags=["Обновление таблицы файлов координатами"])


@update_router.get(path='/ngp',
                status_code=200,
                name='Обновить координаты по НГ Провинциям',
                # tags=['Обновление таблицы файлов координатами'],
                description='Обновить координаты по НГ Провинциям')
async def get_update_by_ngp():
    content = await update_by_ngp()
    return content

@update_router.get(path='/ngo',
                status_code=200,
                name='Обновить координаты по НГ Областям',
                description='Обновить координаты по НГ Областям')
async def get_update_by_ngo():
    content = await update_by_ngo()
    return content

@update_router.get(path='/ngr',
                status_code=200,
                name='Обновить координаты по НГ Районам',
                description='Обновить координаты по НГ Районам')
async def get_update_by_ngr():
    content = await update_by_ngr()
    return content

@update_router.get(path='/area',
                status_code=200,
                name='Обновить координаты по Площадям',
                description='Обновить координаты по Площадям')
async def get_update_by_are():
    content = await update_by_area()
    return content
