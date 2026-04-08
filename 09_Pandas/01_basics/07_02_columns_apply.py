import pandas as pd


df = pd.DataFrame(
    {
        "product": ["A", "B", "C"],
        "price": [10, 20, 15],
        "quantity": [2, 3, 1],
    }
)

df["double_price"] = df["price"].apply(lambda x: x * 2)

print("With apply:")
print(df)
