# -------------------------------------------------
# File Name: 12_unique_elements.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Practical Example — Find Unique Elements.
# -------------------------------------------------

print("Example 17: Practical example - Find unique elements")
print("-" * 40)

votes = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print("Votes:", votes)

# Convert list to set to get only unique values
unique_votes = set(votes)
print("Unique votes:", unique_votes)

print(f"Total votes: {len(votes)}")          # 6 (all votes)
print(f"Unique votes: {len(unique_votes)}")  # 3 (distinct options)
