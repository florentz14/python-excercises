from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "colors_animals.csv"
table_frame = pd.read_table(csv_path, sep=",")

print("read_table(..., sep=','):")
print(table_frame)
