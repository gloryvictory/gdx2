from fastapi import APIRouter, UploadFile
from starlette.requests import Request

from src.api.report.services import (
    report_all_objects, report_upload_file, report_update, report_get_all_count,
    report_all_no_folder, report_all_rgf, report_all_tgf_hmao, report_all_tgf_ynao, report_all_tgf_kras,
    report_all_tgf_ekat, report_all_tgf_omsk, report_all_tgf_novo, report_all_tgf_tomsk, report_all_tgf_more,
    report_all_tgf_tmn, report_all_tgf_kurgan, report_all_tgf, report_all_year,
    report_report_by_author, report_get_all_by_year, report_all_by_rgf, report_all_by_tgf_hmao, report_all_by_tgf_ynao,
    report_all_by_tgf_kras, report_all_by_tgf_ekat, report_all_by_tgf_omsk, report_all_by_tgf_novo,
    report_all_by_tgf_tomsk, report_all_by_tgf_more, report_all_by_tgf_tmn, report_all_by_tgf_kurgan,
    report_get_author,
    report_get_list, report_get_subrf, report_get_org, report_get_area, report_get_field, report_get_lu, report_get_pi,
    report_get_vid_rab, report_get_model_author_count, report_get_model_list_count, report_get_model_subrf_count,
    report_get_model_org_count, report_get_model_area_count, report_get_model_field_count, report_get_model_lu_count,
    report_get_model_pi_count, report_get_model_vid_rab_count, report_get_author_by_id,
    report_fulltext_search, report_update_from_file_with_task, report_index_create, report_message_create,
    report_get_message
)
from src.schemas import S_R_MESSAGE, S_R_MESSAGE_POST

report_router = APIRouter(prefix="/report", tags=["Отчеты"])


@report_router.post(path="/upload/",
                    status_code=200,
                    name='Загрузить Excel файл',
                    tags=['Отчеты'],
                    description='Загрузить Excel файл')
async def upload_file(file: UploadFile):
    content = await report_upload_file(file)
    return content


@report_router.get(path='/update',
                   status_code=200,
                   name='Обновить из файла',
                   tags=['Отчеты'],
                   description='Обновить из файла')
async def get_update():
    content = await report_update()
    return content
#
# @report_router.get(path='/updatefromfile',
#                    status_code=200,
#                    name='Обновить все скопом из файла',
#                    tags=['Отчеты'],
#                    description='Обновить все скопом из файла')
# async def get_update_from_file():
#     content = await report_update_from_file()
#     return content


@report_router.get(path='/updatefromfiletask',
                   status_code=200,
                   name='Обновить все скопом из файла при помощи Celery',
                   tags=['Отчеты'],
                   description='Обновить все скопом из файла  при помощи Celery')
async def get_update_from_file_task():
    content = await report_update_from_file_with_task()
    return content


@report_router.get(path='/all',
                   status_code=200,
                   name='Получить все Отчеты',
                   tags=['Отчеты'],
                   description='Получить Все Отчеты')
async def get_all():
    content = await report_all_objects()
    return content


@report_router.get(path='/count',
                   status_code=200,
                   name='Получить количество вснх Отчетов',
                   tags=['Отчеты'],
                   description='Получить количество всех Отчетов')
async def get_all_count():
    content = await report_get_all_count()
    return content


@report_router.get(path='/all_no_folder',
                   status_code=200,
                   name='Отчеты без папки',
                   tags=['Отчеты'],
                   description='Все Отчеты без папки')
async def get_all_no_folder():
    content = await report_all_no_folder()
    return content


@report_router.get(path='/rgf/all',
                   status_code=200,
                   name='Отчеты только РГФ',
                   tags=['Отчеты'],
                   description='Отчеты только РГФ')
async def get_all_rgf():
    content = await report_all_rgf()
    return content


@report_router.get(path='/tgf_hmao/all',
                   status_code=200,
                   name='Отчеты только ХМТГФ',
                   tags=['Отчеты'],
                   description='Отчеты только ХМТГФ')
async def get_all_tgf_hmao():
    content = await report_all_tgf_hmao()
    return content


@report_router.get(path='/tgf_ynao/all',
                   status_code=200,
                   name='Отчеты только ЯНТГФ',
                   tags=['Отчеты'],
                   description='Отчеты только ЯНТГФ')
async def get_all_tgf_ynao():
    content = await report_all_tgf_ynao()
    return content


@report_router.get(path='/tgf_kras/all',
                   status_code=200,
                   name='Отчеты только КраснТГФ',
                   tags=['Отчеты'],
                   description='Отчеты только КраснТГФ')
async def get_all_tgf_kras():
    content = await report_all_tgf_kras()
    return content


@report_router.get(path='/tgf_ekat/all',
                   status_code=200,
                   name='Отчеты только ЕкатерТГФ',
                   tags=['Отчеты'],
                   description='Отчеты только ЕкатерТГФ')
async def get_all_tgf_ekat():
    content = await report_all_tgf_ekat()
    return content


@report_router.get(path='/tgf_omsk/all',
                   status_code=200,
                   name='Отчеты только ОмскТГФ',
                   tags=['Отчеты'],
                   description='Отчеты только ОмскТГФ')
async def get_all_tgf_omsk():
    content = await report_all_tgf_omsk()
    return content


@report_router.get(path='/tgf_novo/all',
                   status_code=200,
                   name='Отчеты только НовосибТГФ',
                   tags=['Отчеты'],
                   description='Отчеты только НовосибТГФ')
async def get_all_tgf_novo():
    content = await report_all_tgf_novo()
    return content


@report_router.get(path='/tgf_tomsk/all',
                   status_code=200,
                   name='Отчеты только ТомскТГФ',
                   tags=['Отчеты'],
                   description='Отчеты только ТомскТГФ')
async def get_all_tgf_tomsk():
    content = await report_all_tgf_tomsk()
    return content


@report_router.get(path='/tgf_more/all',
                   status_code=200,
                   name='Отчеты только МорскойТГФ',
                   tags=['Отчеты'],
                   description='Отчеты только МорскойТГФ')
async def get_all_tgf_more():
    content = await report_all_tgf_more()
    return content


@report_router.get(path='/tgf_tmn/all',
                   status_code=200,
                   name='Отчеты только ТюмТГФ',
                   tags=['Отчеты'],
                   description='Отчеты только ТюмТГФ')
async def get_all_tgf_tmn():
    content = await report_all_tgf_tmn()
    return content


@report_router.get(path='/tgf_kurgan/all',
                   status_code=200,
                   name='Отчеты только КурганТГФ',
                   tags=['Отчеты'],
                   description='Отчеты только КурганТГФ')
async def get_all_tgf_kurgan():
    content = await report_all_tgf_kurgan()
    return content


@report_router.get(path='/tgf/all',
                   status_code=200,
                   name='Отчеты только ТГФ',
                   tags=['Отчеты'],
                   description='Отчеты только ТГФ')
async def get_all_tgf():
    content = await report_all_tgf()
    return content


@report_router.get(path='/year/all',
                   status_code=200,
                   name='Отчеты только у которых есть год',
                   tags=['Отчеты'],
                   description='Отчеты только у которых есть год')
async def get_all_year():
    content = await report_all_year()
    return content


@report_router.get(path='/year/{year}',
                   status_code=200,
                   name='Отчеты только в год',
                   tags=['Отчеты'],
                   description='Отчеты только в год')
async def get_all_by_year(year: str):
    content = await report_get_all_by_year(year)
    return content


@report_router.get(path='/rgf/{rgf}',
                   status_code=200,
                   name='Отчеты РГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты РГФ по номеру')
async def get_all_by_rgf(rgf: str):
    content = await report_all_by_rgf(rgf)
    return content


@report_router.get(path='/tgf_hmao/{tgf_hmao}',
                   status_code=200,
                   name='Отчеты ХМТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты ХМТГФ по номеру')
async def get_all_by_tgf_hmao(tgf_hmao: str):
    content = await report_all_by_tgf_hmao(tgf_hmao)
    return content


@report_router.get(path='/tgf_ynao/{tgf_ynao}',
                   status_code=200,
                   name='Отчеты ЯНТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты ЯНТГФ по номеру')
async def get_all_by_tgf_ynao(tgf_ynao: str):
    content = await report_all_by_tgf_ynao(tgf_ynao)
    return content


@report_router.get(path='/tgf_kras/{tgf_kras}',
                   status_code=200,
                   name='Отчеты КраснТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты КраснТГФ по номеру')
async def get_all_by_tgf_kras(tgf_kras: str):
    content = await report_all_by_tgf_kras(tgf_kras)
    return content


@report_router.get(path='/tgf_ekat/{tgf_ekat}',
                   status_code=200,
                   name='Отчеты ЕкатерТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты ЕкатерТГФ по номеру')
async def get_all_by_tgf_ekat(tgf_ekat: str):
    content = await report_all_by_tgf_ekat(tgf_ekat)
    return content


@report_router.get(path='/tgf_omsk/{tgf_omsk}',
                   status_code=200,
                   name='Отчеты ОмскТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты ОмскТГФ по номеру')
async def get_all_by_tgf_omsk(tgf_omsk: str):
    content = await report_all_by_tgf_omsk(tgf_omsk)
    return content


@report_router.get(path='/tgf_novo/{tgf_novo}',
                   status_code=200,
                   name='Отчеты НовосибТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты НовосибТГФ по номеру')
async def get_all_by_tgf_novo(tgf_novo: str):
    content = await report_all_by_tgf_novo(tgf_novo)
    return content


@report_router.get(path='/tgf_tomsk/{tgf_tomsk}',
                   status_code=200,
                   name='Отчеты ТомскТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты ТомскТГФ по номеру')
async def get_all_by_tgf_tomsk(tgf_tomsk: str):
    content = await report_all_by_tgf_tomsk(tgf_tomsk)
    return content


@report_router.get(path='/tgf_more/{tgf_more}',
                   status_code=200,
                   name='Отчеты МорскойТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты МорскойТГФ по номеру')
async def get_all_by_tgf_more(tgf_more: str):
    content = await report_all_by_tgf_more(tgf_more)
    return content


@report_router.get(path='/tgf_tmn/{tgf_tmn}',
                   status_code=200,
                   name='Отчеты ТюмТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты ТюмТГФ по номеру')
async def get_all_by_tgf_tmn(tgf_tmn: str):
    content = await report_all_by_tgf_tmn(tgf_tmn)
    return content


@report_router.get(path='/tgf_kurgan/{tgf_kurgan}',
                   status_code=200,
                   name='Отчеты КурганТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты КурганТГФ по номеру')
async def get_all_by_tgf_kurgan(tgf_kurgan: str):
    content = await report_all_by_tgf_kurgan(tgf_kurgan)
    return content


# Авторы из отчетов
@report_router.get(path='/author',
                   status_code=200,
                   name='Получить всех авторов',
                   tags=['Отчеты'],
                   description='Получить всех авторов')
async def get_author():
    content = await report_get_author()
    return content

@report_router.get(path='/author/id/{id}',
                   status_code=200,
                   name='Получить автора',
                   tags=['Отчеты'],
                   description='Получить автора')
async def get_author_by_id(id:int):
    content = await report_get_author_by_id(id)
    return content


@report_router.get(path='/author/fio/{author}',
                   status_code=200,
                   name='Получить отчеты по автору',
                   tags=['Отчеты'],
                   description='Получить отчеты по автору')
async def get_report_by_author(author: str):
    content = await report_report_by_author(author)
    return content


# @report_router.get(path='/author/update',
#                    status_code=200,
#                    name='Обновить авторов',
#                    tags=['Отчеты'],
#                    description='Обновить авторов')
# async def get_update_author():
#     content = await report_get_update_author()
#     return content


@report_router.get(path='/author/count',
                   status_code=200,
                   name='Получить кол-во авторов',
                   tags=['Отчеты'],
                   description='Получить кол-во авторов')
async def get_model_author_count():
    content = await report_get_model_author_count()
    return content


# работа с листами карты из отчетов

@report_router.get(path='/list',
                   status_code=200,
                   name='Получить все листы',
                   tags=['Отчеты'],
                   description='Получить все листы')
async def get_list():
    content = await report_get_list()
    return content


# @report_router.get(path='/list/update',
#                    status_code=200,
#                    name='Обновить листы карты',
#                    tags=['Отчеты'],
#                    description='Обновить листы карты')
# async def get_update_list():
#     content = await report_get_update_list()
#     return content

@report_router.get(path='/list/count',
                   status_code=200,
                   name='Получить кол-во листов',
                   tags=['Отчеты'],
                   description='Получить кол-во листов')
async def get_model_list_count():
    content = await report_get_model_list_count()
    return content


# Субъекты РФ
@report_router.get(path='/subrf',
                   status_code=200,
                   name='Получить все Субъекты РФ',
                   tags=['Отчеты'],
                   description='Получить все Субъекты РФ')
async def get_subrf():
    content = await report_get_subrf()
    return content


# @report_router.get(path='/subrf/update',
#                    status_code=200,
#                    name='Обновить Субъекты РФ',
#                    tags=['Отчеты'],
#                    description='Обновить Субъекты РФ')
# async def get_update_subrf():
#     content = await report_get_update_subrf()
#     return content


@report_router.get(path='/subrf/count',
                   status_code=200,
                   name='Получить кол-во Субъектов РФ',
                   tags=['Отчеты'],
                   description='Получить кол-во Субъектов РФ')
async def get_model_subrf_count():
    content = await report_get_model_subrf_count()
    return content



# Организации
@report_router.get(path='/org',
                   status_code=200,
                   name='Получить все Организации',
                   tags=['Отчеты'],
                   description='Получить все Организации')
async def get_org():
    content = await report_get_org()
    return content


# @report_router.get(path='/org/update',
#                    status_code=200,
#                    name='Обновить Организации',
#                    tags=['Отчеты'],
#                    description='Обновить Организации')
# async def get_update_org():
#     content = await report_get_update_org()
#     return content


@report_router.get(path='/org/count',
                   status_code=200,
                   name='Получить кол-во Организации',
                   tags=['Отчеты'],
                   description='Получить кол-во Организации')
async def get_model_org_count():
    content = await report_get_model_org_count()
    return content


# Площади
@report_router.get(path='/area',
                   status_code=200,
                   name='Получить все Площади',
                   tags=['Отчеты'],
                   description='Получить все Площади')
async def get_area():
    content = await report_get_area()
    return content


# @report_router.get(path='/area/update',
#                    status_code=200,
#                    name='Обновить Площади',
#                    tags=['Отчеты'],
#                    description='Обновить Площади')
# async def get_update_area():
#     content = await report_get_update_area()
#     return content


@report_router.get(path='/area/count',
                   status_code=200,
                   name='Получить кол-во Площадей',
                   tags=['Отчеты'],
                   description='Получить кол-во Площадей')
async def get_model_area_count():
    content = await report_get_model_area_count()
    return content


# Месторождения


@report_router.get(path='/field',
                   status_code=200,
                   name='Получить все Месторождения',
                   tags=['Отчеты'],
                   description='Получить все Месторождения')
async def get_field():
    content = await report_get_field()
    return content


# @report_router.get(path='/field/update',
#                    status_code=200,
#                    name='Обновить Месторождения',
#                    tags=['Отчеты'],
#                    description='Обновить Месторождения')
# async def get_update_field():
#     content = await report_get_update_field()
#     return content


@report_router.get(path='/field/count',
                   status_code=200,
                   name='Получить кол-во Месторождений',
                   tags=['Отчеты'],
                   description='Получить кол-во Месторождений')
async def get_model_field_count():
    content = await report_get_model_field_count()
    return content


# ЛУ
@report_router.get(path='/lu',
                   status_code=200,
                   name='Получить все ЛУ',
                   tags=['Отчеты'],
                   description='Получить все ЛУ')
async def get_lu():
    content = await report_get_lu()
    return content


# @report_router.get(path='/lu/update',
#                    status_code=200,
#                    name='Обновить ЛУ',
#                    tags=['Отчеты'],
#                    description='Обновить ЛУ')
# async def get_update_lu():
#     content = await report_get_update_lu()
#     return content


@report_router.get(path='/lu/count',
                   status_code=200,
                   name='Получить кол-во ЛУ',
                   tags=['Отчеты'],
                   description='Получить кол-во ЛУ')
async def get_model_lu_count():
    content = await report_get_model_lu_count()
    return content


# Полезные ископаемые
@report_router.get(path='/pi',
                   status_code=200,
                   name='Получить все ПИ',
                   tags=['Отчеты'],
                   description='Получить все ПИ')
async def get_pi():
    content = await report_get_pi()
    return content


# @report_router.get(path='/pi/update',
#                    status_code=200,
#                    name='Обновить ПИ',
#                    tags=['Отчеты'],
#                    description='Обновить ПИ')
# async def get_update_pi():
#     content = await report_get_update_pi()
#     return content


@report_router.get(path='/pi/count',
                   status_code=200,
                   name='Получить кол-во ПИ',
                   tags=['Отчеты'],
                   description='Получить кол-во ПИ')
async def get_model_pi_count():
    content = await report_get_model_pi_count()
    return content



# Вид работ
@report_router.get(path='/vid_rab',
                   status_code=200,
                   name='Получить все Виды работ',
                   tags=['Отчеты'],
                   description='Получить все Виды работ')
async def get_vid_rab():
    content = await report_get_vid_rab()
    return content


# @report_router.get(path='/vid_rab/update',
#                    status_code=200,
#                    name='Обновить Вид работ',
#                    tags=['Отчеты'],
#                    description='Обновить Вид работ')
# async def get_update_vid_rab():
#     content = await report_get_update_vid_rab()
#     return content


@report_router.get(path='/vid_rab/count',
                   status_code=200,
                   name='Получить кол-во Вид работ',
                   tags=['Отчеты'],
                   description='Получить кол-во Вид работ')
async def get_model_vid_rab_count():
    content = await report_get_model_vid_rab_count()
    return content

@report_router.get(path='/index/create',
                status_code=200,
                # response_model=List[s_ngr],
                name='Создать Полнотекстовый индекс по отчетам',
                tags=['Отчеты'],
                description='Создать Полнотекстовый по отчетам')
async def get_report_index_create():
    content = await report_index_create()
    return content


@report_router.get(path='/search/{search_str}',
                status_code=200,
                # response_model=List[s_ngr],
                name='Полнотекстовый поиск по отчетам',
                tags=['Отчеты'],
                description='Полнотекстовый поиск по отчетам')
async def get_report_fulltext_search(search_str, request: Request ):
    client_host = request.client.host
    content = await report_fulltext_search(search_str, client_host )
    return content

@report_router.get(path='/query',
                status_code=200,
                # response_model=List[s_ngr],
                name='Полнотекстовый поиск по отчетам',
                tags=['Отчеты'],
                description='Полнотекстовый поиск по отчетам по параметрам')
async def get_report_fulltext_search(request: Request , q: str = None):
    client_host = request.client.host
    content = await report_fulltext_search(q, client_host)
    return content


@report_router.post(path='/message',
                status_code=200,
                name='Создать Пожелание',
                tags=['Отчеты'],
                description='Создать Пожелание')
async def post_report_message_create(message: S_R_MESSAGE_POST):
    content = await report_message_create(message)
    return content


@report_router.get(path='/message',
                status_code=200,
                name='Получить Пожелания',
                tags=['Отчеты'],
                description='Получить Пожелания')
async def get_report_message():
    content = await report_get_message()
    return content

