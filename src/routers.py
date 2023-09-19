from fastapi import APIRouter

from src.api.ext.router import router_ext
from src.api.field.endpoint import fields_router
from src.api.files.router import router_files
from src.api.lu.endpoint import lu_router
from src.api.ngo.endpoint import ngo_router
from src.api.ngp.endpoint import ngp_router
from src.api.ngr.endpoint import ngr_router

# from src.db.router import router_db
# from src.ext.router import router_ext
# from src.files.router import router_files

api_router = APIRouter(prefix='/api/v1')


@api_router.get("/health", description="Health Check", tags=["Health Check"])
def ping():
    """Health check."""
    return {"msg": "pong!"}


api_router.include_router(router_files)  #
api_router.include_router(router_ext)  #
api_router.include_router(ngp_router)  #
api_router.include_router(ngo_router)  #
api_router.include_router(ngr_router)  #
api_router.include_router(fields_router)  #
api_router.include_router(lu_router)  #

# api_router.include_router(router_db, prefix="/db", tags=["База данных"])  #
