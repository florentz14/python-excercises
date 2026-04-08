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

frame2_renamed = frame2.rename(columns={"id": "id_from_frame2", "color": "color_from_frame2"})
joined_frame = frame1.join(frame2_renamed)

print("Join result with renamed columns:")
print(joined_frame)
