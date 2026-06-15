import os
import sys
from fastapi import APIRouter

from src.api.sta.router import sta_router
from src.api.stall.router import stall_router
from src.api.stl.router import stl_router
from src.api.stp.router import stp_router
from src.api.author.router import author_router
from src.api.org.router import org_router
from src.api.list.router import list_router
from src.api.subrf.router import subrf_router
from src.api.area.router import area_router
from src.api.field.router import field_router
from src.api.lu.router import lu_router
from src.api.pi.router import pi_router
from src.api.vid_rab.router import vid_rab_router

sys.path.insert(1, 'src')
os.environ['PYTHONPATH'] = os.environ.get('PYTHONPATH', '') + ';' + os.getcwd()

from src.api.health.router import router_health

from src.api.report.router import report_router

api_router = APIRouter(prefix='/api/v1')


api_router.include_router(router_health)

api_router.include_router(report_router)  #
api_router.include_router(sta_router)
api_router.include_router(stl_router)
api_router.include_router(stp_router)
api_router.include_router(stall_router)
api_router.include_router(author_router)
api_router.include_router(org_router)
api_router.include_router(list_router)
api_router.include_router(subrf_router)
api_router.include_router(area_router)
api_router.include_router(field_router)
api_router.include_router(lu_router)
api_router.include_router(pi_router)
api_router.include_router(vid_rab_router)

# api_router.include_router(router_db, prefix="/db", tags=["База данных"])  #
