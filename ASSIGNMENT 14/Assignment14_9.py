class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

p1 = Product("Pen", 20)
p2 = Product("Pencil", 20)
print("Products are equal in price:" , p1 == p2)
