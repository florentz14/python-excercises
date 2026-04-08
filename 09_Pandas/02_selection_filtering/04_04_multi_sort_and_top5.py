from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "fictional_army.csv"
df = pd.read_csv(csv_path)

print("Sort by regiment, then postTestScore:")
print(df.sort_values(by=["regiment", "postTestScore"], ascending=[True, False]))
print("\nTop 5 by postTestScore:")
print(df.nlargest(5, "postTestScore"))
