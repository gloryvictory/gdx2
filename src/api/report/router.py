from fastapi import APIRouter, UploadFile
from src.api.report.services import (
    report_all_objects, report_upload_file, report_update, report_get_all_count,
    report_all_no_folder, report_all_rgf, report_all_tgf_hmao, report_all_tgf_ynao, report_all_tgf_kras,
    report_all_tgf_ekat, report_all_tgf_omsk, report_all_tgf_novo, report_all_tgf_tomsk, report_all_tgf_more,
    report_all_tgf_tmn, report_all_tgf_kurgan, report_all_tgf, report_all_year, report_get_update_author,
    report_report_by_author, report_get_all_by_year, report_all_by_rgf, report_all_by_tgf_hmao, report_all_by_tgf_ynao,
    report_all_by_tgf_kras, report_all_by_tgf_ekat, report_all_by_tgf_omsk, report_all_by_tgf_novo,
    report_all_by_tgf_tomsk, report_all_by_tgf_more, report_all_by_tgf_tmn, report_all_by_tgf_kurgan
    )

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
async def get_all_by_year(year:str):
    content = await report_get_all_by_year(year)
    return content


@report_router.get(path='/update_author',
                   status_code=200,
                   name='Обновить авторов',
                   tags=['Отчеты'],
                   description='Обновить авторов')
async def get_update_author():
    content = await report_get_update_author()
    return content


@report_router.get(path='/author/{author}',
                   status_code=200,
                   name='Получить отчеты по автору',
                   tags=['Отчеты'],
                   description='Получить отчеты по автору')
async def get_report_by_author(author:str):
    content = await report_report_by_author(author)
    return content



@report_router.get(path='/rgf/{rgf}',
                   status_code=200,
                   name='Отчеты РГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты РГФ по номеру')
async def get_all_by_rgf(rgf:str):
    content = await report_all_by_rgf(rgf)
    return content

@report_router.get(path='/tgf_hmao/{tgf_hmao}',
                   status_code=200,
                   name='Отчеты ХМТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты ХМТГФ по номеру')
async def get_all_by_tgf_hmao(tgf_hmao:str):
    content = await report_all_by_tgf_hmao(tgf_hmao)
    return content


@report_router.get(path='/tgf_ynao/{tgf_ynao}',
                   status_code=200,
                   name='Отчеты ЯНТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты ЯНТГФ по номеру')
async def get_all_by_tgf_ynao(tgf_ynao:str):
    content = await report_all_by_tgf_ynao(tgf_ynao)
    return content


@report_router.get(path='/tgf_kras/{tgf_kras}',
                   status_code=200,
                   name='Отчеты КраснТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты КраснТГФ по номеру')
async def get_all_by_tgf_kras(tgf_kras:str):
    content = await report_all_by_tgf_kras(tgf_kras)
    return content


@report_router.get(path='/tgf_ekat/{tgf_ekat}',
                   status_code=200,
                   name='Отчеты ЕкатерТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты ЕкатерТГФ по номеру')
async def get_all_by_tgf_ekat(tgf_ekat:str):
    content = await report_all_by_tgf_ekat(tgf_ekat)
    return content


@report_router.get(path='/tgf_omsk/{tgf_omsk}',
                   status_code=200,
                   name='Отчеты ОмскТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты ОмскТГФ по номеру')
async def get_all_by_tgf_omsk(tgf_omsk:str):
    content = await report_all_by_tgf_omsk(tgf_omsk)
    return content

@report_router.get(path='/tgf_novo/{tgf_novo}',
                   status_code=200,
                   name='Отчеты НовосибТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты НовосибТГФ по номеру')
async def get_all_by_tgf_novo(tgf_novo:str):
    content = await report_all_by_tgf_novo(tgf_novo)
    return content


@report_router.get(path='/tgf_tomsk/{tgf_tomsk}',
                   status_code=200,
                   name='Отчеты ТомскТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты ТомскТГФ по номеру')
async def get_all_by_tgf_tomsk(tgf_tomsk:str):
    content = await report_all_by_tgf_tomsk(tgf_tomsk)
    return content


@report_router.get(path='/tgf_more/{tgf_more}',
                   status_code=200,
                   name='Отчеты МорскойТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты МорскойТГФ по номеру')
async def get_all_by_tgf_more(tgf_more:str):
    content = await report_all_by_tgf_more(tgf_more)
    return content


@report_router.get(path='/tgf_tmn/{tgf_tmn}',
                   status_code=200,
                   name='Отчеты ТюмТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты ТюмТГФ по номеру')
async def get_all_by_tgf_tmn(tgf_tmn:str):
    content = await report_all_by_tgf_tmn(tgf_tmn)
    return content


@report_router.get(path='/tgf_kurgan/{tgf_kurgan}',
                   status_code=200,
                   name='Отчеты КурганТГФ по номеру',
                   tags=['Отчеты'],
                   description='Отчеты КурганТГФ по номеру')
async def get_all_by_tgf_kurgan(tgf_kurgan:str):
    content = await report_all_by_tgf_kurgan(tgf_kurgan)
    return content