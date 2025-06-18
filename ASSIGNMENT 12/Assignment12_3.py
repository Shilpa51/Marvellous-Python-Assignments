class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter Value1: "))
        self.Value2 = int(input("Enter Value2: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "Division by zero not allowed"


# Creating object and calling methods
arith = Arithmetic()
arith.Accept()
print(f"Addition: {arith.Addition()}")
print(f"Subtraction: {arith.Subtraction()}")
print(f"Multiplication: {arith.Multiplication()}")
print(f"Division: {arith.Division()}")
