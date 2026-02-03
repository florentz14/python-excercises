# Archivo: 27_06_interactiva.py
# Descripción: Función interactiva para resolver ecuaciones cuadráticas

from resolver_cuadratica import ecuacion_cuadratica_completa


def ecuacion_cuadratica_interactiva():
    """
    Función interactiva para resolver ecuaciones cuadráticas.
    """
    while True:
        try:
            print("\n" + "=" * 50)
            print("RESOLVER ECUACIÓN CUADRÁTICA")
            print("=" * 50)
            print("Forma: Ax² + Bx + C = 0\n")

            a = float(input("Ingrese el coeficiente A (A ≠ 0): "))
            if a == 0:
                print("[ERROR] A no puede ser cero")
                continue

            b = float(input("Ingrese el coeficiente B: "))
            c = float(input("Ingrese el coeficiente C: "))

            print(f"\nEcuación: {a}x² + {b}x + {c} = 0")

            soluciones = ecuacion_cuadratica_completa(a, b, c)

            if soluciones:
                if len(soluciones) == 2:
                    print(f"\n[OK] Dos soluciones:")
                    print(f"   x₁ = {soluciones[0]}")
                    print(f"   x₂ = {soluciones[1]}")
                else:
                    print(f"\n[OK] Una solución (raíz doble):")
                    print(f"   x = {soluciones[0]}")
            else:
                print("\n[AVISO] No hay soluciones reales (soluciones complejas)")
                soluciones_complejas = ecuacion_cuadratica_completa(a, b, c, solo_reales=False)
                print(f"   x₁ = {soluciones_complejas[0]}")
                print(f"   x₂ = {soluciones_complejas[1]}")

            continuar = input("\n¿Resolver otra ecuación? (s/n): ").lower()
            if continuar != 's':
                break

        except ValueError:
            print("[ERROR] Por favor ingrese números válidos")
        except KeyboardInterrupt:
            print("\n\nOperación cancelada")
            break
        except Exception as e:
            print(f"[ERROR] {e}")


if __name__ == "__main__":
    print("=== Versión 6: Función Interactiva ===\n")
    ecuacion_cuadratica_interactiva()
