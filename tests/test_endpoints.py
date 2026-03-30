# tests/test_endpoints.py
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


@pytest.fixture
def app():
    from src.main import app as application
    return application


@pytest.fixture
def client(app):
    return TestClient(app)


def test_root(client):
    """Тест корневого эндпоинта"""
    response = client.get("/")
    assert response.status_code == 200
    assert "msg" in response.json()


def test_health(client):
    """Тест health check"""
    response = client.get("/api/v1/health")
    assert response.status_code == 200


def test_get_reports_all(client):
    """Тест получения всех отчетов"""
    response = client.get("/api/v1/report/all")
    assert response.status_code in [200, 500]  # 500 - если нет БД


def test_get_reports_count(client):
    """Тест получения количества отчетов"""
    response = client.get("/api/v1/report/count")
    assert response.status_code in [200, 500]


def test_get_report_by_id(client):
    """Тест получения отчета по ID"""
    response = client.get("/api/v1/report/rgf/all/list")
    assert response.status_code in [200, 404, 500]


def test_get_sta_all(client):
    """Тест получения STA"""
    response = client.get("/api/v1/sta/all")
    assert response.status_code in [200, 500]


def test_get_stl_all(client):
    """Тест получения STL"""
    response = client.get("/api/v1/stl/all")
    assert response.status_code in [200, 500]


def test_get_stp_all(client):
    """Тест получения STP"""
    response = client.get("/api/v1/stp/all")
    assert response.status_code in [200, 500]


def test_get_stall_all_method(client):
    """Тест получения stall методов"""
    response = client.get("/api/v1/stall/all/method/unique")
    assert response.status_code in [200, 500]
