# -------------------------------------------------
# File Name: 34_point.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: 2D Point class using NumPy.
# -------------------------------------------------

import numpy as np


class Point2D:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=float)

    def move(self, direction):
        self.position += np.asarray(direction)

    def distance_to_origin(self):
        return np.linalg.norm(self.position)


# --- Demo ---
if __name__ == "__main__":
    p = Point2D(3, 4)
    p.move([1, -2])

    print(p.position)            # [4 2]
    print(p.distance_to_origin())
