# -------------------------------------------------
# File Name: 03_add_set_items.py
# Author: Florentino Báez
# Date: Variables - Sets
# Description: Add Items to a Set.
#              add() inserts a single element.
#              update() merges multiple elements from any
#              iterable (list, set, tuple, string).
#              Duplicates are silently ignored.
# -------------------------------------------------

fruits = {"apple", "banana", "cherry"}
print("Original:", fruits)

# =========================================================================
# add() - Add a single item
# =========================================================================

fruits.add("orange")                          # Insert one element
print("\nAfter add('orange'):", fruits)

fruits.add("mango")
print("After add('mango'):", fruits)

# Adding an item that already exists has NO effect (no error, no duplicate)
fruits.add("banana")
print("After add('banana') again:", fruits)
# "banana" appears only once

# =========================================================================
# update() - Add multiple items from an iterable
# =========================================================================

# Add items from a list
fruits.update(["grape", "kiwi", "pear"])
print("\nAfter update(['grape','kiwi','pear']):", fruits)

# Add items from another set
tropical = {"papaya", "dragonfruit"}
fruits.update(tropical)
print("After update(tropical):", fruits)

# Add items from a tuple
fruits.update(("lychee", "fig"))
print("After update(('lychee','fig')):", fruits)

# Add characters from a string (each char becomes an element!)
letters = set()
letters.update("abc")
print("\nupdate('abc'):", letters)
# Output: {'a', 'b', 'c'}

# =========================================================================
# update() accepts multiple iterables at once
# =========================================================================

colors = {"red"}
colors.update(["blue", "green"], {"yellow", "purple"}, ("orange",))
print("\nMultiple update:", colors)

# =========================================================================
# Practical example: collect unique tags from multiple posts
# =========================================================================

all_tags = set()
post1_tags = ["python", "coding", "tutorial"]
post2_tags = ["python", "web", "django"]
post3_tags = ["coding", "javascript", "web"]

all_tags.update(post1_tags)     # Merge each post's tags into the main set
all_tags.update(post2_tags)
all_tags.update(post3_tags)

print(f"\nAll unique tags: {sorted(all_tags)}")
print(f"Total unique tags: {len(all_tags)}")
# Output: ['coding', 'django', 'javascript', 'python', 'tutorial', 'web']
