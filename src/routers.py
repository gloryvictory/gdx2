from fastapi import APIRouter

from src.api.area.router import area_router
from src.api.ext.router import router_ext
from src.api.field.router import fields_router
from src.api.file.router import router_files
from src.api.health.router import router_health
from src.api.lu.router import lu_router
from src.api.ngo.router import ngo_router
from src.api.ngp.router import ngp_router
from src.api.ngr.router import ngr_router
from src.api.search.router import search_router
from src.api.update.router import update_router
from src.api.well.router import well_router

# from src.db.router import router_db
# from src.ext.router import router_ext
# from src.file.router import router_files

api_router = APIRouter(prefix='/api/v1')


api_router.include_router(router_health)
api_router.include_router(router_files)  #
api_router.include_router(router_ext)  #
api_router.include_router(ngp_router)  #
api_router.include_router(ngo_router)  #
api_router.include_router(ngr_router)  #
api_router.include_router(lu_router)  #
api_router.include_router(fields_router)  #
api_router.include_router(area_router)  #
api_router.include_router(well_router)  #
api_router.include_router(search_router)  #
api_router.include_router(update_router)  #

# api_router.include_router(router_db, prefix="/db", tags=["База данных"])  #
