from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df = pd.read_csv(csv_path)
df.index = list("abcdefghij")

selected_df = df.loc[["b", "d", "f", "g"], ["score", "qualify"]]

print("Selected DataFrame:")
print(selected_df)
