class Book:
    def __init__ (self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Book title: {self.title}, Author: {self.author}")
    

my_book = Book("1984", "George Orwell")
my_book.title = "Animal Farm"
my_book.display_info()
