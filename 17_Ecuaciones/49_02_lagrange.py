# Archivo: 49_02_lagrange.py
# Descripción: Interpolación de Lagrange

print("=== 2. Interpolación de Lagrange ===\n")


def interpolacion_lagrange(x_puntos, y_puntos, x_evaluar):
    """
    Interpola un punto usando polinomio de Lagrange.
    Complejidad: O(n²)
    """
    n = len(x_puntos)
    resultado = 0.0
    for i in range(n):
        producto = 1.0
        for j in range(n):
            if i != j:
                producto *= (x_evaluar - x_puntos[j]) / (x_puntos[i] - x_puntos[j])
        resultado += y_puntos[i] * producto
    return resultado


def construir_polinomio_lagrange(x_puntos, y_puntos):
    """Devuelve una función que evalúa el polinomio de Lagrange."""
    def polinomio(x):
        return interpolacion_lagrange(x_puntos, y_puntos, x)
    return polinomio


if __name__ == "__main__":
    x_conocidos = [0, 1, 2, 3]
    y_conocidos = [1, 2, 5, 10]

    print("Puntos conocidos:")
    for i in range(len(x_conocidos)):
        print(f"  ({x_conocidos[i]}, {y_conocidos[i]})")

    x_interpolar = 1.5
    y_interpolado = interpolacion_lagrange(x_conocidos, y_conocidos, x_interpolar)
    print(f"\nValor interpolado en x={x_interpolar}: {y_interpolado:.4f}")

    print("\nVerificación en puntos conocidos:")
    for x, y in zip(x_conocidos, y_conocidos):
        valor = interpolacion_lagrange(x_conocidos, y_conocidos, x)
        print(f"  x={x}: esperado={y}, obtenido={valor:.6f}")
