"""
Clase Matrix (listas)
=====================
Tema: 11_POO - Clases sencillas
Descripción: Matriz con lista de listas; add() elemento a elemento.
"""


class Matrix:
    def __init__(self, data):
        self.data = data  # list of lists

    def add(self, other):
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + other[i][j])
            result.append(row)
        return result


# --- Demo ---
if __name__ == "__main__":
    A = Matrix([[1, 2], [3, 4]])
    B = [[5, 6], [7, 8]]

    print(A.add(B))  # [[6, 8], [10, 12]]
