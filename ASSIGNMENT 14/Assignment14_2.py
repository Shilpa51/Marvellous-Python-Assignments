class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute(self):
        area = self.length * self.width
        perimeter = 2 * (self.length + self.width)
        print(f"Area: {area}, Perimeter: {perimeter}")

r = Rectangle(10, 5)
r.compute()
