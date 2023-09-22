from fastapi import APIRouter

from src.api.search.services import index_create

search_router = APIRouter(prefix="/search", tags=["Поиск"])


@search_router.get(path='/index/create',
                status_code=200,
                # response_model=List[s_ngr],
                name='Создать индекс',
                tags=['Поиск'],
                description='Создать индекс')
async def get_index_create():
    content = await index_create()
    return content

