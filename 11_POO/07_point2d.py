"""
Clase Point2D (NumPy)
=====================
Tema: 11_POO - Clases sencillas
Descripción: Punto en 2D; move() y distance_to_origin().
Requiere: pip install numpy
"""

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
