import pandas as pd


df = pd.DataFrame(
    {
        "country": ["USA", "USA", "UK", "UK"],
        "city": ["NYC", "LA", "London", "Manchester"],
        "pop": [8.4, 4.0, 9.0, 2.9],
    }
)

print("=== ORIGINAL ===")
print(df)
print()

print("=== set_index('country') ===")
print(df.set_index("country"))
print()

print("=== reset_index() ===")
print(df.set_index("country").reset_index())
