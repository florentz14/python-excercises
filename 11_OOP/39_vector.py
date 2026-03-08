# -------------------------------------------------
# File Name: 39_vector.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Vector class using lists.
# -------------------------------------------------

class Vector:
    def __init__(self, values):
        self.values = values  # list

    def add(self, other):
        return [self.values[i] + other[i] for i in range(len(self.values))]

    def scale(self, factor):
        return [x * factor for x in self.values]


# --- Demo ---
if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = [4, 5, 6]

    print(v1.add(v2))     # [5, 7, 9]
    print(v1.scale(10))   # [10, 20, 30]
