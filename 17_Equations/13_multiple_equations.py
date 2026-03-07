# Archivo: 27_05_multiples_ecuaciones.py
# Descripción: Resolver múltiples ecuaciones cuadráticas

from resolver_cuadratica import ecuacion_cuadratica_completa


def resolver_multiples_ecuaciones(ecuaciones):
    """
    Resuelve múltiples ecuaciones cuadráticas.

    Parámetros:
    - ecuaciones: Lista de tuplas (a, b, c)
    """
    resultados = []
    for i, (a, b, c) in enumerate(ecuaciones, 1):
        print(f"\nEcuación {i}: {a}x² + {b}x + {c} = 0")
        try:
            soluciones = ecuacion_cuadratica_completa(a, b, c)
            resultados.append((a, b, c, soluciones))
            if soluciones:
                if len(soluciones) == 2:
                    print(f"  Soluciones: x₁ = {soluciones[0]:.4f}, x₂ = {soluciones[1]:.4f}")
                else:
                    print(f"  Solución: x = {soluciones[0]:.4f} (raíz doble)")
            else:
                print(f"  Sin soluciones reales")
        except Exception as e:
            print(f"  Error: {e}")
            resultados.append((a, b, c, None))

    return resultados


if __name__ == "__main__":
    print("=== Versión 5: Resolver Múltiples Ecuaciones ===\n")
    print("Resolviendo múltiples ecuaciones:")
    ecuaciones_ejemplo = [
        (1, 8, 12),
        (1, 2, 1),
        (3, -8, 6),
        (1, 0, -4),   # x² - 4 = 0
        (2, -5, 2)    # 2x² - 5x + 2 = 0
    ]
    resolver_multiples_ecuaciones(ecuaciones_ejemplo)
