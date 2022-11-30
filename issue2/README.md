Шаги для запуска:
1) Установка пакета pytest
> $ pip install -U pytest

2) Run Python tests for main.test_decode
Запускаем параметрический тест, в котором проверяются 3 условия
> $ python -m pytest -v issue2/test_morse_decode.py

3) Передаем в result
> $ python -m pytest -v issue2/test_morse_decode.py > issue2/result
