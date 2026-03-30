# tests/test_schemas.py
import pytest
from src.schemas import S_REPORT_TGF, S_HISTORY, S_HISTORY_TASK

def test_report_schema_fields():
    """Тест полей схемы отчета"""
    # Проверка наличия всех необходимых полей
    schema = S_REPORT_TGF(
        name_ru="Test",
        folder_root="/test",
        folder_link="/test",
        folder_short="/test",
        folder_name="test",
        rgf="test",
        tgf_hmao="test",
        tgf_ynao="test",
        tgf_kras="test",
        tgf_ekat="test",
        tgf_omsk="test",
        tgf_novo="test",
        tgf_tomsk="test",
        tgf_more="test",
        tgf_tmn="test",
        tgf_kurgan="test",
        tgf="test",
        report_name="test",
        author_name="test",
        year_str="2023",
        year_int=2023,
        territory_name="test",
        subrf_name="test",
        list_name="test",
        part_name="test",
        areaoil="test",
        field="test",
        lu="test",
        pi_name="test",
        fin_name="test",
        org_name="test",
        zsniigg_report="test",
        inf_report="test",
        vid_rab="test",
        comments="test",
        lat=0.0,
        lon=0.0,
        is_alive=True,
        report_fts="test",
        created_at="2023-01-01T00:00:00",
        updated_at="2023-01-01T00:00:00"
    )
    assert schema.name_ru == "Test"

def test_history_schema_fields():
    """Тест полей схемы истории"""
    schema = S_HISTORY(
        name_ru="Test",
        url="/test",
        search_str="test",
        addr_ip="127.0.0.1",
        user_name="test",
        user_login="test",
        created_at="2023-01-01T00:00:00",
        updated_at="2023-01-01T00:00:00"
    )
    assert schema.name_ru == "Test"
