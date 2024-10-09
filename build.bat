venv\Scripts\pyinstaller -y  ^
--clean  ^
--additional-hooks-dir extra-hooks  ^
--onefile  ^
--hidden-import=uvicorn ^
--hidden-import=asyncpg.pgproto.pgproto ^
--hidden-import=celery.fixups ^
--hidden-import=celery.fixups.django ^
--hidden-import=celery.app.amqp ^
--hidden-import=celery.backends ^
--hidden-import=celery.backends.redis ^
--hidden-import=celery.app.events ^
--hidden-import=kombu.transport.redis ^
--hidden-import=win32timezone ^
--name=gdx2 ^
.\src\main.py
rem service.py