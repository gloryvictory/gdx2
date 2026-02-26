import os
import sys
from fastapi import APIRouter

from src.api.sta.router import sta_router
from src.api.stall.router import stall_router
from src.api.stl.router import stl_router
from src.api.stp.router import stp_router

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

# api_router.include_router(router_db, prefix="/db", tags=["База данных"])  #
