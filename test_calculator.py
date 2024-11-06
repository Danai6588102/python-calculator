import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    # Test cases add
    def test_add1(self):
        self.assertEqual(self.calc.add(2, 2), 4)

    def test_add2(self):
        self.assertEqual(self.calc.add(1, 6), 7)

    # Test cases subtract
    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(5, 1), 4)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)

    # Test cases multiply
    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(4, 4), 16)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(3, 3), 9)

    # Test cases divide
    def test_divide1(self):
        self.assertEqual(self.calc.divide(8, 4), 2)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(8, 8), 1)

    # Test cases mod
    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(10, 4), 2)


if __name__ == '__main__':
    unittest.main()