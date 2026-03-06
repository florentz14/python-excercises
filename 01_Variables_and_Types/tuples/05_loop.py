# -------------------------------------------------
# File Name: 05_loop.py
# Author: Florentino Báez
# Date: Variables - Tuples
# Description: Loop Through a Tuple.
#              Use a for loop to iterate over each element.
#              Tuples are iterable just like lists, but
#              their elements cannot be modified.
# -------------------------------------------------

print("Example 5: Loop through a tuple")
print("-" * 40)

scores = (85, 92, 78, 95, 88)
print("Scores:", scores)

# Iterate over each element in the tuple
for score in scores:
    print(f"Score: {score}")
