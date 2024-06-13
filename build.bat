venv\Scripts\pyinstaller --onefile ^
--hidden-import=uvicorn ^
--hidden-import=asyncpg.pgproto.pgproto ^
--hidden-import=celery.fixups ^
--hidden-import=celery.fixups.django ^
--hidden-import=win32timezone ^
--name=gdx2 ^
service.py