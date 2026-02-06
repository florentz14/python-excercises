# Archivo: 34_02_optimizada.py
# Descripción: Calcular rango con información adicional

from rango_matriz_util import A, calcular_rango_matriz


if __name__ == "__main__":
    print("=== Versión 2: Optimizada y Mejorada ===\n")
    rango, info = calcular_rango_matriz(A.copy())
