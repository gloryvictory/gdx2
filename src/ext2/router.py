from fastapi import APIRouter

from src.ext2.services import ext_get_all_count


router_ext2 = APIRouter(
    # prefix="/files",
    tags=["Расширения 2"]
)


@router_ext2.get(path='/count',
                  status_code=200,
                  name='Получить количество Расширений',
                  tags=['Расширения 2'],
                  description='Получает количество Расширений')
async def get_count():
    content = await ext_get_all_count()
    return content
