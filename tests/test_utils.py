# tests/test_utils.py
import pytest
from src.api.report.utils import str_get_folder, str_get_full_path_with_format, str_tgf_format

def test_string_utils():
    """Тест утилит строк"""
    # Проверка функций форматирования строк
    assert str_get_folder("test/path") == "test"
    assert str_tgf_format("test") == "test"
    # и т.д.
