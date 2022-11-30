import unittest
from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):
    def test_moscow(self):
        """ Проверяет правильно ли трансформируется Moscow"""
        actual = fit_transform('Moscow')
        expected = [('Moscow', [1])]
        self.assertEqual(actual, expected)

    def test_not_equal(self):
        """ Проверяет, определяет ли функция неправильный перевод
            одного из городов"""
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(cities)
        expected = [
            ('Moscow', [1, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertNotEqual(actual, expected)

    def test_not_in(self):
        """ Проверяет, находятся ли все трансформированные значения
            городов в списке правильных значений"""
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(cities)[0]
        expected = [
            ('Moscow', [1, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertIn(actual, expected)

    def test_empty(self):
        """ Проверяет правильность вывода при обработке
            пустой строки"""
        self.assertEqual(fit_transform(''), [('', [1])])

    def test_error_raise(self):
        """ Перехват исключения при отсутствии аргумента"""
        with self.assertRaises(Exception):
            fit_transform()


if __name__ == '__main__':
    unittest.main()
