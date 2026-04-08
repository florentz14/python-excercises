import pandas as pd


df = pd.DataFrame(
    {
        "product": ["A", "B", "C"],
        "price": [10, 20, 15],
        "quantity": [2, 3, 1],
    }
)

df["total"] = df["price"] * df["quantity"]

print("With total column:")
print(df)
