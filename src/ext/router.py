from fastapi import APIRouter, UploadFile, Depends  # , Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.ext.services import ext_get_all_count, ext_upload_file
from src.database import get_async_session

router_ext = APIRouter(
    # prefix="/files",
    tags=["Расширения"]
)


@router_ext.get(path='/count',
                  status_code=200,
                  name='Получить количество Расширений',
                  tags=['Расширения'],
                  description='Получает количество Расширений')
async def get_count():
    content = await ext_get_all_count()
    return content


@router_ext.post(path="/upload/",
                  status_code=200,
                  name='Загрузить Excel файл',
                  tags=['Расширения'],
                  description='Загрузить Excel файл')
async def upload_file(file: UploadFile):
    content = await ext_upload_file(file)
    return content
