import pandas as pd


df = pd.DataFrame(
    {
        "product": ["A", "B", "C"],
        "price": [10, 20, 15],
        "quantity": [2, 3, 1],
    }
)

df["total"] = df["price"] * df["quantity"]
df = df.rename(columns={"total": "subtotal"})

print("Renamed:")
print(df)
