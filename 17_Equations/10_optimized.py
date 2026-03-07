# Archivo: 27_02_optimizada.py
# Descripción: Versión optimizada con soporte para números complejos

from resolver_cuadratica import ecuacion_cuadratica_completa


if __name__ == "__main__":
    print("=== Versión 2: Optimizada (con Números Complejos) ===\n")
    print("Pruebas versión optimizada:")
    print(f"x² + 8x + 12 = 0: {ecuacion_cuadratica_completa(1, 8, 12)}")
    print(f"x² + 2x + 1 = 0: {ecuacion_cuadratica_completa(1, 2, 1)}")
    print(f"3x² - 8x + 6 = 0: {ecuacion_cuadratica_completa(3, -8, 6)}")
    print(f"x² + 1 = 0 (solo complejas): {ecuacion_cuadratica_completa(1, 0, 1)}")
