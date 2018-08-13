import unittest

from romanize import romanize


class RomanizeTestCase(unittest.TestCase):

    def test_romanize_when_input_is_3_returns_III(self):
        self.assertEqual(romanize(3), 'III')

    def test_romanize_when_input_is_4_returns_IV(self):
        self.assertEqual(romanize(4), 'IV')

    def test_romanize_when_input_is_9_returns_IX(self):
        self.assertEqual(romanize(9), 'IX')

    def test_romanize_when_input_is_58_returns_LVIII(self):
        self.assertEqual(romanize(58), 'LVIII')

    def test_romanize_when_input_is_1994_returns_MCMXCIV(self):
        self.assertEqual(romanize(1994), 'MCMXCIV')


if __name__ == '__main__':
    unittest.main()
