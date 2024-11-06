import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(1, 6), 7)
    # Add the following test methods to the TestCalculator class:
    # Test cases subtract
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 1), 4)
        self.assertEqual(self.calc.subtract(3, 2), 1)

    # Test cases multiply
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 4), 16)
        self.assertEqual(self.calc.multiply(3, 3), 9)

    # Test cases divide
    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(8, 8), 1)

    # Test cases mod
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(10, 4), 2)

if __name__ == '__main__':
    unittest.main()