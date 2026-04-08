import pandas as pd


frame1 = pd.DataFrame(
    {
        "id": ["ball", "pencil", "pen", "mug", "ashtray"],
        "price": [12.33, 11.44, 33.21, 13.23, 33.62],
    }
)
frame2 = pd.DataFrame(
    {
        "id": ["pencil", "pencil", "ball", "pen"],
        "color": ["white", "red", "red", "black"],
    }
)

merged_index = pd.merge(frame1, frame2, left_index=True, right_index=True)

print("Merge on index:")
print(merged_index)
