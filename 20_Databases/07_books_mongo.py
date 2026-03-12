"""
Loading and writing data with MongoDB.

Driver: pymongo
Install: pip install pymongo
"""

import json
import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import PyMongoError

# -------------------------------------------------------------
#  MONGODB SETTINGS - loaded from .env
# -------------------------------------------------------------

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "books_db")

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
JSON_PATH = PROJECT_ROOT / "09_Pandas" / "data" / "book.json"

print("=" * 62)
print("          LOADING AND WRITING DATA WITH MONGODB")
print("=" * 62)

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.admin.command("ping")
    db = client[MONGO_DB]
    print(f"\nConnected to MongoDB -> database: '{MONGO_DB}'")
    print(f"URI: {MONGO_URI}")
except PyMongoError as error:
    print(f"\nConnection failed: {error}")
    print("\nMake sure MongoDB is running and MONGO_URI/MONGO_DB are correct.")
    raise SystemExit(1)

# -------------------------------------------------------------
#  1. LOAD JSON
# -------------------------------------------------------------

with JSON_PATH.open("r", encoding="utf-8") as file:
    data = json.load(file)

authors_raw = data["catalog"]["authors"]

# Fresh start on each run.
db.authors.drop()
db.books.drop()
db.author_stats.drop()

authors_docs = []
books_docs = []

for author in authors_raw:
    authors_docs.append(
        {
            "_id": author["id"],
            "writer": author["writer"],
            "nationality": author["nationality"],
            "language": author["language"],
            "bio": author["bio"],
        }
    )

    for book in author["books"]:
        books_docs.append(
            {
                "_id": book["id"],
                "author_id": author["id"],
                "writer": author["writer"],
                "title": book["title"],
                "category": book["category"],
                "year": book["year"],
                "pages": book["pages"],
                "edition": book["edition"],
                "price": float(book["price"]),
                "currency": book["currency"],
                "available": bool(book["available"]),
                "rating": float(book["rating"]),
                "tags": book["tags"],
            }
        )

db.authors.insert_many(authors_docs)
db.books.insert_many(books_docs)
db.books.create_index("author_id")
db.books.create_index("category")
db.books.create_index("rating")

print(f"\nInserted {len(authors_docs)} authors and {len(books_docs)} books")

# -------------------------------------------------------------
#  2. READ - find all books
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 1 - All Books")
print("-" * 62)

all_books = list(
    db.books.find(
        {},
        {
            "_id": 1,
            "title": 1,
            "category": 1,
            "year": 1,
            "price": 1,
            "rating": 1,
        },
    ).sort("_id", 1)
)
print(pd.DataFrame(all_books).to_string(index=False))

# -------------------------------------------------------------
#  3. FILTER - available and rating >= 4.5
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 2 - Available Books with Rating >= 4.5")
print("-" * 62)

top_books = list(
    db.books.find(
        {"available": True, "rating": {"$gte": 4.5}},
        {"_id": 0, "title": 1, "writer": 1, "price": 1, "rating": 1},
    ).sort("rating", -1)
)
print(pd.DataFrame(top_books).to_string(index=False))

# -------------------------------------------------------------
#  4. AGGREGATE - GROUP BY category
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 3 - Stats by Category (Aggregation Pipeline)")
print("-" * 62)

category_pipeline = [
    {
        "$group": {
            "_id": "$category",
            "total_books": {"$sum": 1},
            "avg_price": {"$avg": "$price"},
            "avg_rating": {"$avg": "$rating"},
        }
    },
    {"$sort": {"avg_rating": -1}},
]
cat_result = list(db.books.aggregate(category_pipeline))
df_cat = pd.DataFrame(cat_result).rename(columns={"_id": "category"})
if not df_cat.empty:
    df_cat["avg_price"] = df_cat["avg_price"].round(2)
    df_cat["avg_rating"] = df_cat["avg_rating"].round(2)
print(df_cat.to_string(index=False))

# -------------------------------------------------------------
#  5. UPDATE + DELETE
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 4 - UPDATE and DELETE")
print("-" * 62)

before = db.books.find_one({"_id": "B006"}, {"title": 1, "available": 1})
print(f"Before update -> {before['title']}, available: {before['available']}")

db.books.update_one({"_id": "B006"}, {"$set": {"available": True}})

after = db.books.find_one({"_id": "B006"}, {"title": 1, "available": 1})
print(f"After update  -> {after['title']}, available: {after['available']}")

before_count = db.books.count_documents({})
db.books.delete_one({"_id": "B001"})
after_count = db.books.count_documents({})
print(f"Books before delete: {before_count}")
print(f"Books after  delete: {after_count}")

# -------------------------------------------------------------
#  6. PANDAS ANALYSIS + EXPORT TO COLLECTION
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 5 - Pandas Analysis + Export")
print("-" * 62)

df_books = pd.DataFrame(list(db.books.find({}, {"_id": 0})))
df_books["price_per_page"] = (df_books["price"] / df_books["pages"]).round(4)

author_stats = (
    df_books.groupby("writer")
    .agg(
        books=("title", "count"),
        total_revenue=("price", "sum"),
        avg_rating=("rating", "mean"),
    )
    .reset_index()
    .round(2)
)

db.author_stats.insert_many(author_stats.to_dict(orient="records"))
print("Collection 'author_stats' created from Pandas aggregation")
print(author_stats.to_string(index=False))

# -------------------------------------------------------------
#  7. METADATA
# -------------------------------------------------------------

print("\n" + "-" * 62)
print("  SECTION 6 - Database Metadata")
print("-" * 62)

collections = db.list_collection_names()
print(f"Collections: {collections}")

for coll in collections:
    count = db[coll].count_documents({})
    print(f"- {coll}: {count} documents")

client.close()
print("\nConnection closed.")
print("=" * 62)
