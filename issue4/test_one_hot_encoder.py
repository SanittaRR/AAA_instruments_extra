from one_hot_encoder import fit_transform
import pytest


def test_moscow():
    """ Проверяет правильно ли трансформируется Moscow"""
    assert fit_transform('Moscow') == [('Moscow', [1])]


def test_empty():
    """ Проверяет правильность вывода при обработке
        пустой строки"""
    assert fit_transform('') == [('', [1])]


def test_raise_type_error():
    """ Перехват исключения при получении аргумента
        неправильного типа"""
    with pytest.raises(TypeError):
        fit_transform(2)


@pytest.mark.parametrize(
    "source_cities,result", [
        (['Moscow', 'New York', 'Moscow', 'London'],
         [
             ('Moscow', [0, 0, 1]),
             ('New York', [0, 1, 0]),
             ('Moscow', [0, 0, 1]),
             ('London', [1, 0, 0]),
         ]
         )
    ], )
def test_decode(source_cities, result):
    """ Проверяет, правильность трансформации списка городов"""
    assert fit_transform(source_cities) == result
