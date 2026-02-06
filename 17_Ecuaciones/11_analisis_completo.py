# Archivo: 27_03_analisis_completo.py
# Descripción: Análisis completo de una ecuación cuadrática

from resolver_cuadratica import ecuacion_cuadratica_completa


def analizar_ecuacion_cuadratica(a, b, c):
    """
    Analiza una ecuación cuadrática completamente.
    """
    print("=" * 60)
    print(f"ANÁLISIS DE LA ECUACIÓN: {a}x² + {b}x + {c} = 0")
    print("=" * 60)

    if a == 0:
        print("[ERROR] No es una ecuación cuadrática (a = 0)")
        return None

    discriminante = b**2 - 4*a*c
    print(f"\n1. Discriminante (Δ = b² - 4ac):")
    print(f"   Δ = {b}² - 4({a})({c}) = {discriminante}")

    print(f"\n2. Tipo de soluciones:")
    if discriminante > 0:
        print("   Dos soluciones reales distintas")
        print("   -> La parábola corta al eje X en dos puntos")
    elif discriminante == 0:
        print("   Una solución real (raíz doble)")
        print("   -> La parábola toca al eje X en un punto (vértice)")
    else:
        print("   [AVISO] Dos soluciones complejas conjugadas")
        print("   -> La parábola no corta al eje X (no tiene raíces reales)")

    print(f"\n3. Soluciones:")
    soluciones = ecuacion_cuadratica_completa(a, b, c)
    if soluciones:
        if len(soluciones) == 2:
            print(f"   x₁ = {soluciones[0]}")
            print(f"   x₂ = {soluciones[1]}")
            if discriminante > 0:
                print(f"\n   Verificación:")
                print(f"   x₁ + x₂ = {soluciones[0] + soluciones[1]} (debería ser -b/a = {-b/a})")
                print(f"   x₁ · x₂ = {soluciones[0] * soluciones[1]} (debería ser c/a = {c/a})")
        else:
            print(f"   x = {soluciones[0]} (raíz doble)")
    else:
        print("   No hay soluciones reales")

    print(f"\n4. Vértice de la parábola:")
    x_vertice = -b / (2*a)
    y_vertice = a*x_vertice**2 + b*x_vertice + c
    print(f"   V = ({x_vertice:.4f}, {y_vertice:.4f})")

    print(f"\n5. Concavidad:")
    if a > 0:
        print("   Parábola abre hacia arriba (a > 0)")
    else:
        print("   Parábola abre hacia abajo (a < 0)")

    print("=" * 60)
    return soluciones


if __name__ == "__main__":
    print("=== Versión 3: Con Análisis Completo ===\n")
    print("Análisis de ejemplos:")
    analizar_ecuacion_cuadratica(1, 8, 12)
    print()
    analizar_ecuacion_cuadratica(1, 2, 1)
