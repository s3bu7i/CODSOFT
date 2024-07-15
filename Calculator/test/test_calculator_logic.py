# test_calculator_logic.py
import unittest
from calculator_logic import CalculatorLogic


class TestCalculatorLogic(unittest.TestCase):
    def setUp(self):
        self.calc = CalculatorLogic()

    def test_addition(self):
        self.calc.add_to_expression('2')
        self.calc.add_to_expression('+')
        self.calc.add_to_expression('2')
        self.assertEqual(self.calc.evaluate(), '4')

    def test_subtraction(self):
        self.calc.add_to_expression('5')
        self.calc.add_to_expression('-')
        self.calc.add_to_expression('3')
        self.assertEqual(self.calc.evaluate(), '2')

    def test_multiplication(self):
        self.calc.add_to_expression('3')
        self.calc.add_to_expression('*')
        self.calc.add_to_expression('4')
        self.assertEqual(self.calc.evaluate(), '12')

    def test_division(self):
        self.calc.add_to_expression('12')
        self.calc.add_to_expression('/')
        self.calc.add_to_expression('4')
        self.assertEqual(self.calc.evaluate(), '3.0')

    def test_sine(self):
        self.calc.add_to_expression('sin(')
        self.calc.add_to_expression('0')
        self.calc.add_to_expression(')')
        self.assertEqual(self.calc.evaluate(), '0.0')

    def test_cosine(self):
        self.calc.add_to_expression('cos(')
        self.calc.add_to_expression('0')
        self.calc.add_to_expression(')')
        self.assertEqual(self.calc.evaluate(), '1.0')

    def test_tangent(self):
        self.calc.add_to_expression('tan(')
        self.calc.add_to_expression('0')
        self.calc.add_to_expression(')')
        self.assertEqual(self.calc.evaluate(), '0.0')

    def test_logarithm(self):
        self.calc.add_to_expression('log(')
        self.calc.add_to_expression('10')
        self.calc.add_to_expression(')')
        self.assertEqual(self.calc.evaluate(), '1.0')

    def test_square_root(self):
        self.calc.add_to_expression('sqrt(')
        self.calc.add_to_expression('16')
        self.calc.add_to_expression(')')
        self.assertEqual(self.calc.evaluate(), '4.0')

    def test_power(self):
        self.calc.add_to_expression('pow(')
        self.calc.add_to_expression('2')
        self.calc.add_to_expression(',')
        self.calc.add_to_expression('3')
        self.calc.add_to_expression(')')
        self.assertEqual(self.calc.evaluate(), '8.0')

    def test_clear(self):
        self.calc.add_to_expression('2+2')
        self.calc.clear()
        self.assertEqual(self.calc.expression, '')

    def test_invalid_expression(self):
        self.calc.add_to_expression('2/')
        self.calc.add_to_expression('0')
        self.assertEqual(self.calc.evaluate(), 'Error')


if __name__ == '__main__':
    unittest.main()
