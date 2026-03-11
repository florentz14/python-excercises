"""
Pandas + SQLAlchemy unified database interface demo.

Uses SQLite as default backend, but the same Pandas/SQLAlchemy workflow can
be reused for PostgreSQL, MySQL, Oracle, and SQL Server by changing the URL.
"""

import json
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, inspect, text

# -------------------------------------------------------------
#  PANDAS + SQLAlchemy - Unified DB Interface
# -------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
JSON_PATH = PROJECT_ROOT / "09_Pandas" / "data" / "book.json"
DB_PATH = BASE_DIR / "books_sqlalchemy.db"

print("=" * 62)
print("   PANDAS + SQLALCHEMY - Unified DB Interface (SQLite demo)")
print("=" * 62)

# -------------------------------------------------------------
#  1. CREATE ENGINE
# -------------------------------------------------------------

engine = create_engine(f"sqlite:///{DB_PATH}")
print(f"\nEngine created  : {engine}")
print(f"Dialect         : {engine.dialect.name}")
print(f"Driver          : {engine.dialect.driver}")

# -------------------------------------------------------------
#  2. LOAD JSON -> build flat DataFrame
# -------------------------------------------------------------

with JSON_PATH.open("r", encoding="utf-8") as file:
    data = json.load(file)

rows = []
for author in data["catalog"]["authors"]:
    for book in author["books"]:
        rows.append(
            {
                "book_id": book["id"],
                "author_id": author["id"],
                "writer": author["writer"],
                "nationality": author["nationality"],
                "title": book["title"],
                "category": book["category"],
                "year": book["year"],
                "pages": book["pages"],
                "edition": book["edition"],
                "price": book["price"],
                "available": book["available"],
                "rating": book["rating"],
                "tags": ", ".join(book["tags"]),
            }
        )

df_books = pd.DataFrame(rows)
df_authors = df_books[["author_id", "writer", "nationality"]].drop_duplicates().reset_index(drop=True)

print(f"\nJSON loaded -> {len(df_books)} books, {len(df_authors)} authors")

# -------------------------------------------------------------
#  3. WRITE -> DataFrame to SQL (to_sql)
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 1 - Writing DataFrames to SQL (to_sql)")
print("-" * 62)

with engine.begin() as conn:
    df_authors.to_sql("authors", conn, if_exists="replace", index=False)
    df_books.to_sql("books", conn, if_exists="replace", index=False)

print("Table 'authors' written")
print("Table 'books'   written")

# -------------------------------------------------------------
#  4. READ -> SQL to DataFrame (read_sql)
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 2 - Reading SQL into DataFrame (read_sql)")
print("-" * 62)

with engine.connect() as conn:
    df_all = pd.read_sql("SELECT * FROM books", conn)

print(df_all[["book_id", "title", "category", "year", "price", "rating"]].to_string(index=False))

# -------------------------------------------------------------
#  5. READ with WHERE
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 3 - Filtered Query (WHERE rating >= 4.5)")
print("-" * 62)

query = """
    SELECT title, writer, price, rating
    FROM books
    WHERE available = 1 AND rating >= 4.5
    ORDER BY rating DESC
"""
with engine.connect() as conn:
    df_top = pd.read_sql(query, conn)

print(df_top.to_string(index=False))

# -------------------------------------------------------------
#  6. READ with GROUP BY
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 4 - Aggregated Query (GROUP BY category)")
print("-" * 62)

query = """
    SELECT   category,
             COUNT(*)              AS total_books,
             ROUND(AVG(price), 2)  AS avg_price,
             ROUND(AVG(rating), 2) AS avg_rating
    FROM books
    GROUP BY category
    ORDER BY avg_rating DESC
"""
with engine.connect() as conn:
    df_cat = pd.read_sql(query, conn)

print(df_cat.to_string(index=False))

# -------------------------------------------------------------
#  7. READ with parameterized query
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 5 - Parameterized Query (safe placeholder)")
print("-" * 62)

target_category = "Programming"
query = text("SELECT title, price, rating FROM books WHERE category = :cat ORDER BY rating DESC")

with engine.connect() as conn:
    df_param = pd.read_sql(query, conn, params={"cat": target_category})

print(f"Category filter: '{target_category}'")
print(df_param.to_string(index=False))

# -------------------------------------------------------------
#  8. UPDATE via raw SQL + engine
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 6 - UPDATE via engine.begin()")
print("-" * 62)

with engine.connect() as conn:
    row = conn.execute(text("SELECT title, available FROM books WHERE book_id = 'B006'")).fetchone()
    print(f"Before -> {row[0]}, available: {bool(row[1])}")

with engine.begin() as conn:
    conn.execute(text("UPDATE books SET available = 1 WHERE book_id = 'B006'"))

with engine.connect() as conn:
    row = conn.execute(text("SELECT title, available FROM books WHERE book_id = 'B006'")).fetchone()
    print(f"After  -> {row[0]}, available: {bool(row[1])}")

# -------------------------------------------------------------
#  9. PANDAS OPERATIONS on loaded DataFrame
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 7 - Pandas Analysis on SQL Data")
print("-" * 62)

with engine.connect() as conn:
    df = pd.read_sql("SELECT * FROM books", conn)

df["price_per_page"] = (df["price"] / df["pages"]).round(4)

print("\nDescriptive statistics:")
print(df[["price", "pages", "rating"]].describe().round(2))

print("\nAuthor revenue summary:")
author_stats = df.groupby("writer").agg(
    books=("title", "count"),
    total_revenue=("price", "sum"),
    avg_rating=("rating", "mean"),
).round(2)
print(author_stats.to_string())

print("\nBest value book (lowest price_per_page):")
best = df.loc[df["price_per_page"].idxmin(), ["title", "pages", "price", "price_per_page"]]
print(f"-> {best['title']} | {best['pages']} pages | ${best['price']} | ${best['price_per_page']}/page")

# -------------------------------------------------------------
#  10. INSPECT - DB metadata via SQLAlchemy inspector
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 8 - Database Metadata (SQLAlchemy Inspector)")
print("-" * 62)

inspector = inspect(engine)
tables = inspector.get_table_names()
print(f"Tables : {tables}")

for table in tables:
    cols = inspector.get_columns(table)
    col_info = ", ".join(f"{col['name']} ({col['type']})" for col in cols)
    print(f"\n'{table}':")
    print(f"  {col_info}")

# -------------------------------------------------------------
#  11. EXPORT - write results back to SQL table
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 9 - Export analysis result to new SQL table")
print("-" * 62)

with engine.begin() as conn:
    author_stats.reset_index().to_sql("author_stats", conn, if_exists="replace", index=False)

print("Table 'author_stats' created from Pandas aggregation")

with engine.connect() as conn:
    df_stats = pd.read_sql("SELECT * FROM author_stats", conn)
print(df_stats.to_string(index=False))

# -------------------------------------------------------------
#  DONE
# -------------------------------------------------------------

engine.dispose()
print("\nEngine disposed - all connections closed.")
print("=" * 62)
