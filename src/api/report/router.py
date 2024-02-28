from fastapi import APIRouter, UploadFile
from src.api.report.services import report_all_objects, report_upload_file

report_router = APIRouter(prefix="/report", tags=["Отчеты"])


@report_router.get(path='/all',
                status_code=200,
                name='Отчеты',
                tags=['Отчеты'],
                description='Все Отчеты')
async def get_all():
    content = await report_all_objects()
    return content


@report_router.post(path="/upload/",
                  status_code=200,
                  name='Загрузить Excel файл',
                  tags=['Отчеты'],
                  description='Загрузить Excel файл')
async def upload_file(file: UploadFile):
    content = await report_upload_file(file)
    return content