# tests/test_database.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.db import engine, async_session_maker

def test_database_connection():
    """Тест подключения к базе данных"""
    # Проверка соединения с базой данных
    connection = engine.connect()
    assert connection is not None
    connection.close()

def test_session_creation():
    """Тест создания сессии"""
    async_session = async_session_maker()
    assert async_session is not None
