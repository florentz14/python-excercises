# 16_simple_libro.py - Simple class: Book
# Florentino Baez - ITSE-1002

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
