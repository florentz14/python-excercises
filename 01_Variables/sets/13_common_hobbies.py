# -------------------------------------------------
# File Name: 13_common_hobbies.py
# Author: Florentino Báez
# Date: Variables - Sets
# Description: Practical Example — Common Hobbies.
#              Uses intersection (&) to find shared hobbies
#              between two people, and union (|) to list
#              all hobbies combined. A real-world use case
#              for set operations.
# -------------------------------------------------

# Example 18: Practical example - Common hobbies
print("Example 18: Practical example - Common hobbies")
print("-" * 40)

alice_hobbies = {"reading", "hiking", "coding", "gaming"}
bob_hobbies = {"gaming", "music", "hiking", "cooking"}

print("Alice's hobbies:", alice_hobbies)
print("Bob's hobbies:", bob_hobbies)

# Intersection: hobbies shared by both Alice and Bob
common = alice_hobbies & bob_hobbies
print("Common hobbies:", common)

# Union: all unique hobbies from both people
all_hobbies = alice_hobbies | bob_hobbies
print("All hobbies:", all_hobbies)
