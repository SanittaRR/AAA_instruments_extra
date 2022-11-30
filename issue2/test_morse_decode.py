from morse import decode
import pytest


@pytest.mark.parametrize(
    "source_morse,result", [
        ('... --- ...', 'SOS'),
        ('.... ..', 'HI'),
        ('-.-- . ...', 'YES'),
    ], )
def test_decode(source_morse, result):
    """ Проверяет правильность декодирования функции decode"""
    assert decode(source_morse) == result
