class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Coordinate: ({self.x} {self.y})"
    
point1 = Coordinate(1,2)
point2 = Coordinate(2,3)
point3 = point1 + point2

print(point3)