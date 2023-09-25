from fastapi import APIRouter

from src.api.search.services import index_create, fulltext_search

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

@search_router.get(path='/fulltext/{search_str}',
                status_code=200,
                # response_model=List[s_ngr],
                name='Полнотекстовый поиск',
                tags=['Поиск'],
                description='Полнотекстовый поиск')
async def get_fulltext_search(search_str):
    content = await fulltext_search(search_str)
    return content



