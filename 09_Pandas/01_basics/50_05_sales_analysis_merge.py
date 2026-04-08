import pandas as pd


products = pd.DataFrame(
    {
        "product_id": [1, 2, 3, 4],
        "product_name": ["Laptop", "Mouse", "Keyboard", "Monitor"],
        "category": ["Electronics", "Accessories", "Accessories", "Electronics"],
    }
)
transactions = pd.DataFrame(
    {
        "txn_id": [1001, 1002, 1003, 1004, 1005],
        "product_id": [1, 2, 1, 3, 5],
        "region_id": [10, 20, 10, 30, 10],
        "revenue": [1200, 25, 1350, 75, 800],
    }
)
regions = pd.DataFrame({"region_id": [10, 20, 30], "region_name": ["North", "South", "East"]})

step1 = pd.merge(transactions, products, on="product_id", how="left")
final = pd.merge(step1, regions, on="region_id", how="left")

print("Final merged sales table:")
print(final)

revenue_by_category = final.groupby("category", as_index=False).agg(revenue=("revenue", "sum"))
revenue_by_region = final.groupby("region_name", as_index=False).agg(revenue=("revenue", "sum"))

print("\nRevenue by category:")
print(revenue_by_category)
print("\nRevenue by region:")
print(revenue_by_region)
