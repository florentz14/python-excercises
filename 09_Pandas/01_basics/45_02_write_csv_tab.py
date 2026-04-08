from pathlib import Path

import pandas as pd


df = pd.DataFrame(
    {"col1": [1, 4, 3, 4, 5], "col2": [4, 5, 6, 7, 8], "col3": [7, 8, 9, 0, 1]}
)
out = Path(__file__).parent / "new_file.csv"
df.to_csv(out, sep="\t", index=False)

print(f"File written: {out.name}")
