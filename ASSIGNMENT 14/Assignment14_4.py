class Student:
    school_name = "ABC School"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, School: {Student.school_name}")

s = Student("Ankit", 23)
s.display()
Student.school_name = "XYZ School"
s.display()
