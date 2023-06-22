from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
# from src.files.schemas import FILES_S
from src.files.services import files_get_all_count, src_add, src_get_all, src_get_by_id

router_files = APIRouter(
    # prefix="/files",
    tags=["Файлы"]
)


@router_files.get(path='/count',
                  status_code=200,
                  name='Получить количество Файлов',
                  tags=['Файлы'],
                  description='Получает количество Файлов')
async def get_count():
    content = await files_get_all_count()
    return content


@router_files.post(path='/source/',
                   status_code=200,
                   name='Добавить источник',
                   tags=['Файлы'],
                   description='Добавить источник', )
async def source_add(folder: str,  session: AsyncSession = Depends(get_async_session)):
    content = await src_add(folder, session)
    return content

@router_files.get(path='/source/',
                   status_code=200,
                   name='Получить все источники',
                   tags=['Файлы'],
                   description='Получить все источники', )
async def source_get_all(session: AsyncSession = Depends(get_async_session)):
    content = await src_get_all(session)
    return content

@router_files.get(path='/source/{id}',
                   status_code=200,
                   name='Получить все источник',
                   tags=['Файлы'],
                   description='Получить все источник', )
async def source_get_all(id:int, session: AsyncSession = Depends(get_async_session)):
    content = await src_get_by_id(id, session)
    return content

# async def add_specific_operations(src_new: FILE_SRC_S_CREATE, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(FILE_SRC_M).values(**src_new.dict())
#     print(stmt)
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": "success"}