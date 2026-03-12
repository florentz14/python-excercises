# =============================================================================
# PANDAS IN DEPTH: MERGING & JOINING
# Complete program with examples covering all merge/join operations
# =============================================================================

import numpy as np
import pandas as pd

# Set the display options
pd.set_option("display.width", 100)
pd.set_option("display.max_columns", 10)

# Set the separator for the print statements
SEP = "=" * 65
SEC = "-" * 65

# =============================================================================
# SECTION 1: SAMPLE DATA
# =============================================================================
print(SEP)
print("SECTION 1: SAMPLE DataFrames")
print(SEP)

# Create a DataFrame with the first set of data
frame1 = pd.DataFrame(
    {
        "id": ["ball", "pencil", "pen", "mug", "ashtray"],
        "price": [12.33, 11.44, 33.21, 13.23, 33.62],
    }
)

# Create a DataFrame with the second set of data
frame2 = pd.DataFrame(
    {
        "id": ["pencil", "pencil", "ball", "pen"],
        "color": ["white", "red", "red", "black"],
    }
)

# Print the DataFrames
print("frame1:\n", frame1)
print("\nframe2:\n", frame2)

# =============================================================================
# SECTION 2: BASIC MERGE (INNER JOIN - default)
# =============================================================================
print(f"\n{SEP}")
print("SECTION 2: BASIC MERGE - pd.merge() [INNER JOIN]")
print(SEP)
print("Keeps only rows whose 'id' appears in BOTH DataFrames.")
print(SEC)

# Auto-detects common column 'id'
result_auto = pd.merge(frame1, frame2)
print("pd.merge(frame1, frame2)  [auto-detect key]:\n", result_auto)

# Explicit key with on=
result_on = pd.merge(frame1, frame2, on="id")
print("\npd.merge(frame1, frame2, on='id')  [explicit key]:\n", result_on)

# =============================================================================
# SECTION 3: OUTER JOINS (LEFT, RIGHT, OUTER)
# =============================================================================
print(f"\n{SEP}")
print("SECTION 3: JOIN TYPES - how='left' / 'right' / 'outer'")
print(SEP)

# LEFT JOIN - all rows from frame1, matching rows from frame2
left = pd.merge(frame1, frame2, on="id", how="left")
print("LEFT JOIN  (all frame1 rows preserved, NaN where no match):\n", left)

# RIGHT JOIN - all rows from frame2, matching rows from frame1
right = pd.merge(frame1, frame2, on="id", how="right")
print("\nRIGHT JOIN (all frame2 rows preserved, NaN where no match):\n", right)

# OUTER JOIN - all rows from both, NaN where no match
outer = pd.merge(frame1, frame2, on="id", how="outer")
print("\nOUTER JOIN (all rows from both, NaN where no match):\n", outer)

# =============================================================================
# SECTION 4: MERGING ON MULTIPLE KEYS
# =============================================================================
print(f"\n{SEP}")
print("SECTION 4: MERGING ON MULTIPLE KEYS")
print(SEP)

# Create a DataFrame with the orders data
orders = pd.DataFrame(
    {
        "product": ["pen", "pen", "mug", "mug"],
        "size": ["small", "large", "small", "large"],
        "qty": [100, 200, 150, 50],
    }
)

# Create a DataFrame with the pricing data
pricing = pd.DataFrame(
    {
        "product": ["pen", "pen", "mug", "mug"],
        "size": ["small", "large", "small", "large"],
        "price": [2.50, 3.00, 8.00, 10.00],
    }
)

# Print the DataFrames
print("orders:\n", orders)
print("\npricing:\n", pricing)

# Merge the orders and pricing DataFrames on the 'product' and 'size' columns
multi_key = pd.merge(orders, pricing, on=["product", "size"])
print("\npd.merge(orders, pricing, on=['product', 'size']):\n", multi_key)

# =============================================================================
# SECTION 5: MERGING ON INDEX (left_index / right_index)
# =============================================================================
print(f"\n{SEP}")
print("SECTION 5: MERGING ON INDEX")
print(SEP)

# DataFrames with meaningful indexes
stock = pd.DataFrame({"qty": [50, 30, 80, 20]}, index=["ball", "pen", "pencil", "mug"])
info = pd.DataFrame(
    {"color": ["red", "black", "white", "green"]},
    index=["ball", "pen", "pencil", "mug"],
)

print("stock (indexed by product):\n", stock)
print("\ninfo  (indexed by product):\n", info)

# Merge the stock and info DataFrames on the index
by_index = pd.merge(stock, info, left_index=True, right_index=True)
print("\npd.merge(stock, info, left_index=True, right_index=True):\n", by_index)

# Mixed: one column key, one index key
frame3 = pd.DataFrame({"id": ["ball", "pencil", "pen", "mug"], "qty": [50, 30, 80, 20]})
frame4 = pd.DataFrame(
    {"color": ["red", "white", "black", "green"]},
    index=["ball", "pencil", "pen", "mug"],
)
print("\nframe3 (column key 'id'):\n", frame3)
print("\nframe4 (index as key):\n", frame4)

# Merge the frame3 and frame4 DataFrames on the 'id' column and the index
mixed = pd.merge(frame3, frame4, left_on="id", right_index=True)
print("\npd.merge(frame3, frame4, left_on='id', right_index=True):\n", mixed)

# =============================================================================
# SECTION 6: DataFrame.join() - index-based convenience method
# =============================================================================
print(f"\n{SEP}")
print("SECTION 6: DataFrame.join() - index-based convenience method")
print(SEP)
print("join() merges on the index by default; faster than merge() for index keys.")
print(SEC)

# Create a DataFrame with the employees data
employees = pd.DataFrame(
    {"name": ["Alice", "Bob", "Carol"], "department": ["HR", "IT", "Finance"]},
    index=[101, 102, 103],
)
# Create a DataFrame with the salaries data
salaries = pd.DataFrame({"salary": [70000, 90000, 85000]}, index=[101, 102, 103])

print("employees:\n", employees)
print("\nsalaries:\n", salaries)

# Join the employees and salaries DataFrames on the index
joined = employees.join(salaries)
print("\nemployees.join(salaries):\n", joined)

# join() with how= parameter
extra = pd.DataFrame({"bonus": [5000, 7000]}, index=[101, 104])
print("\nextra (has emp 104 not in employees):\n", extra)

# Join the employees and extra DataFrames on the index with how='left'
left_join = employees.join(extra, how="left")
# Join the employees and extra DataFrames on the index with how='outer'
outer_join = employees.join(extra, how="outer")
print("\nemployees.join(extra, how='left'):\n", left_join)
print("\nemployees.join(extra, how='outer'):\n", outer_join)

# Joining multiple DataFrames at once
dept_info = pd.DataFrame(
    {"location": ["Building A", "Building B", "Building C"]},
    index=[101, 102, 103],
)
# Joining multiple DataFrames at once
multi_joined = employees.join([salaries, dept_info])
# Print the joined DataFrame
print("\nemployees.join([salaries, dept_info]):\n", multi_joined)

# =============================================================================
# SECTION 7: HANDLING OVERLAPPING COLUMN NAMES (suffixes)
# =============================================================================
print(f"\n{SEP}")
print("SECTION 7: HANDLING OVERLAPPING COLUMN NAMES - suffixes")
print(SEP)

# Create a DataFrame with the left data
left_df = pd.DataFrame({"id": [1, 2, 3], "value": [10, 20, 30]})
# Create a DataFrame with the right data
right_df = pd.DataFrame({"id": [1, 2, 4], "value": [100, 200, 400]})
# Print the DataFrames

print("left_df:\n", left_df)
print("\nright_df:\n", right_df)

# Merge the left and right DataFrames on the 'id' column with custom suffixes
merged_suffix = pd.merge(left_df, right_df, on="id", suffixes=("_left", "_right"))
# Print the merged DataFrame
print("\npd.merge(..., suffixes=('_left', '_right')):\n", merged_suffix)

# =============================================================================
# SECTION 8: REAL-WORLD SCENARIO
#             Sales analysis - products, transactions, regions
# =============================================================================
print(f"\n{SEP}")
print("SECTION 8: REAL-WORLD SCENARIO - Sales Analysis")
print(SEP)

# Create a DataFrame with the products data
products = pd.DataFrame(
    {
        "product_id": [1, 2, 3, 4],
        "product_name": ["Laptop", "Mouse", "Keyboard", "Monitor"],
        "category": ["Electronics", "Accessories", "Accessories", "Electronics"],
    }
)

# Create a DataFrame with the transactions data
transactions = pd.DataFrame(
    {
        "txn_id": [1001, 1002, 1003, 1004, 1005],
        "product_id": [1, 2, 1, 3, 5],
        "region_id": [10, 20, 10, 30, 10],
        "revenue": [1200, 25, 1350, 75, 800],
    }
)

# Create a DataFrame with the regions data
regions = pd.DataFrame(
    {
        "region_id": [10, 20, 30],
        "region_name": ["North", "South", "East"],
    }
)

print("products:\n", products)
print("\ntransactions:\n", transactions)
print("\nregions:\n", regions)

# Step 1: join transactions with products (LEFT to keep unknown products) (LEFT JOIN)
step1 = pd.merge(transactions, products, on="product_id", how="left")
print("\nStep 1 - transactions LEFT JOIN products:\n", step1)

# Step 2: join with regions (LEFT JOIN)
final = pd.merge(step1, regions, on="region_id", how="left")
print("\nStep 2 - result LEFT JOIN regions:\n", final)

# Step 3: simple aggregation on the merged result (GROUP BY)
print("\nRevenue by category:\n", final.groupby("category")["revenue"].sum().reset_index())
print("\nRevenue by region:\n", final.groupby("region_name")["revenue"].sum().reset_index())

# =============================================================================
# SECTION 9: SUMMARY TABLE
# =============================================================================
print(f"\n{SEP}")
print("SECTION 9: SUMMARY - Merge / Join Quick Reference")
print(SEP)

# Create a DataFrame with the summary data
summary = pd.DataFrame(
    {
        "Function / Option": [
            "pd.merge(df1, df2)",
            'pd.merge(..., on="col")',
            'pd.merge(..., how="left")',
            'pd.merge(..., how="right")',
            'pd.merge(..., how="outer")',
            'pd.merge(..., how="inner")',
            'pd.merge(..., on=["c1","c2"])',
            "pd.merge(..., left_index=True, right_index=True)",
            'pd.merge(..., left_on="col", right_index=True)',
            "pd.merge(..., suffixes=(a,b))",
            "df1.join(df2)",
            "df1.join([df2, df3])",
            'df1.join(df2, how="outer")',
        ],
        "Description": [
            "Inner join; auto-detects common column(s)",
            "Inner join on explicit column key",
            "Keep ALL rows from left df; NaN for missing right",
            "Keep ALL rows from right df; NaN for missing left",
            "Keep ALL rows from both; NaN for missing matches",
            "Keep only rows present in BOTH (default)",
            "Inner join on multiple column keys",
            "Join on row indexes of both DataFrames",
            "Left column key matched to right index",
            "Rename duplicate columns with custom suffixes",
            "Index-based inner join (convenience method)",
            "Join multiple DataFrames at once by index",
            "Index-based outer join",
        ],
        "Time Complexity": [
            "O(n*m) worst; O(n) avg w/ hash",
            "O(n*m) worst; O(n) avg w/ hash",
            "O(n*m) worst; O(n) avg w/ hash",
            "O(n*m) worst; O(n) avg w/ hash",
            "O(n*m) worst; O(n) avg w/ hash",
            "O(n*m) worst; O(n) avg w/ hash",
            "O(n*m) worst; O(n) avg w/ hash",
            "O(n+m)",
            "O(n+m)",
            "Same as underlying merge",
            "O(n+m)",
            "O(n+m) per join",
            "O(n+m)",
        ],
    }
)

# Print the summary DataFrame
print(summary.to_string(index=False))

print(f"\n{SEP}")
# Print the end of the program
print("END OF PROGRAM")
print(SEP)
