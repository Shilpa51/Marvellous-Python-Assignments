class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        return "Cannot divide by zero"

calc = Calculator()
x, y = 20, 10
print("Add:", calc.add(x, y))
print("Subtract:", calc.subtract(x, y))
print("Multiply:", calc.multiply(x, y))
print("Divide:", calc.divide(x, y))
