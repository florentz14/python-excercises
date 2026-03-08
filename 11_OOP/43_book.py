# -------------------------------------------------
# File Name: 43_book.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Simple Book class with title, author, pages and info() method.
# -------------------------------------------------

class Book:
    """Class with several attributes."""
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        return f"{self.title} - {self.author} ({self.pages} pgs)"

# Short list of books
books = [
    Book("Don Quixote", "Cervantes", 863),
    Book("1984", "Orwell", 328),
    Book("The Hobbit", "Tolkien", 366),
]

# Usage
for b in books:
    print(b.info())
