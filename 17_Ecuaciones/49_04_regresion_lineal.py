# Archivo: 49_04_regresion_lineal.py
# Descripción: Regresión lineal (mínimos cuadrados)

print("=== 4. Regresión Lineal (Desde Cero) ===\n")


def regresion_lineal(x_datos, y_datos):
    """
    Regresión lineal y = mx + b por mínimos cuadrados.
    Retorna: (pendiente m, intercepto b, R²)
    """
    n = len(x_datos)
    x_media = sum(x_datos) / n
    y_media = sum(y_datos) / n
    suma_xy = sum((x_datos[i] - x_media) * (y_datos[i] - y_media) for i in range(n))
    suma_x2 = sum((x_datos[i] - x_media) ** 2 for i in range(n))
    if suma_x2 == 0:
        return None, None, 0.0
    m = suma_xy / suma_x2
    b = y_media - m * x_media
    y_predicho = [m * x + b for x in x_datos]
    ss_res = sum((y_datos[i] - y_predicho[i]) ** 2 for i in range(n))
    ss_tot = sum((y_datos[i] - y_media) ** 2 for i in range(n))
    r_cuadrado = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0.0
    return m, b, r_cuadrado


def predecir_regresion(m, b, x):
    """Predice y usando la recta de regresión."""
    return m * x + b


if __name__ == "__main__":
    x_reg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_reg = [2.1, 4.2, 5.8, 8.1, 9.9, 12.2, 13.8, 16.1, 18.0, 20.1]

    print(f"Datos X: {x_reg}")
    print(f"Datos Y: {y_reg}")

    m, b, r2 = regresion_lineal(x_reg, y_reg)
    print(f"\nEcuación: y = {m:.4f}x + {b:.4f}")
    print(f"R² (coeficiente de determinación): {r2:.4f}")

    print("\nPredicciones:")
    for x in [11, 12, 15]:
        y_pred = predecir_regresion(m, b, x)
        print(f"  x={x}: y={y_pred:.2f}")

    print("\nComparación datos reales vs predichos:")
    y_predichos = [predecir_regresion(m, b, x) for x in x_reg]
    for i in range(len(x_reg)):
        err = abs(y_reg[i] - y_predichos[i])
        print(f"  x={x_reg[i]}: real={y_reg[i]:.2f}, predicho={y_predichos[i]:.2f}, error={err:.2f}")
