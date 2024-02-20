class Student:
    def __init__(self, name, age, major = "Undeclared"):
        if not isinstance(age,int) or age < 0:
            raise ValueError("Age must be a positive integer")
        if not isinstance(major, str):
            raise TypeError("Major must be a string")
        self.name = name
        self.age = age
        self.major = major

new_student = Student("John", 23, "Engineering")