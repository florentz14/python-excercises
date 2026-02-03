# Archivo: 49_03_newton_interpolacion.py
# Descripción: Interpolación de Newton (diferencias divididas)

print("=== 3. Interpolación de Newton ===\n")


def diferencias_divididas(x_puntos, y_puntos):
    """Calcula las diferencias divididas (coeficientes para Newton)."""
    n = len(x_puntos)
    tabla = [[0.0] * n for _ in range(n)]
    for i in range(n):
        tabla[i][0] = y_puntos[i]
    for j in range(1, n):
        for i in range(n - j):
            tabla[i][j] = (tabla[i+1][j-1] - tabla[i][j-1]) / (x_puntos[i+j] - x_puntos[i])
    return tabla[0]


def interpolacion_newton(x_puntos, y_puntos, x_evaluar):
    """Interpola usando método de Newton (diferencias divididas)."""
    n = len(x_puntos)
    coeficientes = diferencias_divididas(x_puntos, y_puntos)
    resultado = coeficientes[0]
    producto = 1.0
    for i in range(1, n):
        producto *= (x_evaluar - x_puntos[i-1])
        resultado += coeficientes[i] * producto
    return resultado


if __name__ == "__main__":
    x_newton = [1, 2, 4, 5]
    y_newton = [0, 1, 15, 24]

    print("Puntos conocidos:")
    for i in range(len(x_newton)):
        print(f"  ({x_newton[i]}, {y_newton[i]})")

    coefs = diferencias_divididas(x_newton, y_newton)
    print(f"\nCoeficientes de diferencias divididas: {coefs}")

    x_interp = 3.0
    y_newton_interp = interpolacion_newton(x_newton, y_newton, x_interp)
    print(f"Valor interpolado en x={x_interp}: {y_newton_interp:.4f}")
