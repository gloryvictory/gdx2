from fastapi import APIRouter

from src.api.well.services import well_reload

well_router = APIRouter(prefix="/well", tags=["Скважины"])


# @well_router.get(path='/all',
#                  status_code=200,
#                  # response_model=List[s_well],
#                  name='Получить список скважин',
#                  tags=['Скважины'],
#                  description='Получает список Скважин и координаты')
# # @cache(expire=30)
# async def get_data():
#     content = await well_get_all()
#     return content
#
#
# @well_router.get(path='/count',
#                  status_code=200,
#                  name='Получить количество Скважины',
#                  tags=['Скважины'],
#                  description='Получает количество Скважин')
# async def get_count():
#     content = await well_get_all_count()
#     return content


@well_router.get(path='/reload',
                 status_code=200,
                 name='Обновить список Скважин',
                 tags=['Скважины'],
                 description='Загружает список Скважин из GeoJSON (файла или сервиса)')
async def get_well_reload():
    content_json = await well_reload()
    return content_json

#
# @well_router.get(path="/{area}",
#                  status_code=200,
#                  response_model=List[s_well],
#                  name='Получить список скважин по запрашиваемой площади',
#                  tags=['Скважины'],
#                  description='Получает список Скважин и координаты  по конкретной площади'
#                  )
# async def get_by_area(area: str):
#     content = await well_get_by_area(area)
#     return content
#
#
# @well_router.get(path='/{area}/count',
#                  status_code=200,
#                  name='Получить кол-во Скважин по запрашиваемой Площади',
#                  tags=['Скважины'],
#                  description='Получает количество Скважинпо запрашиваемой Площади')
# async def get_by_area_count(area: str):
#     content = await well_get_area_count(area)
#     return content
#
#
# @well_router.get(path='/geojson',
#                  status_code=200,
#                  name='Получить файл в формате GeoJSON',
#                  tags=['Скважины'],
#                  description='Получить файл в формате GeoJSON')
# async def get_geojson():
#     content_json = await well_get_geojson_file()
#     return JSONResponse(content=content_json)
