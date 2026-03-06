# Archivo: 27_07_verificacion.py
# Descripción: Verificación de soluciones de ecuaciones cuadráticas

from resolver_cuadratica import ecuacion_cuadratica_completa


def verificar_soluciones(a, b, c, soluciones):
    """
    Verifica que las soluciones sean correctas.
    """
    print(f"\nVerificando soluciones para {a}x² + {b}x + {c} = 0:")
    print(f"Soluciones encontradas: {soluciones}")

    if not soluciones:
        print("No hay soluciones reales para verificar")
        return

    for i, x in enumerate(soluciones, 1):
        resultado = a*x**2 + b*x + c
        print(f"  x_{i} = {x}")
        print(f"  Verificación: {a}({x})² + {b}({x}) + {c} = {resultado}")
        if abs(resultado) < 1e-10:
            print(f"  [OK] Correcto (error: {abs(resultado):.2e})")
        else:
            print(f"  [AVISO] Error: {abs(resultado):.2e}")


if __name__ == "__main__":
    print("=== Versión 7: Verificación de Soluciones ===\n")
    print("Verificando soluciones de los ejemplos:")
    verificar_soluciones(1, 8, 12, ecuacion_cuadratica_completa(1, 8, 12))
    verificar_soluciones(1, 2, 1, ecuacion_cuadratica_completa(1, 2, 1))
