#Instance method
class MyClass:
    def instance_method(self):
        print("This is an instance method.")

#Self
        
class MyClass:
    def __init__(self, value):
        self.value = value

    def update_value(self, new_value):
        self.value = new_value

# Example
class Car:
    def __init__(self, color):
        self.color = color

    def describe(self):
        print(f"This car is {self.color}.")