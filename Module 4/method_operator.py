#For method overloading, create an area method that can calculate the area based on different sets of parameters.
#For operator overloading, implement the add method to add two Rectangle objects, combining their areas.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self, *args):
        if len(args) == 0:
            return self.length * self.breadth
        
        return args[0] * args[1]
    
    def __add__(self, other):
        combined_area = self.area() + other.area()
        return combined_area
    

rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(3, 7)

print(f"Area of rectangle1: {rectangle1.area()}")
print(f"Area of rectangle2: {rectangle2.area()}")

total_area = rectangle1 + rectangle2
print(f"Total combined area: {total_area}")