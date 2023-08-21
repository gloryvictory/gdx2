from fastapi import APIRouter, UploadFile, Depends  # , Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.ext.services import ext_get_all_count, ext_get_uniq, ext_upload_file, ext_get_info_by_ext, \
    ext_get_ext_by_cat, ext_get_all, ext_get_ext_by_product, ext_get_ext_by_project

# from src.ext.services import ext_get_all_count, ext_upload_file, ext_get_uniq

router_ext = APIRouter(
    prefix="/ext",
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


@router_ext.get(path='/uniq',
                status_code=200,
                name='Получить Расширения уникальные',
                tags=['Расширения'],
                description='Получает Расширения уникальные')
async def get_count():
    content = await ext_get_uniq()
    return content


@router_ext.get(path='/all',
                status_code=200,
                name='Получить Все Расширения',
                tags=['Расширения'],
                description='Получает Все Расширения')
async def get_count():
    content = await ext_get_all()
    return content


@router_ext.get(path='/info/{ext}',
                status_code=200,
                name='Получить информацию по Расширению',
                tags=['Расширения'],
                description='Получить информацию по Расширению')
async def get_info_by_ext(ext: str):
    content = await ext_get_info_by_ext(ext)
    return content


@router_ext.get(path='/category/{cat}',
                status_code=200,
                name='Получить расширения по конкретной категории',
                tags=['Расширения'],
                description='Получить расширения по конкретной категории')
async def get_ext_by_cat(cat: str):
    content = await ext_get_ext_by_cat(cat)
    return content


@router_ext.get(path='/product/{product}',
                status_code=200,
                name='Получить расширения по продуктам',
                tags=['Расширения'],
                description='Получить расширения по продуктам')
async def get_ext_by_product(product: str):
    content = await ext_get_ext_by_product(product)
    return content


@router_ext.get(path='/project',
                status_code=200,
                name='Получить расширения файлов проекта',
                tags=['Расширения'],
                description='Получить расширения файлов проекта')
async def get_ext_by_project():
    content = await ext_get_ext_by_project()
    return content


@router_ext.post(path="/upload/",
                 status_code=200,
                 name='Загрузить Excel файл',
                 tags=['Расширения'],
                 description='Загрузить Excel файл')
async def upload_file(file: UploadFile):
    content = await ext_upload_file(file)
    return content
