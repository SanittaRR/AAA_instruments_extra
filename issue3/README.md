Шаги для запуска:

1) Запускаем класс со всеми тестами
Проверяются 4 теста, среди которых `assertEqual`, `assertIn`, `assertNotEqual`, 
а также пример с перехватом ошибки (`assertRaises`)
> $ python -m unittest issue3/test_one_hot_encoder.py

2) Передаем в result
> $ python -m unittest issue3/test_one_hot_encoder.py > issue3/result

П.с. 
3) Так как данный код, при прохождении всех тестов ничего не выводит в result,
для наглядности выполнения тестов, используется следующий код
> $ python -m pytest -v issue3/test_one_hot_encoder.py > issue3/result
