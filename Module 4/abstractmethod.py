"""
#     @abstractmethod




class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2


my_circle = Circle(5)
print(f"The area of the circle is: {my_circle.area()}")
'''
try:
    my_shape = Shape()
except TypeError as e:
    print(f"Error: {e}")
'''
