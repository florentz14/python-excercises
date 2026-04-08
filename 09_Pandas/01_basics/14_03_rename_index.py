import pandas as pd


df = pd.DataFrame(
    {
        "country": ["USA", "USA", "UK", "UK"],
        "city": ["NYC", "LA", "London", "Manchester"],
        "pop": [8.4, 4.0, 9.0, 2.9],
    }
)

df_idx = df.set_index("country")
df_idx.index = df_idx.index.rename("nation")

print("=== index.rename('nation') ===")
print(df_idx)
