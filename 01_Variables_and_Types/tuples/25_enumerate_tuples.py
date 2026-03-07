# ------------------------------------------------------------
# File: 25_enumerate_tuples.py
# Purpose: enumerate() with tuples.
# Description: Iterate with index and value.
# ------------------------------------------------------------

names = ("Anna", "Louis", "Carlos")
print("Tuple:", names)
print("\nfor i, name in enumerate(names):")
for i, name in enumerate(names):
    print(f"  {i}: {name}")

# Start from 1
print("\nenumerate(names, start=1):")
for i, name in enumerate(names, start=1):
    print(f"  {i}: {name}")
