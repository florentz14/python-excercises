"""
Clase SparseMatrix (diccionario)
=================================
Tema: 11_POO - Clases sencillas
Descripción: Matriz dispersa; solo guarda elementos no nulos en un dict (fila, col): valor.
"""


class SparseMatrix:
    def __init__(self):
        self.data = {}  # (row, col): value

    def set(self, row, col, value):
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def get(self, row, col):
        return self.data.get((row, col), 0)


# --- Demo ---
if __name__ == "__main__":
    M = SparseMatrix()
    M.set(0, 1, 5)
    M.set(2, 3, 10)

    print(M.get(0, 1))  # 5
    print(M.get(1, 1))  # 0
