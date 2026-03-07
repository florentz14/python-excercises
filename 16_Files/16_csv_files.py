"""
16_Files - Exercise 16: Working with CSV files using the csv module
==================================================================
CSV (Comma-Separated Values) is common for data exchange.
The csv module handles quoting, escaping, and different delimiters.
"""

import csv

# Create a CSV file
csv_file = "data.csv"
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "San Francisco"],
    ["Charlie", 35, "Chicago"]
]

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print(f"Created CSV file '{csv_file}'.")

# Read the CSV file
print("\nReading CSV file:")
with open(csv_file, "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Using DictReader for header-based access
print("\nUsing DictReader:")
with open(csv_file, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old from {row['City']}")

# Write with DictWriter
dict_csv_file = "dict_data.csv"
fieldnames = ["Product", "Price", "Quantity"]

with open(dict_csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Product": "Apple", "Price": 1.50, "Quantity": 10})
    writer.writerow({"Product": "Banana", "Price": 0.75, "Quantity": 20})

print(f"\nCreated dict-based CSV '{dict_csv_file}'.")

# Read back
print("Reading dict CSV:")
with open(dict_csv_file, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# Custom delimiter example
tsv_file = "data.tsv"
with open(tsv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerows(data)

print(f"\nCreated TSV file '{tsv_file}' with tab delimiter.")
