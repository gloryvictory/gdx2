# uvicorn main:app --reload
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from src import cfg
from src.db.db import get_async_session, engine
from src.routers import api_router

app = FastAPI(title="GDX2 App")

# app.mount("/static", StaticFiles(directory="static"), name="static")


# , root_path=API_VERSION
# origins = [
#     "http://localhost",
#     "http://localhost:8080",
#     "https://localhost",
#     "https://localhost:8080",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)


# Root API
@app.get("/", status_code=200,
         name='Get Info',
         tags=['Главная'],
         description='Получает информацию о сервисе')
def root() -> JSONResponse:
    url_swagger = f"http://{cfg.SERVER_HOST}:{cfg.SERVER_PORT}/docs"

    return JSONResponse(status_code=200,
                        content={
                            "msg": "Success",
                            "Info": "Hello it is FastAPI-NSI project",
                            "Swagger Documentation": url_swagger})


app.include_router(api_router)

# for router in all_routers:
#     app.include_router(router)


@app.on_event("startup")
async def startup() -> None:
    pass
    # redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    # FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


@app.on_event("shutdown")
async def shutdown() -> None:
    pass
    session = get_async_session()
    await session.aclose()
    await engine.dispose()



#     database_ = app.state.database
#     if database_.is_connected:
#         await database_.disconnect()


if __name__ == "__main__":
    # set_logger()
    uvicorn.run("main:app", host=cfg.SERVER_HOST, port=int(cfg.SERVER_PORT), reload=True)
