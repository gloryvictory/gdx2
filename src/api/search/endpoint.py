from fastapi import APIRouter

from src.api.search.services import index_create, fulltext_search, fulltext_search_limit_offset

search_router = APIRouter(prefix="/search", tags=["Поиск"])


@search_router.get(path='/index/create',
                status_code=200,
                # response_model=List[s_ngr],
                name='Создать Полнотекстовый индекс',
                tags=['Поиск'],
                description='Создать Полнотекстовый индекс')
async def get_index_create():
    content = await index_create()
    return content

@search_router.get(path='/{search_str}',
                status_code=200,
                # response_model=List[s_ngr],
                name='Полнотекстовый поиск',
                tags=['Поиск'],
                description='Полнотекстовый поиск')
async def get_fulltext_search(search_str):
    content = await fulltext_search(search_str)
    return content

@search_router.get(path='/{search_str}/{limit}/{offset}',
                  status_code=200,
                  name='Полнотекстовый поиск с указанием лимита и оффсета',
                  tags=['Файлы'],
                  description='Полнотекстовый поиск с указанием лимита и оффсета')
async def get_fulltext_search_limit_offset(search_str:str,  limit: int, offset: int):
    content = await fulltext_search_limit_offset(search_str, limit, offset)
    return content

