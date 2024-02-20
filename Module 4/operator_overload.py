'''
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other):
        combined_title = f"{self.title} and {other.title}"
        combined_pages = self.pages + other.pages
        return Book(combined_title, combined_pages)
    
book1 = Book("Pyhon Basics", 200)
book2 = Book ("Advanced Python", 300)
combined_book = book1 + book2

print(f"Combined Book: {combined_book.title}, Total Pages: {combined_book.pages}")
'''

# Vectors

class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other):
        added = tuple(a + b for a,b in zip(self.components, other.components))
        return Vector(*added)
    
    def __sub__(self, other):
        substracted = tuple(a-b for a,b in zip(self.components, other.components))
        return Vector(*substracted)
    
v1 = Vector(1,2,3)
v2 = Vector(4,5,6)
v3 = v1+v2
v4 = v1-v2
print(f'Addition: {v3.components}')
print(f'Substraction: {v4.components}')