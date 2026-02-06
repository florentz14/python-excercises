# Example 18: Practical example - Common hobbies
print("Example 18: Practical example - Common hobbies")
print("-" * 40)
alice_hobbies = {"reading", "hiking", "coding", "gaming"}
bob_hobbies = {"gaming", "music", "hiking", "cooking"}
print("Alice's hobbies:", alice_hobbies)
print("Bob's hobbies:", bob_hobbies)
common = alice_hobbies & bob_hobbies
print("Common hobbies:", common)
all_hobbies = alice_hobbies | bob_hobbies
print("All hobbies:", all_hobbies)
