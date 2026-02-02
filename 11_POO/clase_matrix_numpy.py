"""
Clase MatrixNP (NumPy)
======================
Tema: 11_POO - Clases sencillas
Descripción: Matriz con NumPy; add(), multiply() (producto matricial) y transpose().
Requiere: pip install numpy
"""

import numpy as np


class MatrixNP:
    def __init__(self, data):
        self.data = np.array(data)

    def add(self, other):
        return self.data + np.asarray(other)

    def multiply(self, other):
        return self.data @ np.asarray(other)  # producto matricial

    def transpose(self):
        return self.data.T


# --- Demo ---
if __name__ == "__main__":
    A = MatrixNP([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print("A + B:\n", A.add(B))
    print("A @ B:\n", A.multiply(B))
    print("A.T:\n", A.transpose())
