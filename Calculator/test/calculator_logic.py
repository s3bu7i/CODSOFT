# calculator_logic.py
import math


class CalculatorLogic:
    def __init__(self):
        self.expression = ""

    def clear(self):
        self.expression = ""
        return self.expression

    def add_to_expression(self, value):
        self.expression += str(value)
        return self.expression

    def evaluate(self):
        try:
            self.expression = self.expression.replace('sin', 'math.sin')
            self.expression = self.expression.replace('cos', 'math.cos')
            self.expression = self.expression.replace('tan', 'math.tan')
            self.expression = self.expression.replace('log', 'math.log10')
            self.expression = self.expression.replace('sqrt', 'math.sqrt')
            self.expression = self.expression.replace('pow', 'math.pow')

            result = str(eval(self.expression))
            self.expression = result
            return result
        except Exception as e:
            self.expression = ""
            return "Error"
