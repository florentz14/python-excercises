from pathlib import Path

import pandas as pd


out = Path(__file__).parent / "new_file.csv"
df2 = pd.read_csv(out, sep="\t")

print("Data from new_file.csv file:")
print(df2)
