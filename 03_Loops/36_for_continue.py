"""For loop: continue statement.
Skips printing when value is 3.
"""
# Author: Florentino Báez


for i in range(1, 6):
    if i == 3:
        print("Skipping 3")
        continue
    print(i)
