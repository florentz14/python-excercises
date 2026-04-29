from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Author:
    id: str
    writer: str
    nationality: str
    language: str


@dataclass
class Book:
    id: str
    author_id: str
    title: str
    category: str
    year: int
    pages: int
    edition: int
    price: float
    available: bool
    rating: float
