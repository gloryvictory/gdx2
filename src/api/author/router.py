from fastapi import APIRouter

from src.api.author.services import author_get_all

author_router = APIRouter(prefix="/author", tags=["Авторы"])


@author_router.get(path='/all',
                   status_code=200,
                   name='Получить всех авторов',
                   tags=['Авторы'],
                   description='Получить всех авторов')
async def get_all():
    content = await author_get_all()
    return content
