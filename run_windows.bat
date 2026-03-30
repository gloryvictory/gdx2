set PYTHONPATH=c:\Glory\Projects\Python\zsniigg\gdx2
rem python src\main.py
venv\Scripts\activate
uvicorn src.main:app --reload --host 0.0.0.0 --port 8001
