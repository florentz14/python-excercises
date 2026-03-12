# -------------------------------------------------
# File Name: 43_merge_join_basics.py
# Author: Florentino Baez
# Date: 09_Pandas
# Description: Basic merge and join operations.
# -------------------------------------------------

import pandas as pd

# 1. Source data (DataFrame)
frame1 = pd.DataFrame(
    {
        "id": ["ball", "pencil", "pen", "mug", "ashtray"],
        "price": [12.33, 11.44, 33.21, 13.23, 33.62],
    }
)
# Print the DataFrame
print("=== FRAME 1 ===")
print(frame1)
print()

# Create a DataFrame
frame2 = pd.DataFrame(
    {
        "id": ["pencil", "pencil", "ball", "pen"],
        "color": ["white", "red", "red", "black"],
    }
)
# Print the DataFrame
print("=== FRAME 1 ===")
print(frame1)
print("\n=== FRAME 2 ===")
print(frame2)

# 2. Merge by column key
merged_on_id = pd.merge(frame1, frame2, on="id")
print("\n=== MERGE ON 'id' ===")
print(merged_on_id)

# 3. Merge by index
merged_index = pd.merge(frame1, frame2, left_index=True, right_index=True)
print("\n=== MERGE ON INDEX ===")
print(merged_index)

# 4. Join with renamed columns to avoid overlap confusion
frame2_renamed = frame2.rename(columns={"id": "id_from_frame2", "color": "color_from_frame2"})
joined_frame = frame1.join(frame2_renamed)
print("\n=== JOIN RESULT ===")
print(joined_frame)
