# Archivo: 34_05_ejemplos_tipos.py
# Descripción: Ejemplos de rangos para diferentes tipos de matrices

import numpy as np

from rango_matriz_util import A


def ejemplos_diferentes_matrices():
    """
    Muestra ejemplos de rangos para diferentes tipos de matrices.
    """
    print("\nEjemplos de rangos para diferentes matrices:")
    print("=" * 70)

    ejemplos = {
        'Matriz identidad 3x3': np.eye(3),
        'Matriz de rango completo': np.array([[1, 2], [3, 4]]),
        'Matriz de rango reducido': np.array([[1, 2], [2, 4]]),
        'Matriz del ejemplo original': A,
        'Matriz cero': np.zeros((3, 3)),
        'Matriz rectangular (más columnas)': np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]),
        'Matriz rectangular (más filas)': np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    }

    for nombre, matriz in ejemplos.items():
        rango = np.linalg.matrix_rank(matriz)
        rango_max = min(matriz.shape)
        tipo = "Completo" if rango == rango_max else "Reducido"
        print(f"\n{nombre}:")
        print(f"  Forma: {matriz.shape}, Rango: {rango}/{rango_max} ({tipo})")
        if matriz.size <= 16:
            print(f"  Matriz:\n{matriz}")

    print("=" * 70)


if __name__ == "__main__":
    print("=== Versión 5: Matrices de Diferentes Tipos ===\n")
    ejemplos_diferentes_matrices()
