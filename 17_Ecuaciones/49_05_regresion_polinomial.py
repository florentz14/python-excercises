# Archivo: 49_05_regresion_polinomial.py
# Descripción: Regresión polinomial (mínimos cuadrados)

import numpy as np

print("=== 5. Regresión Polinomial (Grado 2) ===\n")


def regresion_polinomial(x_datos, y_datos, grado=2):
    """
    Regresión polinomial por mínimos cuadrados.
    Retorna coeficientes [a_n, ..., a_0] para y = a_n*x^n + ... + a_0.
    """
    n = len(x_datos)
    A = np.array([[x**i for i in range(grado + 1)] for x in x_datos])
    b = np.array(y_datos)
    ATA = np.dot(A.T, A)
    ATb = np.dot(A.T, b)
    try:
        coeficientes = np.linalg.solve(ATA, ATb)
        return coeficientes[::-1]
    except np.linalg.LinAlgError:
        return None


if __name__ == "__main__":
    x_poly = [0, 1, 2, 3, 4, 5]
    y_poly = [1, 2, 5, 10, 17, 26]

    coefs_poly = regresion_polinomial(x_poly, y_poly, grado=2)
    if coefs_poly is not None:
        print(f"Datos: x={x_poly}, y={y_poly}")
        print(f"Coeficientes (ax^2 + bx + c): a={coefs_poly[0]:.4f}, b={coefs_poly[1]:.4f}, c={coefs_poly[2]:.4f}")
        print(f"Ecuación: y = {coefs_poly[0]:.4f}x^2 + {coefs_poly[1]:.4f}x + {coefs_poly[2]:.4f}")
