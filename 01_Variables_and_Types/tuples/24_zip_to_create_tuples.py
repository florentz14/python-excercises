# -------------------------------------------------
# File Name: 24_zip_to_create_tuples.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Create tuples with zip() pairing elements from iterables.
# -------------------------------------------------

names = ["Anna", "Louis", "Carlos"]
scores = [90, 85, 95]
pairs = list(zip(names, scores))
print("names:", names)
print("scores:", scores)
print("zip(names, scores):", pairs)

for name, score in pairs:
    print(f"  {name}: {score}")
