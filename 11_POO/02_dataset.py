"""
Clase Dataset (NumPy)
=====================
Tema: 11_POO - Clases sencillas
Descripción: Conjunto de datos; mean(), max() y normalize() por columnas.
Requiere: pip install numpy
"""

import numpy as np


class Dataset:
    def __init__(self, data):
        self.data = np.array(data)

    def mean(self):
        return self.data.mean(axis=0)

    def max(self):
        return self.data.max(axis=0)

    def normalize(self):
        min_val = self.data.min()
        max_val = self.data.max()
        if max_val == min_val:
            return np.zeros_like(self.data)
        return (self.data - min_val) / (max_val - min_val)


# --- Demo ---
if __name__ == "__main__":
    data = Dataset([
        [70, 180],
        [80, 175],
        [65, 170],
    ])

    print("Mean:", data.mean())
    print("Max:", data.max())
    print("Normalized:\n", data.normalize())
