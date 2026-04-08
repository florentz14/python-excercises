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

print("frame1:")
print(frame1)
print("\nframe2:")
print(frame2)

print("\nInner merge (auto key):")
print(pd.merge(frame1, frame2))
print("\nInner merge (on='id'):")
print(pd.merge(frame1, frame2, on="id"))
print("\nLeft merge:")
print(pd.merge(frame1, frame2, on="id", how="left"))
print("\nRight merge:")
print(pd.merge(frame1, frame2, on="id", how="right"))
print("\nOuter merge:")
print(pd.merge(frame1, frame2, on="id", how="outer"))
