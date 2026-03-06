# Archivo: 49_01_newton_raphson.py
# Descripción: Método de Newton-Raphson para raíces

print("=== Métodos Numéricos ===\n")
print("=== 1. Método de Newton-Raphson ===\n")


def newton_raphson(f, df, x0, tolerancia=1e-6, max_iter=100):
    """
    Encuentra una raíz de f(x) = 0 usando Newton-Raphson.
    Retorna: (raíz, número de iteraciones, convergió)
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-10:
            return None, i, False
        x_nuevo = x - fx / dfx
        if abs(x_nuevo - x) < tolerancia:
            return x_nuevo, i + 1, True
        x = x_nuevo
    return x, max_iter, False


if __name__ == "__main__":
    print("Ejemplo 1: Raíz cuadrada de 16 (x^2 - 16 = 0)")
    f1 = lambda x: x**2 - 16
    df1 = lambda x: 2*x
    raiz1, iter1, conv1 = newton_raphson(f1, df1, 5.0)
    print(f"Raíz: {raiz1}, Iteraciones: {iter1}, Convergió: {conv1}")

    print("\nEjemplo 2: Raíz de x^3 - x - 1 = 0")
    f2 = lambda x: x**3 - x - 1
    df2 = lambda x: 3*x**2 - 1
    raiz2, iter2, conv2 = newton_raphson(f2, df2, 1.5)
    print(f"Raíz: {raiz2:.6f}, Iteraciones: {iter2}, Convergió: {conv2}")
