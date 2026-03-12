# -------------------------------------------------
# File Name: 112_explode.py
# Description: Expand list-like columns
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({"id": [1, 2], "tags": [["a", "b"], ["c"]]})
print("Exploded:")
print(df.explode("tags"))
