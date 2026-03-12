"""
Books Catalog Analysis with SQLite3 + Pandas.

Description:
- Loads `09_Pandas/data/book.json` and normalizes data into SQLite tables.
- Runs analytical queries from SQLite and prints business summaries.
- Exports result tables to CSV.

Input:
- JSON file: `09_Pandas/data/book.json`

Output:
- SQLite DB: `09_Pandas/data/books_catalog.sqlite3`
- `09_Pandas/data/exports/books_output_sqlite.csv`
- `09_Pandas/data/exports/books_author_summary_sqlite.csv`
- `09_Pandas/data/exports/books_category_summary_sqlite.csv`
"""

import json
import sqlite3
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
PANDAS_DIR = BASE_DIR.parent
DATA_DIR = PANDAS_DIR / "data"
JSON_PATH = DATA_DIR / "book.json"
DB_PATH = DATA_DIR / "books_catalog.sqlite3"
EXPORTS_DIR = DATA_DIR / "exports"


def load_json_rows(path: Path) -> tuple[dict, list[dict], list[dict]]:
    """Load catalog JSON and return metadata, authors, and books rows."""
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    catalog = data["catalog"]
    meta = {k: v for k, v in catalog.items() if k != "authors"}

    author_rows = []
    book_rows = []
    for author in catalog["authors"]:
        author_rows.append(
            {
                "author_id": author["id"],
                "writer": author["writer"],
                "nationality": author["nationality"],
            }
        )
        for book in author["books"]:
            book_rows.append(
                {
                    "book_id": book["id"],
                    "author_id": author["id"],
                    "title": book["title"],
                    "category": book["category"],
                    "year": book["year"],
                    "pages": book["pages"],
                    "edition": book["edition"],
                    "price": book["price"],
                    "available": 1 if book["available"] else 0,
                    "rating": book["rating"],
                    "tags": ", ".join(book["tags"]),
                }
            )
    return meta, author_rows, book_rows


def rebuild_schema(conn: sqlite3.Connection) -> None:
    """Recreate authors/books schema from scratch."""
    conn.executescript(
        """
        DROP TABLE IF EXISTS books;
        DROP TABLE IF EXISTS authors;

        CREATE TABLE authors (
            author_id TEXT PRIMARY KEY,
            writer TEXT NOT NULL,
            nationality TEXT NOT NULL
        );

        CREATE TABLE books (
            book_id TEXT PRIMARY KEY,
            author_id TEXT NOT NULL,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            year INTEGER NOT NULL,
            pages INTEGER NOT NULL,
            edition INTEGER NOT NULL,
            price REAL NOT NULL,
            available INTEGER NOT NULL CHECK (available IN (0, 1)),
            rating REAL NOT NULL,
            tags TEXT,
            FOREIGN KEY (author_id) REFERENCES authors(author_id)
        );
        """
    )


def seed_data(conn: sqlite3.Connection, authors: list[dict], books: list[dict]) -> None:
    """Insert normalized rows into SQLite."""
    conn.executemany(
        """
        INSERT INTO authors (author_id, writer, nationality)
        VALUES (:author_id, :writer, :nationality)
        """,
        authors,
    )
    conn.executemany(
        """
        INSERT INTO books (
            book_id, author_id, title, category, year, pages,
            edition, price, available, rating, tags
        )
        VALUES (
            :book_id, :author_id, :title, :category, :year, :pages,
            :edition, :price, :available, :rating, :tags
        )
        """,
        books,
    )
    conn.commit()


def main() -> None:
    if not JSON_PATH.exists():
        raise FileNotFoundError(f"Input file not found: {JSON_PATH}")

    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)

    meta, authors, books = load_json_rows(JSON_PATH)

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        rebuild_schema(conn)
        seed_data(conn, authors, books)

        full_df = pd.read_sql_query(
            """
            SELECT
                a.author_id,
                a.writer,
                a.nationality,
                b.book_id,
                b.title,
                b.category,
                b.year,
                b.pages,
                b.edition,
                b.price,
                b.available,
                b.rating,
                b.tags
            FROM books b
            JOIN authors a ON a.author_id = b.author_id
            ORDER BY b.book_id
            """,
            conn,
        )
        full_df["available"] = full_df["available"].astype(bool)

        available_df = pd.read_sql_query(
            """
            SELECT b.book_id, b.title, a.writer, b.price, b.rating
            FROM books b
            JOIN authors a ON a.author_id = b.author_id
            WHERE b.available = 1
            ORDER BY b.rating DESC, b.price ASC
            """,
            conn,
        )

        top_rated = pd.read_sql_query(
            """
            SELECT b.title, a.writer, b.rating, b.price
            FROM books b
            JOIN authors a ON a.author_id = b.author_id
            WHERE b.rating >= 4.5
            ORDER BY b.rating DESC, b.price ASC
            """,
            conn,
        )

        author_summary = pd.read_sql_query(
            """
            SELECT
                a.writer,
                COUNT(*) AS total_books,
                ROUND(AVG(b.price), 2) AS avg_price,
                ROUND(SUM(b.price), 2) AS total_revenue,
                ROUND(AVG(b.rating), 2) AS avg_rating,
                ROUND(AVG(b.pages), 2) AS avg_pages
            FROM books b
            JOIN authors a ON a.author_id = b.author_id
            GROUP BY a.writer
            ORDER BY a.writer
            """,
            conn,
        ).set_index("writer")

        category_summary = pd.read_sql_query(
            """
            SELECT
                category,
                COUNT(*) AS total_books,
                ROUND(AVG(price), 2) AS avg_price,
                ROUND(AVG(rating), 2) AS avg_rating
            FROM books
            GROUP BY category
            ORDER BY avg_rating DESC, category
            """,
            conn,
        ).set_index("category")

        price_extremes = pd.read_sql_query(
            """
            SELECT title, writer, price, price_rank
            FROM (
                SELECT
                    b.title,
                    a.writer,
                    b.price,
                    'most_expensive' AS price_rank
                FROM books b
                JOIN authors a ON a.author_id = b.author_id
                ORDER BY b.price DESC
                LIMIT 1
            )
            UNION ALL
            SELECT title, writer, price, price_rank
            FROM (
                SELECT
                    b.title,
                    a.writer,
                    b.price,
                    'cheapest' AS price_rank
                FROM books b
                JOIN authors a ON a.author_id = b.author_id
                ORDER BY b.price ASC
                LIMIT 1
            )
            """,
            conn,
        )

        value_df = pd.read_sql_query(
            """
            SELECT
                title,
                pages,
                price,
                ROUND(price / pages, 4) AS price_per_page
            FROM books
            ORDER BY price_per_page ASC
            """,
            conn,
        )

        per_year = pd.read_sql_query(
            """
            SELECT year, COUNT(*) AS books_published
            FROM books
            GROUP BY year
            ORDER BY year
            """,
            conn,
        ).set_index("year")

    print("=" * 60)
    print("        TECH BOOKS CATALOG - SQLITE3 + PANDAS")
    print("=" * 60)
    print(f"\nTitle      : {meta['title']}")
    print(f"Version    : {meta['version']}")
    print(f"Updated    : {meta['last_updated']}")
    print(f"Authors    : {meta['total_authors']}")
    print(f"Total books: {len(full_df)}")
    print(f"SQLite DB  : {DB_PATH}")

    print("\n" + "-" * 60)
    print("  SECTION 1 - Full Book Listing")
    print("-" * 60)
    print(full_df.to_string(index=False))

    print("\n" + "-" * 60)
    print("  SECTION 2 - Descriptive Statistics (price, pages, rating)")
    print("-" * 60)
    print(full_df[["price", "pages", "rating"]].describe().round(2))

    print("\n" + "-" * 60)
    print("  SECTION 3 - Available Books Only")
    print("-" * 60)
    print(available_df.to_string(index=False))

    print("\n" + "-" * 60)
    print("  SECTION 4 - Top Rated Books (rating >= 4.5)")
    print("-" * 60)
    print(top_rated.to_string(index=False))

    print("\n" + "-" * 60)
    print("  SECTION 5 - Summary by Author")
    print("-" * 60)
    print(author_summary.to_string())

    print("\n" + "-" * 60)
    print("  SECTION 6 - Summary by Category")
    print("-" * 60)
    print(category_summary.to_string())

    print("\n" + "-" * 60)
    print("  SECTION 7 - Price Extremes")
    print("-" * 60)
    most_expensive = price_extremes.loc[price_extremes["price_rank"] == "most_expensive"].iloc[0]
    cheapest = price_extremes.loc[price_extremes["price_rank"] == "cheapest"].iloc[0]
    print(f"  Most expensive : {most_expensive['title']} by {most_expensive['writer']} - ${most_expensive['price']:.2f}")
    print(f"  Cheapest       : {cheapest['title']} by {cheapest['writer']} - ${cheapest['price']:.2f}")

    print("\n" + "-" * 60)
    print("  SECTION 8 - Price per Page (value for money)")
    print("-" * 60)
    print(value_df.to_string(index=False))

    print("\n" + "-" * 60)
    print("  SECTION 9 - Books Published per Year")
    print("-" * 60)
    print(per_year.to_string())

    books_output_csv = EXPORTS_DIR / "books_output_sqlite.csv"
    author_summary_csv = EXPORTS_DIR / "books_author_summary_sqlite.csv"
    category_summary_csv = EXPORTS_DIR / "books_category_summary_sqlite.csv"

    full_df.to_csv(books_output_csv, index=False)
    author_summary.to_csv(author_summary_csv)
    category_summary.to_csv(category_summary_csv)

    print("\n" + "-" * 60)
    print("  CSV files exported:")
    print(f"    - {books_output_csv}")
    print(f"    - {author_summary_csv}")
    print(f"    - {category_summary_csv}")
    print("=" * 60)


if __name__ == "__main__":
    main()
