import pandas as pd


df = pd.DataFrame(
    {
        "product": ["A", "B", "C"],
        "price": [10, 20, 15],
        "quantity": [2, 3, 1],
    }
)

mapping: dict[str, str] = {"A": "High", "B": "Medium", "C": "Low"}
df["level"] = df["product"].replace(mapping)

print("With mapping:")
print(df)
