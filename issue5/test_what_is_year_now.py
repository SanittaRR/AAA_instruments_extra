from what_is_year_now import what_is_year_now
from unittest.mock import patch
import pytest


def test_get_cases1():
    """ Проверка правильности вывода текущего года,
        при формате даты YYYY-MM-DD """
    with patch("urllib.request.urlopen") as mocked_get_cases,\
         patch("json.load") as mocked_get_cases2:
        mocked_get_cases2.return_value = \
            {'currentDateTime': "2022-11-18 00:00:00"}
        assert what_is_year_now() == 2022
        mocked_get_cases.assert_called_once()


def test_get_cases2():
    """ Проверка правильности вывода текущего года,
        при формате даты DD.MM.YYYY """
    with patch("urllib.request.urlopen") as mocked_get_cases,\
         patch("json.load") as mocked_get_cases2:
        mocked_get_cases2.return_value = \
            {'currentDateTime': "01.10.2023 00:00:00"}
        assert what_is_year_now() == 2023
        mocked_get_cases.assert_called_once()


def test_get_cases3():
    """ Проверка выдачи ошибки,
        при неправильном формате даты """
    with patch("json.load") as mocked_get_cases2:
        mocked_get_cases2.return_value = \
            {'currentDateTime': "01:10:2023 00:00:00"}
        with pytest.raises(ValueError):
            what_is_year_now()


def test_raise_type_error():
    """ Перехват исключения при получении аргумента
        неправильного типа"""
    with pytest.raises(TypeError):
        what_is_year_now(23)
