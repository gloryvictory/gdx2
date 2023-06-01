from fastapi import APIRouter, HTTPException

from src.database import Base, engine


router_db = APIRouter(
    # prefix="/files",
    tags=["База данных"]
)


@router_db.get(path='/create',
                  status_code=200,
                  name='Создать таблицы',
                  tags=['База данных'],
                  description='Создать таблицы')
# async def db_create(session: AsyncSession = Depends(get_async_session)):
async def db_create():
    try:
        # User.__table__.create(engine)
        # Base.metadata.create_all(engine)
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
        return {
            "status": "success",
            # "data": result.all(),
            "details": None
        }
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": Exception
        })


