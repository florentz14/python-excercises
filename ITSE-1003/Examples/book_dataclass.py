# -------------------------------------------------
# File Name: ITSE-1003/Examples/book_dataclass.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Dataclass basics.
# -------------------------------------------------

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int

    def short_description(self) -> str:
        return f"{self.title} by {self.author} ({self.pages} pages)"


def main() -> None:
    book = Book("Clean Code", "Robert C. Martin", 464)
    print(book)
    print(book.short_description())


if __name__ == "__main__":
    main()
