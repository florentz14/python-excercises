"""
Pandas + SQLAlchemy unified database interface demo.

Extended version:
- normalizes entities (publishers, tags, inventory, reviews)
- keeps SQLite as default backend
- shows reusable SQL patterns for richer analytics
"""

import json
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, inspect, text

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
JSON_PATH = PROJECT_ROOT / "09_Pandas" / "data" / "book.json"
DATA_DIR = BASE_DIR / "Data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DATA_DIR / "books_sqlalchemy.db"

print("=" * 72)
print("   PANDAS + SQLALCHEMY - EXTENDED UNIFIED DB INTERFACE (SQLite)")
print("=" * 72)

engine = create_engine(f"sqlite:///{DB_PATH}")
print(f"\nEngine created  : {engine}")
print(f"Dialect         : {engine.dialect.name}")
print(f"Driver          : {engine.dialect.driver}")

# -------------------------------------------------------------
#  1) LOAD JSON AND BUILD BASE DATAFRAMES
# -------------------------------------------------------------
with JSON_PATH.open("r", encoding="utf-8") as file:
    data = json.load(file)

publisher_by_category = {
    "Programming": "CodeMaster Press",
    "Data Science": "DataLab Books",
    "Artificial Intelligence": "FutureAI Publishing",
    "Databases": "QueryHouse Media",
    "Cloud": "CloudCore Editions",
    "Web Development": "Frontend Works",
    "Markup Languages": "Markup Studio",
}

book_rows = []
tag_rows = []
review_rows = []
inventory_rows = []

for author in data["catalog"]["authors"]:
    for book in author["books"]:
        publisher_name = publisher_by_category.get(book["category"], "General Tech Press")
        isbn = f"978-0-{int(book['id'][1:]):03d}-{book['year'] % 100:02d}-{book['edition']}"

        book_rows.append(
            {
                "book_id": book["id"],
                "author_id": author["id"],
                "writer": author["writer"],
                "nationality": author["nationality"],
                "title": book["title"],
                "category": book["category"],
                "publisher_name": publisher_name,
                "isbn": isbn,
                "year": book["year"],
                "pages": book["pages"],
                "edition": book["edition"],
                "price": float(book["price"]),
                "available": bool(book["available"]),
                "rating": float(book["rating"]),
                "created_at": "2026-01-01 00:00:00",
                "updated_at": "2026-03-11 00:00:00",
            }
        )

        for tag in book["tags"]:
            tag_rows.append({"book_id": book["id"], "tag": tag.lower().strip()})

        review_rows.append(
            {
                "book_id": book["id"],
                "reviewer": "editorial_board",
                "review_score": float(book["rating"]),
                "review_comment": f"Editorial rating for {book['title']}",
                "review_date": "2026-03-11",
            }
        )
        review_rows.append(
            {
                "book_id": book["id"],
                "reviewer": "community_pick",
                "review_score": max(1.0, min(5.0, round(float(book["rating"]) - 0.2, 1))),
                "review_comment": f"Community feedback for {book['title']}",
                "review_date": "2026-03-10",
            }
        )

        stock = 18 if book["available"] else 3
        reorder = 6
        inventory_rows.append(
            {
                "book_id": book["id"],
                "warehouse": "Main",
                "stock_qty": stock,
                "reorder_level": reorder,
                "last_restock_date": "2026-03-01",
            }
        )

df_books = pd.DataFrame(book_rows)
df_authors = df_books[["author_id", "writer", "nationality"]].drop_duplicates().reset_index(drop=True)
df_publishers = (
    df_books[["publisher_name"]]
    .drop_duplicates()
    .sort_values("publisher_name")
    .reset_index(drop=True)
    .reset_index(names="publisher_id")
)
df_publishers["publisher_id"] = df_publishers["publisher_id"] + 1

df_books = df_books.merge(df_publishers, on="publisher_name", how="left")
df_books = df_books.drop(columns=["publisher_name"])
df_tags = pd.DataFrame(tag_rows).drop_duplicates().sort_values(["book_id", "tag"]).reset_index(drop=True)
df_reviews = pd.DataFrame(review_rows)
df_inventory = pd.DataFrame(inventory_rows)

print(
    f"\nJSON loaded -> {len(df_books)} books, {len(df_authors)} authors, "
    f"{len(df_publishers)} publishers"
)

# -------------------------------------------------------------
#  2) WRITE NORMALIZED TABLES
# -------------------------------------------------------------
print("\n" + "-" * 72)
print("  SECTION 1 - Writing normalized entities to SQL")
print("-" * 72)

with engine.begin() as conn:
    df_authors.to_sql("authors", conn, if_exists="replace", index=False)
    df_publishers.to_sql("publishers", conn, if_exists="replace", index=False)
    df_books.to_sql("books", conn, if_exists="replace", index=False)
    df_inventory.to_sql("book_inventory", conn, if_exists="replace", index=False)
    df_reviews.to_sql("book_reviews", conn, if_exists="replace", index=False)
    df_tags.to_sql("book_tags", conn, if_exists="replace", index=False)

print("Tables written: authors, publishers, books, book_inventory, book_reviews, book_tags")

# -------------------------------------------------------------
#  3) READ JOINED DATA
# -------------------------------------------------------------
print("\n" + "-" * 72)
print("  SECTION 2 - Joined catalog view")
print("-" * 72)

query = """
    SELECT b.book_id, b.title, b.category, p.publisher_name, b.price, b.rating
    FROM books b
    JOIN publishers p ON p.publisher_id = b.publisher_id
    ORDER BY b.book_id
"""
with engine.connect() as conn:
    df_joined = pd.read_sql(query, conn)

print(df_joined.to_string(index=False))

# -------------------------------------------------------------
#  4) TOP-RATED BY CATEGORY
# -------------------------------------------------------------
print("\n" + "-" * 72)
print("  SECTION 3 - Top-rated books by category")
print("-" * 72)

query = """
    SELECT category, title, rating, price
    FROM (
        SELECT category, title, rating, price,
               ROW_NUMBER() OVER (PARTITION BY category ORDER BY rating DESC, price DESC) AS rn
        FROM books
    ) ranked
    WHERE rn = 1
    ORDER BY category
"""
with engine.connect() as conn:
    df_top = pd.read_sql(query, conn)

print(df_top.to_string(index=False))

# -------------------------------------------------------------
#  5) INVENTORY HEALTH
# -------------------------------------------------------------
print("\n" + "-" * 72)
print("  SECTION 4 - Inventory health and low stock")
print("-" * 72)

query = """
    SELECT i.book_id, b.title, i.stock_qty, i.reorder_level,
           CASE WHEN i.stock_qty <= i.reorder_level THEN 1 ELSE 0 END AS low_stock
    FROM book_inventory i
    JOIN books b ON b.book_id = i.book_id
    ORDER BY low_stock DESC, i.stock_qty ASC
"""
with engine.connect() as conn:
    df_inventory_health = pd.read_sql(query, conn)

print(df_inventory_health.to_string(index=False))

# -------------------------------------------------------------
#  6) INVENTORY VALUE
# -------------------------------------------------------------
print("\n" + "-" * 72)
print("  SECTION 5 - Inventory value by category")
print("-" * 72)

query = """
    SELECT b.category,
           SUM(i.stock_qty) AS units_in_stock,
           ROUND(SUM(i.stock_qty * b.price), 2) AS inventory_value
    FROM books b
    JOIN book_inventory i ON i.book_id = b.book_id
    GROUP BY b.category
    ORDER BY inventory_value DESC
"""
with engine.connect() as conn:
    df_value = pd.read_sql(query, conn)

print(df_value.to_string(index=False))

# -------------------------------------------------------------
#  7) REVIEW METRICS
# -------------------------------------------------------------
print("\n" + "-" * 72)
print("  SECTION 6 - Review metrics")
print("-" * 72)

query = """
    SELECT b.book_id, b.title,
           ROUND(AVG(r.review_score), 2) AS avg_review_score,
           COUNT(*) AS review_count
    FROM books b
    JOIN book_reviews r ON r.book_id = b.book_id
    GROUP BY b.book_id, b.title
    ORDER BY avg_review_score DESC, review_count DESC
"""
with engine.connect() as conn:
    df_reviews_agg = pd.read_sql(query, conn)

print(df_reviews_agg.to_string(index=False))

# -------------------------------------------------------------
#  8) TAG FREQUENCY
# -------------------------------------------------------------
print("\n" + "-" * 72)
print("  SECTION 7 - Tag frequency")
print("-" * 72)

query = """
    SELECT tag, COUNT(*) AS tag_count
    FROM book_tags
    GROUP BY tag
    ORDER BY tag_count DESC, tag ASC
"""
with engine.connect() as conn:
    df_tags_freq = pd.read_sql(query, conn)

print(df_tags_freq.to_string(index=False))

# -------------------------------------------------------------
#  9) UPDATE EXAMPLE (inventory restock)
# -------------------------------------------------------------
print("\n" + "-" * 72)
print("  SECTION 8 - UPDATE example: restock one low-stock title")
print("-" * 72)

with engine.connect() as conn:
    row = conn.execute(
        text(
            """
            SELECT i.book_id, b.title, i.stock_qty
            FROM book_inventory i
            JOIN books b ON b.book_id = i.book_id
            WHERE i.stock_qty <= i.reorder_level
            ORDER BY i.stock_qty ASC
            LIMIT 1
            """
        )
    ).fetchone()

if row:
    print(f"Before restock -> {row[1]} ({row[0]}), stock: {row[2]}")
    with engine.begin() as conn:
        conn.execute(
            text("UPDATE book_inventory SET stock_qty = stock_qty + 20 WHERE book_id = :book_id"),
            {"book_id": row[0]},
        )
    with engine.connect() as conn:
        after = conn.execute(
            text(
                """
                SELECT i.book_id, b.title, i.stock_qty
                FROM book_inventory i
                JOIN books b ON b.book_id = i.book_id
                WHERE i.book_id = :book_id
                """
            ),
            {"book_id": row[0]},
        ).fetchone()
    print(f"After  restock -> {after[1]} ({after[0]}), stock: {after[2]}")
else:
    print("No low-stock titles found.")

# -------------------------------------------------------------
#  10) EXPORT BUSINESS REPORT TABLES
# -------------------------------------------------------------
print("\n" + "-" * 72)
print("  SECTION 9 - Export SQL report tables")
print("-" * 72)

category_report = df_value.copy()
publisher_report = (
    df_joined.groupby("publisher_name")
    .agg(total_books=("book_id", "count"), avg_rating=("rating", "mean"), avg_price=("price", "mean"))
    .reset_index()
    .round(2)
)

with engine.begin() as conn:
    category_report.to_sql("report_inventory_by_category", conn, if_exists="replace", index=False)
    publisher_report.to_sql("report_publisher_summary", conn, if_exists="replace", index=False)

print("Tables created: report_inventory_by_category, report_publisher_summary")

# -------------------------------------------------------------
#  11) INSPECT DATABASE METADATA
# -------------------------------------------------------------
print("\n" + "-" * 72)
print("  SECTION 10 - SQLAlchemy Inspector metadata")
print("-" * 72)

inspector = inspect(engine)
tables = sorted(inspector.get_table_names())
print(f"Tables ({len(tables)}): {tables}")

for table in tables:
    cols = inspector.get_columns(table)
    col_info = ", ".join(f"{col['name']} ({col['type']})" for col in cols)
    print(f"\n{table}:")
    print(f"  {col_info}")

engine.dispose()
print("\nEngine disposed - all connections closed.")
print("=" * 72)
