class Vehicle:
    def start(self):
        print("Vehicle starting...")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car starting with engine sound...")

c = Car()
c.start()
