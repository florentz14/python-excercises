# Archivo: 34_07_interactiva.py
# Descripción: Función interactiva para calcular el rango de matrices

import numpy as np
from rango_matriz_util import A, calcular_rango_matriz


def rango_matriz_interactivo():
    """
    Función interactiva para calcular el rango de matrices.
    """
    while True:
        try:
            print("\n" + "=" * 60)
            print("CALCULADORA DE RANGO DE MATRIZ")
            print("=" * 60)
            print("\nOpciones:")
            print("1. Usar matriz de ejemplo")
            print("2. Crear matriz personalizada")
            print("3. Salir")

            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":
                matriz = A.copy()
                print("\nMatriz de ejemplo:")
                print(matriz)

            elif opcion == "2":
                filas = int(input("Número de filas: "))
                columnas = int(input("Número de columnas: "))
                print(f"\nIngrese los elementos de la matriz ({filas}x{columnas}):")
                print("(Separados por espacios, una fila por línea)")

                elementos = []
                for i in range(filas):
                    fila_str = input(f"Fila {i+1}: ")
                    fila = [float(x) for x in fila_str.split()]
                    if len(fila) != columnas:
                        print(f"Error: La fila debe tener {columnas} elementos")
                        break
                    elementos.append(fila)
                else:
                    matriz = np.array(elementos)

            elif opcion == "3":
                print("Hasta luego.")
                break

            else:
                print("[ERROR] Opción no válida")
                continue

            rango, info = calcular_rango_matriz(matriz, mostrar_info=True)

            continuar = input("\n¿Analizar otra matriz? (s/n): ").lower()
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
    print("=== Versión 7: Función Interactiva ===\n")
    rango_matriz_interactivo()
