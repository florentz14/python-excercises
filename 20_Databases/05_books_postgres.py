"""
Loading and writing data with PostgreSQL.

Driver: psycopg2
Install: pip install psycopg2-binary
"""

import os

import psycopg2
from dotenv import load_dotenv
from psycopg2 import OperationalError

# -------------------------------------------------------------
#  LOADING AND WRITING DATA WITH PostgreSQL
#  CONNECTION SETTINGS - loaded from .env
# -------------------------------------------------------------

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": int(os.getenv("POSTGRES_PORT", "5432")),
    "dbname": os.getenv("POSTGRES_DB", "books_db"),
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD", ""),
}


# -------------------------------------------------------------
#  HELPER - pretty table printer
# -------------------------------------------------------------
def print_rows(rows, headers):
    """Print query results as a formatted table."""
    col_widths = [
        max(len(str(h)), max((len(str(r[i])) for r in rows), default=0))
        for i, h in enumerate(headers)
    ]
    sep = "  " + "  ".join("-" * w for w in col_widths)
    header_line = "  " + "  ".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers))
    print(header_line)
    print(sep)
    for row in rows:
        print("  " + "  ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(headers))))


# -------------------------------------------------------------
#  1. CONNECT
# -------------------------------------------------------------

print("=" * 62)
print("      LOADING AND WRITING DATA WITH POSTGRESQL")
print("=" * 62)

try:
    connection = psycopg2.connect(**DB_CONFIG)
    connection.autocommit = False
    cursor = connection.cursor()
    print(f"\nConnected to PostgreSQL -> database: '{DB_CONFIG['dbname']}'")
    print(f"Host: {DB_CONFIG['host']}:{DB_CONFIG['port']} | User: {DB_CONFIG['user']}")

except OperationalError as error:
    print(f"\nConnection failed: {error}")
    print("\nMake sure PostgreSQL is running and your .env variables are correct.")
    print("You can create the database with:")
    print('  psql -U postgres -c "CREATE DATABASE books_db;"')
    raise SystemExit(1)

# -------------------------------------------------------------
#  2. DROP + CREATE TABLES (fresh start on every run)
# -------------------------------------------------------------

cursor.execute("DROP TABLE IF EXISTS books CASCADE")
cursor.execute("DROP TABLE IF EXISTS authors CASCADE")

cursor.execute(
    """
    CREATE TABLE authors (
        id          VARCHAR(10)  PRIMARY KEY,
        writer      VARCHAR(100) NOT NULL,
        nationality VARCHAR(50),
        language    VARCHAR(50)
    )
"""
)

cursor.execute(
    """
    CREATE TABLE books (
        id          VARCHAR(10)  PRIMARY KEY,
        author_id   VARCHAR(10)  NOT NULL REFERENCES authors(id),
        title       VARCHAR(200) NOT NULL,
        category    VARCHAR(100),
        year        SMALLINT,
        pages       SMALLINT,
        edition     SMALLINT,
        price       NUMERIC(8,2),
        available   BOOLEAN      DEFAULT TRUE,
        rating      NUMERIC(3,1)
    )
"""
)

connection.commit()
print("\nTables created: 'authors', 'books'")

# -------------------------------------------------------------
#  3. WRITE DATA - INSERT
# -------------------------------------------------------------

authors_data = [
    ("A001", "Mark Ross", "USA", "English"),
    ("A002", "Barbara Bracket", "UK", "English"),
    ("A003", "Carlos Nguyen", "Canada", "English"),
    ("A004", "Sophie Muller", "Germany", "English"),
]

books_data = [
    ("B001", "A001", "XML Cookbook", "Markup Languages", 2018, 320, 2, 23.56, True, 4.2),
    ("B002", "A001", "Python Fundamentals", "Programming", 2020, 480, 3, 50.70, True, 4.8),
    ("B003", "A001", "The NumPy Library", "Data Science", 2021, 270, 1, 12.30, True, 4.5),
    ("B004", "A002", "Java Enterprise", "Programming", 2019, 560, 4, 28.60, True, 4.6),
    ("B005", "A002", "HTML5", "Web Development", 2020, 390, 2, 31.35, True, 4.3),
    ("B006", "A002", "Python for Dummies", "Programming", 2022, 430, 1, 28.00, False, 4.1),
    ("B007", "A003", "SQL Mastery", "Databases", 2021, 410, 2, 35.00, True, 4.7),
    ("B008", "A003", "Introduction to Cloud Computing", "Cloud", 2023, 500, 1, 45.90, True, 4.4),
    ("B009", "A004", "Machine Learning Essentials", "Artificial Intelligence", 2022, 620, 1, 59.99, True, 4.9),
    ("B010", "A004", "Deep Learning with Python", "Artificial Intelligence", 2023, 540, 1, 55.00, True, 4.8),
]

cursor.executemany("INSERT INTO authors VALUES (%s, %s, %s, %s)", authors_data)
cursor.executemany(
    "INSERT INTO books VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    books_data,
)
connection.commit()
print(f"Inserted {len(authors_data)} authors and {len(books_data)} books")

# -------------------------------------------------------------
#  4. READ - SELECT all books
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 1 - All Books")
print("-" * 62)

cursor.execute(
    """
    SELECT id, title, category, year, price::FLOAT, rating::FLOAT
    FROM books
    ORDER BY id
"""
)
rows = cursor.fetchall()
print_rows(rows, ["ID", "Title", "Category", "Year", "Price", "Rating"])

# -------------------------------------------------------------
#  5. READ - JOIN authors + books
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 2 - Books with Author (INNER JOIN)")
print("-" * 62)

cursor.execute(
    """
    SELECT a.writer, b.title, b.price::FLOAT, b.rating::FLOAT
    FROM books b
    INNER JOIN authors a ON b.author_id = a.id
    ORDER BY a.writer, b.title
"""
)
rows = cursor.fetchall()
print_rows(rows, ["Author", "Title", "Price", "Rating"])

# -------------------------------------------------------------
#  6. FILTER - WHERE clause
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 3 - Available Books with Rating >= 4.5 (WHERE)")
print("-" * 62)

cursor.execute(
    """
    SELECT title, price::FLOAT, rating::FLOAT
    FROM books
    WHERE available = TRUE AND rating >= 4.5
    ORDER BY rating DESC
"""
)
rows = cursor.fetchall()
print_rows(rows, ["Title", "Price", "Rating"])

# -------------------------------------------------------------
#  7. AGGREGATE - GROUP BY category
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 4 - Stats by Category (GROUP BY + AVG + COUNT)")
print("-" * 62)

cursor.execute(
    """
    SELECT   category,
             COUNT(*)                      AS total_books,
             ROUND(AVG(price),  2)::FLOAT AS avg_price,
             ROUND(AVG(rating), 2)::FLOAT AS avg_rating
    FROM     books
    GROUP BY category
    ORDER BY avg_rating DESC
"""
)
rows = cursor.fetchall()
print_rows(rows, ["Category", "Books", "Avg Price", "Avg Rating"])

# -------------------------------------------------------------
#  8. UPDATE - modify a record
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 5 - UPDATE: mark 'Python for Dummies' as available")
print("-" * 62)

cursor.execute("SELECT title, available FROM books WHERE id = %s", ("B006",))
before = cursor.fetchone()
print(f"  Before -> title: {before[0]}, available: {before[1]}")

cursor.execute("UPDATE books SET available = TRUE WHERE id = %s", ("B006",))
connection.commit()

cursor.execute("SELECT title, available FROM books WHERE id = %s", ("B006",))
after = cursor.fetchone()
print(f"  After  -> title: {after[0]}, available: {after[1]}")

# -------------------------------------------------------------
#  9. DELETE - remove a record
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 6 - DELETE: remove book B001")
print("-" * 62)

cursor.execute("SELECT COUNT(*) FROM books")
before_count = cursor.fetchone()[0]

cursor.execute("DELETE FROM books WHERE id = %s", ("B001",))
connection.commit()

cursor.execute("SELECT COUNT(*) FROM books")
after_count = cursor.fetchone()[0]

print(f"  Books before DELETE : {before_count}")
print(f"  Books after  DELETE : {after_count}")

# -------------------------------------------------------------
#  10. TRANSACTION - ROLLBACK example
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 7 - TRANSACTION with ROLLBACK")
print("-" * 62)

try:
    cursor.execute("UPDATE books SET price = price * 1.10")
    cursor.execute("SELECT COUNT(*) FROM books WHERE id = 'INVALID'")
    result = cursor.fetchone()
    if result[0] == 0:
        raise ValueError("Simulated error - rolling back transaction.")
    connection.commit()

except ValueError as error:
    connection.rollback()
    print(f"  Error: {error}")
    print("  Transaction rolled back - prices unchanged.")

# -------------------------------------------------------------
#  11. POSTGRESQL-SPECIFIC - server version & metadata
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 8 - PostgreSQL Server Info & Table Metadata")
print("-" * 62)

cursor.execute("SELECT version()")
pg_version = cursor.fetchone()[0]
print(f"  Server : {pg_version[:60]}...")

cursor.execute(
    """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
    ORDER BY table_name
"""
)
tables = [row[0] for row in cursor.fetchall()]
print(f"  Tables : {tables}")

for table in tables:
    cursor.execute(
        """
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = %s
        ORDER BY ordinal_position
    """,
        (table,),
    )
    columns = cursor.fetchall()
    col_str = ", ".join(f"{col[0]} ({col[1]})" for col in columns)
    print(f"\n  '{table}' columns:")
    print(f"    {col_str}")

# -------------------------------------------------------------
#  12. CLOSE
# -------------------------------------------------------------

cursor.close()
connection.close()
print("\nConnection closed.")
print("=" * 62)
