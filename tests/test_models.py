# tests/test_models.py
import pytest
from src.models import M_REPORT_TGF, M_HISTORY, M_HISTORY_TASK

def test_report_model_fields():
    """Тест полей модели отчета"""
    # Проверка наличия всех необходимых полей
    assert hasattr(M_REPORT_TGF, 'folder_root')
    assert hasattr(M_REPORT_TGF, 'report_name')
    assert hasattr(M_REPORT_TGF, 'author_name')
    assert hasattr(M_REPORT_TGF, 'year_int')
    # и т.д.

def test_history_model_fields():
    """Тест полей модели истории"""
    assert hasattr(M_HISTORY, 'url')
    assert hasattr(M_HISTORY, 'search_str')
    assert hasattr(M_HISTORY, 'addr_ip')
    # и т.д.

def test_history_task_model_fields():
    """Тест полей модели истории задач"""
    assert hasattr(M_HISTORY_TASK, 'task_id')
    assert hasattr(M_HISTORY_TASK, 'task_type')
    assert hasattr(M_HISTORY_TASK, 'task_name')
    # и т.д.
