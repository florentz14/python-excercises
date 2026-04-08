import pandas as pd


orders = pd.DataFrame(
    {
        "product": ["pen", "pen", "mug", "mug"],
        "size": ["small", "large", "small", "large"],
        "qty": [100, 200, 150, 50],
    }
)
pricing = pd.DataFrame(
    {
        "product": ["pen", "pen", "mug", "mug"],
        "size": ["small", "large", "small", "large"],
        "price": [2.50, 3.00, 8.00, 10.00],
    }
)
print("Merge on multiple keys:")
print(pd.merge(orders, pricing, on=["product", "size"]))

stock = pd.DataFrame({"qty": [50, 30, 80, 20]}, index=["ball", "pen", "pencil", "mug"])
info = pd.DataFrame({"color": ["red", "black", "white", "green"]}, index=["ball", "pen", "pencil", "mug"])
print("\nMerge on index:")
print(pd.merge(stock, info, left_index=True, right_index=True))

frame3 = pd.DataFrame({"id": ["ball", "pencil", "pen", "mug"], "qty": [50, 30, 80, 20]})
frame4 = pd.DataFrame({"color": ["red", "white", "black", "green"]}, index=["ball", "pencil", "pen", "mug"])
print("\nMerge with left column and right index:")
print(pd.merge(frame3, frame4, left_on="id", right_index=True))
