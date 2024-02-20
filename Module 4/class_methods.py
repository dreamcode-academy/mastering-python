# @classmethod


class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books += 1

    @classmethod
    def total(cls):
        return f"There are {cls.total_books} books"
    

book1 = Book("Title1")

book2 = Book("Title2")

total_books = Book.total()

print(total_books)