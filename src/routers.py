from fastapi import APIRouter

from src.db.router import router_db
from src.ext.router import router_ext
from src.files.router import router_files

api_router = APIRouter(prefix='/api/v1')


@api_router.get("/health", description="Health Check", tags=["Health Check"])
def ping():
    """Health check."""
    return {"msg": "pong!"}


api_router.include_router(router_files, prefix="/files", tags=["Файлы"])  #
api_router.include_router(router_ext, prefix="/ext", tags=["Расширения"])  #
api_router.include_router(router_db, prefix="/db", tags=["База данных"])  #
