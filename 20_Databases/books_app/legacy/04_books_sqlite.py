"""
Loading and writing data with SQLite3.

Uses Python's built-in sqlite3 driver (no installation needed).
The database is embedded and stored in a single local file.
"""

import sqlite3
from pathlib import Path

# -------------------------------------------------------------
#  LOADING AND WRITING DATA WITH SQLite3
# -------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "Data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_FILE = DATA_DIR / "books_catalog.db"

# Remove existing DB to start fresh on every run.
if DB_FILE.exists():
    DB_FILE.unlink()

# -------------------------------------------------------------
#  1. CONNECT - creates the .db file if it does not exist
# -------------------------------------------------------------

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
print("=" * 60)
print("       LOADING AND WRITING DATA WITH SQLITE3")
print("=" * 60)
print(f"\nConnected to database: '{DB_FILE}'")

# -------------------------------------------------------------
#  2. CREATE TABLES
# -------------------------------------------------------------

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS authors (
        id          TEXT PRIMARY KEY,
        writer      TEXT NOT NULL,
        nationality TEXT,
        language    TEXT
    )
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS books (
        id          TEXT PRIMARY KEY,
        author_id   TEXT NOT NULL,
        title       TEXT NOT NULL,
        category    TEXT,
        year        INTEGER,
        pages       INTEGER,
        edition     INTEGER,
        price       REAL,
        available   INTEGER,   -- 1 = True, 0 = False
        rating      REAL,
        FOREIGN KEY (author_id) REFERENCES authors(id)
    )
"""
)

connection.commit()
print("\nTables created: 'authors', 'books'")

# -------------------------------------------------------------
#  3. WRITE DATA - INSERT rows
# -------------------------------------------------------------

authors_data = [
    ("A001", "Mark Ross", "USA", "English"),
    ("A002", "Barbara Bracket", "UK", "English"),
    ("A003", "Carlos Nguyen", "Canada", "English"),
    ("A004", "Sophie Muller", "Germany", "English"),
]

books_data = [
    ("B001", "A001", "XML Cookbook", "Markup Languages", 2018, 320, 2, 23.56, 1, 4.2),
    ("B002", "A001", "Python Fundamentals", "Programming", 2020, 480, 3, 50.70, 1, 4.8),
    ("B003", "A001", "The NumPy Library", "Data Science", 2021, 270, 1, 12.30, 1, 4.5),
    ("B004", "A002", "Java Enterprise", "Programming", 2019, 560, 4, 28.60, 1, 4.6),
    ("B005", "A002", "HTML5", "Web Development", 2020, 390, 2, 31.35, 1, 4.3),
    ("B006", "A002", "Python for Dummies", "Programming", 2022, 430, 1, 28.00, 0, 4.1),
    ("B007", "A003", "SQL Mastery", "Databases", 2021, 410, 2, 35.00, 1, 4.7),
    ("B008", "A003", "Introduction to Cloud Computing", "Cloud", 2023, 500, 1, 45.90, 1, 4.4),
    ("B009", "A004", "Machine Learning Essentials", "Artificial Intelligence", 2022, 620, 1, 59.99, 1, 4.9),
    ("B010", "A004", "Deep Learning with Python", "Artificial Intelligence", 2023, 540, 1, 55.00, 1, 4.8),
]

cursor.executemany("INSERT INTO authors VALUES (?, ?, ?, ?)", authors_data)
cursor.executemany("INSERT INTO books   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", books_data)
connection.commit()
print(f"Inserted {len(authors_data)} authors and {len(books_data)} books")

# -------------------------------------------------------------
#  4. READ - SELECT all books
# -------------------------------------------------------------

print("\n" + "-" * 60)
print("  SECTION 1 - All Books")
print("-" * 60)

cursor.execute("SELECT id, title, category, year, price, rating FROM books")
rows = cursor.fetchall()

print(f"  {'ID':<6} {'Title':<35} {'Category':<25} {'Year'} {'Price':>7} {'Rating':>6}")
print(f"  {'-'*6} {'-'*35} {'-'*25} {'-'*4} {'-'*7} {'-'*6}")
for row in rows:
    print(f"  {row[0]:<6} {row[1]:<35} {row[2]:<25} {row[3]} {row[4]:>7.2f} {row[5]:>6.1f}")

# -------------------------------------------------------------
#  5. READ - JOIN authors + books
# -------------------------------------------------------------

print("\n" + "-" * 60)
print("  SECTION 2 - Books with Author (JOIN)")
print("-" * 60)

cursor.execute(
    """
    SELECT a.writer, b.title, b.price, b.rating
    FROM books b
    JOIN authors a ON b.author_id = a.id
    ORDER BY a.writer
"""
)

rows = cursor.fetchall()
print(f"  {'Author':<20} {'Title':<35} {'Price':>7} {'Rating':>6}")
print(f"  {'-'*20} {'-'*35} {'-'*7} {'-'*6}")
for row in rows:
    print(f"  {row[0]:<20} {row[1]:<35} {row[2]:>7.2f} {row[3]:>6.1f}")

# -------------------------------------------------------------
#  6. FILTER - WHERE clause
# -------------------------------------------------------------

print("\n" + "-" * 60)
print("  SECTION 3 - Available Books with Rating >= 4.5 (WHERE)")
print("-" * 60)

cursor.execute(
    """
    SELECT title, price, rating
    FROM books
    WHERE available = 1 AND rating >= 4.5
    ORDER BY rating DESC
"""
)

rows = cursor.fetchall()
for row in rows:
    print(f"  {row[0]:<35} ${row[1]:>6.2f}  rating: {row[2]}")

# -------------------------------------------------------------
#  7. AGGREGATE - GROUP BY category
# -------------------------------------------------------------

print("\n" + "-" * 60)
print("  SECTION 4 - Stats by Category (GROUP BY + AVG + COUNT)")
print("-" * 60)

cursor.execute(
    """
    SELECT   category,
             COUNT(*)        AS total_books,
             ROUND(AVG(price),  2) AS avg_price,
             ROUND(AVG(rating), 2) AS avg_rating
    FROM     books
    GROUP BY category
    ORDER BY avg_rating DESC
"""
)

rows = cursor.fetchall()
print(f"  {'Category':<25} {'Books':>6} {'Avg Price':>10} {'Avg Rating':>11}")
print(f"  {'-'*25} {'-'*6} {'-'*10} {'-'*11}")
for row in rows:
    print(f"  {row[0]:<25} {row[1]:>6} {row[2]:>10.2f} {row[3]:>11.2f}")

# -------------------------------------------------------------
#  8. UPDATE - modify a record
# -------------------------------------------------------------

print("\n" + "-" * 60)
print("  SECTION 5 - UPDATE: mark 'Python for Dummies' as available")
print("-" * 60)

cursor.execute("SELECT title, available FROM books WHERE id = 'B006'")
before = cursor.fetchone()
print(f"  Before -> title: {before[0]}, available: {bool(before[1])}")

cursor.execute("UPDATE books SET available = 1 WHERE id = 'B006'")
connection.commit()

cursor.execute("SELECT title, available FROM books WHERE id = 'B006'")
after = cursor.fetchone()
print(f"  After  -> title: {after[0]}, available: {bool(after[1])}")

# -------------------------------------------------------------
#  9. DELETE - remove a record
# -------------------------------------------------------------

print("\n" + "-" * 60)
print("  SECTION 6 - DELETE: remove book B001")
print("-" * 60)

cursor.execute("SELECT COUNT(*) FROM books")
before_count = cursor.fetchone()[0]

cursor.execute("DELETE FROM books WHERE id = 'B001'")
connection.commit()

cursor.execute("SELECT COUNT(*) FROM books")
after_count = cursor.fetchone()[0]

print(f"  Books before DELETE : {before_count}")
print(f"  Books after  DELETE : {after_count}")

# -------------------------------------------------------------
#  10. DATABASE METADATA
# -------------------------------------------------------------

print("\n" + "-" * 60)
print("  SECTION 7 - Database Metadata")
print("-" * 60)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print(f"  Tables in database: {[t[0] for t in tables]}")

for table_name in [t[0] for t in tables]:
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    col_names = [col[1] for col in columns]
    print(f"  '{table_name}' columns: {col_names}")

db_size = DB_FILE.stat().st_size
print(f"\n  Database file : {DB_FILE}")
print(f"  File size     : {db_size} bytes")

# -------------------------------------------------------------
#  11. CLOSE CONNECTION
# -------------------------------------------------------------

connection.close()
print("\nConnection closed.")
print("=" * 60)
