from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.file.services import files_get_count, files_get_all, files_get_all_limit_offset, src_get_all, \
    files_get_by_id
from src.db.db import get_async_session
# from src.file.schemas import FILES_S
# from src.file.services import files_get_all_count, src_add, src_get_all, src_get_by_id

router_files = APIRouter(
    prefix="/file",
    tags=["Файлы"]
)


@router_files.get(path='/count',
                  status_code=200,
                  name='Получить количество Файлов',
                  tags=['Файлы'],
                  description='Получает количество Файлов')
async def get_count():
    content = await files_get_count()
    return content


@router_files.get(path='/all',
                  status_code=200,
                  name='Получить список всех Файлов',
                  tags=['Файлы'],
                  description='Получает список всех Файлов')
async def get_all():
    content = await files_get_all()
    return content


@router_files.get(path='/all/{limit}/{offset}',
                  status_code=200,
                  name='Получить список всех Файлов с указанием лимита и оффсета',
                  tags=['Файлы'],
                  description='Получить список всех Файлов с указанием лимита и оффсета')
async def get_all_limit_offset(limit: int, offset: int):
    content = await files_get_all_limit_offset(limit, offset)
    return content


@router_files.get(path='/{id}',
                  status_code=200,
                  name='Получить Файл по ID',
                  tags=['Файлы'],
                  description='Получить Файл по ID')
async def get_get_by_id(_id: int):
    content = await files_get_by_id(_id)
    return content


@router_files.get(path='/source/',
                  status_code=200,
                  name='Получить все источники',
                  tags=['Файлы'],
                  description='Получить все источники', )
async def source_get_all():
    content = await src_get_all()
    return content

#
# @router_files.post(path='/source/',
#                    status_code=200,
#                    name='Добавить источник',
#                    tags=['Файлы'],
#                    description='Добавить источник', )
# async def source_add(folder: str, session: AsyncSession = Depends(get_async_session)):
#     # content = await src_add(folder, session)
#     # return content
#     content = "ОК"
#     return content
#
#
# @router_files.get(path='/source/',
#                   status_code=200,
#                   name='Получить все источники',
#                   tags=['Файлы'],
#                   description='Получить все источники', )
# async def source_get_all(session: AsyncSession = Depends(get_async_session)):
#     # content = await src_get_all(session)
#     # return content
#     content = "ОК"
#     return content


# @router_files.get(path='/source/{id}',
#                   status_code=200,
#                   name='Получить все источник',
#                   tags=['Файлы'],
#                   description='Получить все источник', )
# async def source_get_all(id: int, session: AsyncSession = Depends(get_async_session)):
#     # content = await src_get_by_id(id, session)
#     # return content
#     content = "ОК"
#     return content

# async def add_specific_operations(src_new: FILE_SRC_S_CREATE, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(FILE_SRC_M).values(**src_new.dict())
#     print(stmt)
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": "success"}
