import pandas as pd


df = pd.DataFrame(
    {
        "country": ["USA", "USA", "UK", "UK"],
        "city": ["NYC", "LA", "London", "Manchester"],
        "pop": [8.4, 4.0, 9.0, 2.9],
    }
)

print("=== set_index(drop=False) ===")
print(df.set_index("country", drop=False))
