import unittest

from romanize import romanize


class RomanizeTestCase(unittest.TestCase):

    def test_romanize_when_input_is_3_returns_III(self):
        self.assertEqual(romanize(3), 'III')

    def test_romanize_when_input_is_4_returns_IV(self):
        pass

    def test_romanize_when_input_is_9_returns_IX(self):
        pass

    def test_romanize_when_input_is_58_returns_LVIII(self):
        pass

    def test_romanize_when_input_is_1994_returns_MCMXCIV(self):
        pass


if __name__ == '__main__':
    unittest.main()
