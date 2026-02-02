"""
Clase VectorNP (NumPy)
======================
Tema: 11_POO - Clases sencillas
Descripción: Vector con NumPy; add(), scale() y magnitude().
Requiere: pip install numpy
"""

import numpy as np


class VectorNP:
    def __init__(self, values):
        self.values = np.array(values)

    def add(self, other):
        return self.values + np.asarray(other)

    def scale(self, factor):
        return self.values * factor

    def magnitude(self):
        return np.linalg.norm(self.values)


# --- Demo ---
if __name__ == "__main__":
    v = VectorNP([3, 4])
    print(v.add([1, 2]))        # [4 6]
    print(v.scale(2))           # [6 8]
    print(v.magnitude())        # 5.0
