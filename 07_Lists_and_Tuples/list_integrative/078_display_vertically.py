# ---------------------------------------------------------------------------
# 168. Display List Vertically (each element on new line; or 2D as columns)
# ---------------------------------------------------------------------------
# Descripción: Display List Vertically (each element on new line; or 2D as columns)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def display_vertical(lst: list) -> None:
    for x in lst:
        print(x)


def display_2d_vertical(matrix: list[list]) -> None:
    for col in range(len(matrix[0]) if matrix else 0):
        print(' '.join(str(row[col]) for row in matrix))


display_vertical(['a', 'b', 'c'])
# For [[1,2,5],[4,5,8],[7,3,6]]: 1 4 7, 2 5 3, 5 8 6
