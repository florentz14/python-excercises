import pandas as pd


df = pd.DataFrame(
    {
        "country": ["USA", "USA", "UK", "UK"],
        "city": ["NYC", "LA", "London", "Manchester"],
        "pop": [8.4, 4.0, 9.0, 2.9],
    }
)

df_mi = df.set_index(["country", "city"])

print("=== MultiIndex (country, city) ===")
print(df_mi)
print()

print("=== MultiIndex reset_index() ===")
print(df_mi.reset_index())
