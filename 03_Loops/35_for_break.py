"""For loop: break statement.
Exits the loop when value 5 is found.
"""
# Author: Florentino Báez


for i in range(1, 11):
    if i == 5:
        print("Found 5, breaking out")
        break
    print(i)
