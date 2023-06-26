from fastapi import APIRouter, UploadFile  # , Depends, HTTPException
from src.ext.services import ext_get_all_count, ext_upload_file

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
#
# @router_files.post(path='/source/',
#                    status_code=200,
#                    name='Добавить источник',
#                    tags=['Расширения'],
#                    description='Добавить источник', )
# async def source_add(folder: str,  session: AsyncSession = Depends(get_async_session)):
#     content = await src_add(folder, session)
#     return content
#
# @router_files.get(path='/source/',
#                    status_code=200,
#                    name='Получить все источники',
#                    tags=['Расширения'],
#                    description='Получить все источники', )
# async def source_get_all(session: AsyncSession = Depends(get_async_session)):
#     content = await src_get_all(session)
#     return content
#
# @router_files.get(path='/source/{id}',
#                    status_code=200,
#                    name='Получить все источник',
#                    tags=['Расширения'],
#                    description='Получить все источник', )
# async def source_get_all(id:int, session: AsyncSession = Depends(get_async_session)):
#     content = await src_get_by_id(id, session)
#     return content

# async def add_specific_operations(src_new: FILE_SRC_S_CREATE, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(FILE_SRC_M).values(**src_new.dict())
#     print(stmt)
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": "success"}