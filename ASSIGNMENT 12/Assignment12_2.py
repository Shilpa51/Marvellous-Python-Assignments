class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter radius of circle: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print(f"Radius = {self.Radius}")
        print(f"Area = {self.Area}")
        print(f"Circumference = {self.Circumference}")


# Creating object and calling methods
circle1 = Circle()
circle1.Accept()
circle1.CalculateArea()
circle1.CalculateCircumference()
circle1.Display()
