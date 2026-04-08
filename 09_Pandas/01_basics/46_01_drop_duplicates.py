import pandas as pd


df = pd.DataFrame({"item": ["ball", "pencil", "pencil", "ashtray"], "status": [1, 1, 1, 2]})
clean_df = df.drop_duplicates()

print("Original data:")
print(df)
print("\nDrop duplicates:")
print(clean_df)
