# ------------------------------------------------------------
# File: 24_zip_to_create_tuples.py
# Purpose: Create tuples with zip().
# Description: Pair elements from multiple iterables.
# ------------------------------------------------------------

names = ["Anna", "Louis", "Carlos"]
scores = [90, 85, 95]
pairs = list(zip(names, scores))
print("names:", names)
print("scores:", scores)
print("zip(names, scores):", pairs)

for name, score in pairs:
    print(f"  {name}: {score}")
