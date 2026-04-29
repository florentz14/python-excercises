import sqlite3

# --- Data sets ---

titles = [
    (1, "The Hunger Games"),
    (2, "The Great Gatsby"),
    (3, "The Maze Runner"),
    (4, "The Lord of the Rings"),
]

authors = [
    (1, "Suzanne Collins",  1974),
    (2, "F. Scott Fitzgerald", 1896),
    (3, "James Dashner",    1972),
    (4, "J.R.R. Tolkien",   1892),
]

genres = [
    (1, "Dystopian Fiction"),
    (2, "Classic Literature"),
    (3, "Science Fiction"),
    (4, "Fantasy"),
]

# book_id, author_id, genre_id, year_published, pages
books_meta = [
    (1, 1, 1, 2008, 374),
    (2, 2, 2, 1925, 180),
    (3, 3, 3, 2009, 375),
    (4, 4, 4, 1954, 1178),
]

# --- Schema ---

SCHEMA = """
CREATE TABLE IF NOT EXISTS authors (
    id      INTEGER PRIMARY KEY,
    name    TEXT    NOT NULL,
    born    INTEGER
);

CREATE TABLE IF NOT EXISTS genres (
    id      INTEGER PRIMARY KEY,
    name    TEXT    NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS books (
    id          INTEGER PRIMARY KEY,
    title       TEXT    NOT NULL,
    author_id   INTEGER REFERENCES authors(id),
    genre_id    INTEGER REFERENCES genres(id),
    published   INTEGER,
    pages       INTEGER
);
"""

# --- Queries ---

INSERT_AUTHORS = "INSERT OR IGNORE INTO authors VALUES (?, ?, ?)"
INSERT_GENRES = "INSERT OR IGNORE INTO genres  VALUES (?, ?)"
INSERT_BOOKS = """
    INSERT OR IGNORE INTO books (id, title, author_id, genre_id, published, pages)
    VALUES (?, ?, ?, ?, ?, ?)
"""

with sqlite3.connect("books.db") as conn:
    cursor = conn.cursor()

    # Enable foreign-key enforcement
    cursor.execute("PRAGMA foreign_keys = ON")

    # Create tables
    cursor.executescript(SCHEMA)

    # Batch inserts — collected, then inserted all at once
    cursor.executemany(INSERT_AUTHORS, authors)
    cursor.executemany(INSERT_GENRES,  genres)

    # Merge titles + meta before inserting books
    books_rows = [
        (meta[0], title[1], meta[1], meta[2], meta[3], meta[4])
        for title, meta in zip(titles, books_meta)
    ]
    cursor.executemany(INSERT_BOOKS, books_rows)

    conn.commit()

    # --- Read back with a JOIN ---
    cursor.execute("""
        SELECT b.id, b.title, a.name AS author, g.name AS genre, b.published, b.pages
        FROM   books   b
        JOIN   authors a ON a.id = b.author_id
        JOIN   genres  g ON g.id = b.genre_id
        ORDER  BY b.published
    """)

    print(
        f"\n{'ID':<4} {'Title':<28} {'Author':<22} {'Genre':<22} {'Year':<6} {'Pages'}")
    print("-" * 90)
    for row in cursor.fetchall():
        print(
            f"{row[0]:<4} {row[1]:<28} {row[2]:<22} {row[3]:<22} {row[4]:<6} {row[5]}")
