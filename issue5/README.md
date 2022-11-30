Шаги для запуска:
1) Запускаем mock тесты на проверку принятия дат правильного типа, и соответствия результата
> $ python -m pytest -v issue5/test_what_is_year_now.py

2) Сохраняем результаты в result
> $ python -m pytest -v issue5/test_what_is_year_now.py > issue5/result

3) Устанавливаем пакет для расчета coverage
> $ pip install -U pytest-cov

4) Переходим внутрь папки
> $ cd issue5

5) Проверяем процент покрытия кода тестами
> $ python -m pytest -q test_what_is_year_now.py --cov=what_is_year_now

5) Формируем отчет о покрытии в виде директории с html файлами
> $ python -m pytest -q test_what_is_year_now.py --cov=what_is_year_now --cov-report html

