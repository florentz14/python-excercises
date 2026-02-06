# Archivo: 31_08_interactiva.py
# Descripción: Función interactiva para calcular integrales

from integracion_util import f_original, integrar_funcion


def integracion_interactiva():
    """
    Función interactiva para calcular integrales.
    """
    while True:
        try:
            print("\n" + "=" * 60)
            print("CALCULADORA DE INTEGRALES")
            print("=" * 60)
            print("\nOpciones:")
            print("1. Función cuadrática: -x^2 - 2x + 8")
            print("2. Función personalizada")
            print("3. Salir")

            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":
                a = float(input("Límite inferior (a): "))
                b = float(input("Límite superior (b): "))
                integrar_funcion(f_original, a, b)

            elif opcion == "2":
                print("\nIngrese la función en términos de x (ejemplo: x**2 + 2*x + 1)")
                funcion_str = input("f(x) = ")
                a = float(input("Límite inferior (a): "))
                b = float(input("Límite superior (b): "))

                def funcion_personalizada(x):
                    return eval(funcion_str)

                integrar_funcion(funcion_personalizada, a, b)

            elif opcion == "3":
                print("Hasta luego.")
                break

            else:
                print("[ERROR] Opción no válida")

        except ValueError:
            print("[ERROR] Por favor ingrese números válidos")
        except SyntaxError:
            print("[ERROR] Error en la sintaxis de la función")
        except KeyboardInterrupt:
            print("\n\nOperación cancelada")
            break
        except Exception as e:
            print(f"[ERROR] {e}")


if __name__ == "__main__":
    print("=== Versión 8: Función Interactiva ===\n")
    integracion_interactiva()
