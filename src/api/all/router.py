from fastapi import APIRouter

from src.api.all.services import get_all_objects
from src.api.search.services import index_create, fulltext_search, fulltext_search_limit_offset

all_router = APIRouter(prefix="/all", tags=["Все объекты"])


@all_router.get(path='/objects',
                status_code=200,
                name='Все объекты',
                tags=['Все объекты'],
                description='Все объекты НГО, НГП, НГР, Месторождения, Площади, ЛУ, Скважины')
async def get_all():
    content = await get_all_objects()
    return content
