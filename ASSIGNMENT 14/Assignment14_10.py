class Employee:
    def __init__(self, name, department, salary):
        self.name = name            # public
        self._department = department  # protected
        self.__salary = salary      # private

    def display(self):
        print(f"Name: {self.name}, Department: {self._department}, Salary: {self.__salary}")

e = Employee("Sneha", "HR", 55000)
e.display()
# Accessing directly
print(e.name)
print(e._department)
# print(e.__salary)  # Will raise AttributeError
print(e._Employee__salary)  # Accessing private variable using name mangling
