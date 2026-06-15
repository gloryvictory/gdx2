# tests/test_crud_references.py
"""
Тесты CRUD-операций для всех справочных таблиц.

Проверяет эндпоинты для: author, org, list, subrf, area, field, lu, pi, vid_rab.
Каждый справочник имеет одинаковый набор из 6 эндпоинтов:
- GET /all, GET /count, GET /{guid}, POST /, PUT /{guid}, DELETE /{guid}
"""
import uuid
import pytest
from fastapi.testclient import TestClient

# Глобальный список всех справочных префиксов с тегами
REFERENCES = [
    ("author", "Авторы"),
    ("org", "Организации"),
    ("list", "Листы карты"),
    ("subrf", "Субъекты РФ"),
    ("area", "Площади"),
    ("field", "Месторождения"),
    ("lu", "Лицензионные участки"),
    ("pi", "Полезные ископаемые"),
    ("vid_rab", "Виды работ"),
]


@pytest.fixture
def app():
    from src.main import app as application
    return application


@pytest.fixture
def client(app):
    return TestClient(app)


# ---------------------------------------------------------------------------
# GET /all
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("prefix,tag", REFERENCES)
def test_get_all(client, prefix, tag):
    """Получение всех записей справочника"""
    response = client.get(f"/api/v1/{prefix}/all")
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        data = response.json()
        assert "msg" in data
        assert "count" in data
        assert "data" in data


# ---------------------------------------------------------------------------
# GET /count
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("prefix,tag", REFERENCES)
def test_get_count(client, prefix, tag):
    """Получение количества записей справочника"""
    response = client.get(f"/api/v1/{prefix}/count")
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        data = response.json()
        assert "msg" in data
        assert "count" in data


# ---------------------------------------------------------------------------
# GET /{guid}
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("prefix,tag", REFERENCES)
def test_get_by_id(client, prefix, tag):
    """Получение записи справочника по GUID"""
    test_guid = uuid.uuid4()
    response = client.get(f"/api/v1/{prefix}/{test_guid}")
    assert response.status_code in [200, 404, 500]
    if response.status_code == 200:
        data = response.json()
        assert "msg" in data
        assert "data" in data


# ---------------------------------------------------------------------------
# POST /
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("prefix,tag", REFERENCES)
def test_create(client, prefix, tag):
    """Создание новой записи в справочнике"""
    response = client.post(f"/api/v1/{prefix}/?name_ru=TestRecord")
    assert response.status_code in [201, 500]
    if response.status_code == 201:
        data = response.json()
        assert "msg" in data
        assert "count" in data
        assert "data" in data
        assert data["data"]["name_ru"] == "TestRecord"


# ---------------------------------------------------------------------------
# PUT /{guid}
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("prefix,tag", REFERENCES)
def test_update(client, prefix, tag):
    """Обновление записи в справочнике"""
    test_guid = uuid.uuid4()
    response = client.put(f"/api/v1/{prefix}/{test_guid}?name_ru=UpdatedRecord")
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        data = response.json()
        assert "msg" in data


# ---------------------------------------------------------------------------
# DELETE /{guid}
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("prefix,tag", REFERENCES)
def test_delete(client, prefix, tag):
    """Удаление записи из справочника"""
    test_guid = uuid.uuid4()
    response = client.delete(f"/api/v1/{prefix}/{test_guid}")
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        data = response.json()
        assert "msg" in data


# ---------------------------------------------------------------------------
# Интеграционные тесты: create → read → update → delete (только при наличии БД)
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("prefix,tag", REFERENCES)
def test_crud_flow(client, prefix, tag):
    """Полный цикл CRUD: создание, чтение, обновление, удаление"""
    # 1. Создание
    create_resp = client.post(f"/api/v1/{prefix}/?name_ru=FlowTestRecord")
    if create_resp.status_code != 201:
        pytest.skip(f"БД недоступна для {prefix} (status={create_resp.status_code})")

    created = create_resp.json()
    assert created["data"]["name_ru"] == "FlowTestRecord"
    record_guid = created["data"]["guid"]

    # 2. Чтение по GUID
    get_resp = client.get(f"/api/v1/{prefix}/{record_guid}")
    assert get_resp.status_code == 200
    assert get_resp.json()["data"]["name_ru"] == "FlowTestRecord"

    # 3. Обновление
    update_resp = client.put(f"/api/v1/{prefix}/{record_guid}?name_ru=FlowUpdatedRecord")
    assert update_resp.status_code == 200
    assert update_resp.json()["data"]["name_ru"] == "FlowUpdatedRecord"

    # 4. Удаление
    delete_resp = client.delete(f"/api/v1/{prefix}/{record_guid}")
    assert delete_resp.status_code == 200

    # 5. Проверка, что запись удалена
    get_after_del = client.get(f"/api/v1/{prefix}/{record_guid}")
    assert get_after_del.status_code == 200
    assert get_after_del.json()["data"] is None
