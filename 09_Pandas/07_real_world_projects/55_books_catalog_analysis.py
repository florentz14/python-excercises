"""
Books Catalog Analysis with Pandas.

Description:
- Loads `data/book.json` and flattens nested author/book data into a DataFrame.
- Prints catalog metadata, filters, group summaries, and basic statistics.
- Exports CSV outputs for full data and aggregated summaries.

Input:
- JSON file: `09_Pandas/data/book.json`

Output:
- `09_Pandas/data/exports/books_output.csv`
- `09_Pandas/data/exports/books_author_summary.csv`
- `09_Pandas/data/exports/books_category_summary.csv`

Run:
- python 09_Pandas/07_real_world_projects/55_books_catalog_analysis.py
"""

import json
from pathlib import Path

import pandas as pd

# ---------------------------------------------
#  1. LOAD AND FLATTEN JSON
# ---------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR / "data" / "book.json"

# Read the JSON file
with JSON_PATH.open("r", encoding="utf-8") as f:
    data = json.load(f)

# Extract catalog information
catalog_info = {k: v for k, v in data["catalog"].items() if k != "authors"}

# Extract the authors information
authors_raw = data["catalog"]["authors"]

# Flatten the data: one row per book, keeping author fields
rows = []
# Loop through each author and their books
for author in authors_raw:
    # Loop through each book of the author
    for book in author["books"]:
        # Append the book information to the rows list
        rows.append(
            {
                "author_id": author["id"],
                "writer": author["writer"],
                "nationality": author["nationality"],
                "book_id": book["id"],
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

# Create the DataFrame
df = pd.DataFrame(rows)

# ---------------------------------------------
#  2. CATALOG METADATA
# ---------------------------------------------

# Print the catalog metadata
print("=" * 60)
print("          TECH BOOKS CATALOG - PANDAS ANALYSIS")
print("=" * 60)
print(f"\nTitle      : {catalog_info['title']}")
print(f"Version    : {catalog_info['version']}")
print(f"Updated    : {catalog_info['last_updated']}")
print(f"Authors    : {catalog_info['total_authors']}")
print(f"Total books: {len(df)}")

# ---------------------------------------------
#  3. FULL DATAFRAME
# ---------------------------------------------

print("\n" + "-" * 60)
print("  SECTION 1 - Full Book Listing")
print("-" * 60)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)
pd.set_option("display.max_colwidth", 30)
print(df.to_string(index=False))

# ---------------------------------------------
#  4. DESCRIPTIVE STATISTICS
# ---------------------------------------------

print("\n" + "-" * 60)
print("  SECTION 2 - Descriptive Statistics (price, pages, rating)")
print("-" * 60)
print(df[["price", "pages", "rating"]].describe().round(2))

# ---------------------------------------------
#  5. FILTER: AVAILABLE BOOKS ONLY
# ---------------------------------------------

print("\n" + "-" * 60)
print("  SECTION 3 - Available Books Only")
print("-" * 60)
available_df = pd.DataFrame(
    df[df["available"] == True].loc[:, ["book_id", "title", "writer", "price", "rating"]]
)
print(available_df.to_string(index=False))

# ---------------------------------------------
#  6. FILTER: BOOKS RATED >= 4.5
# ---------------------------------------------

print("\n" + "-" * 60)
print("  SECTION 4 - Top Rated Books (rating >= 4.5)")
print("-" * 60)
# Filter the books rated >= 4.5 and sort by rating in descending order
top_rated = pd.DataFrame(
    df[df["rating"] >= 4.5].loc[:, ["title", "writer", "rating", "price"]]
)
top_rated_rows = sorted(
    top_rated.itertuples(index=False),
    key=lambda row: float(row[2]),
    reverse=True,
)
top_rated = pd.DataFrame(top_rated_rows, columns=["title", "writer", "rating", "price"])
# Print the top rated books
print(top_rated.to_string(index=False))

# ---------------------------------------------
#  7. GROUP BY AUTHOR
# ---------------------------------------------

print("\n" + "-" * 60)
print("  SECTION 5 - Summary by Author")
print("-" * 60)
# Group by author and calculate the summary statistics
author_summary = (
    df.groupby("writer")
    .agg(
        total_books=("title", "count"),
        avg_price=("price", "mean"),
        total_revenue=("price", "sum"),
        avg_rating=("rating", "mean"),
        avg_pages=("pages", "mean"),
    )
    .round(2)
)
# Print the author summary
print(author_summary.to_string())

# ---------------------------------------------
#  8. GROUP BY CATEGORY
# ---------------------------------------------

print("\n" + "-" * 60)
print("  SECTION 6 - Summary by Category")
print("-" * 60)
# Group by category and calculate the summary statistics
category_summary = pd.DataFrame(
    df.groupby("category", as_index=False).agg(
        total_books=("title", "count"),
        avg_price=("price", "mean"),
        avg_rating=("rating", "mean"),
    )
).round(2)
category_rows = sorted(
    category_summary.itertuples(index=False),
    key=lambda row: float(row[3]),
    reverse=True,
)
category_summary = pd.DataFrame(
    category_rows, columns=["category", "total_books", "avg_price", "avg_rating"]
)
# Print the category summary
print(category_summary.set_index("category").to_string())

# ---------------------------------------------
#  9. MOST EXPENSIVE & CHEAPEST BOOK
# ---------------------------------------------

print("\n" + "-" * 60)
print("  SECTION 7 - Price Extremes")
print("-" * 60)
# Find the most expensive and cheapest books
most_expensive = df.loc[df["price"].idxmax(), ["title", "writer", "price"]]
cheapest = df.loc[df["price"].idxmin(), ["title", "writer", "price"]]
print(f"  Most expensive : {most_expensive['title']} by {most_expensive['writer']} - ${most_expensive['price']:.2f}")
print(f"  Cheapest       : {cheapest['title']} by {cheapest['writer']} - ${cheapest['price']:.2f}")

# ---------------------------------------------
#  10. NEW COMPUTED COLUMN: price per page
# ---------------------------------------------

print("\n" + "-" * 60)
print("  SECTION 8 - Price per Page (value for money)")
print("-" * 60)
df["price_per_page"] = (df["price"] / df["pages"]).round(4)
# Sort the books by price per page
value_df = pd.DataFrame(df.loc[:, ["title", "pages", "price", "price_per_page"]])
value_rows = sorted(
    value_df.itertuples(index=False),
    key=lambda row: float(row[3]),
)
value_df = pd.DataFrame(value_rows, columns=["title", "pages", "price", "price_per_page"])
# Print the books sorted by price per page
print(value_df.to_string(index=False))

# ---------------------------------------------
#  11. BOOKS PER YEAR
# ---------------------------------------------

print("\n" + "-" * 60)
print("  SECTION 9 - Books Published per Year")
print("-" * 60)
# Group by year and count the number of books published
per_year = pd.DataFrame(
    df.groupby("year", as_index=False).agg(books_published=("title", "count"))
)

# Print the books published per year
print(per_year.set_index("year")["books_published"].to_string())

# ---------------------------------------------
#  12. EXPORT TO CSV
# ---------------------------------------------

exports_dir = BASE_DIR / "data" / "exports"

# Create the exports directory if it doesn't exist
exports_dir.mkdir(parents=True, exist_ok=True)

# Create the books output CSV file
books_output_csv = exports_dir / "books_output.csv"

# Create the author summary CSV file
author_summary_csv = exports_dir / "books_author_summary.csv"

# Create the category summary CSV file
category_summary_csv = exports_dir / "books_category_summary.csv"

# Export the DataFrame to a CSV file
df.to_csv(books_output_csv, index=False)

# Export the author summary to a CSV file
author_summary.to_csv(author_summary_csv)

# Export the category summary to a CSV file
category_summary.to_csv(category_summary_csv, index=False)

# Print the CSV files exported
print("\n" + "-" * 60)
print("  CSV files exported:")
print(f"    - {books_output_csv}")
print(f"    - {author_summary_csv}")
print(f"    - {category_summary_csv}")
print("=" * 60)
