from fastapi import APIRouter

# from src.files.schemas import FILES_S
from src.files.services import files_get_all_count

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

