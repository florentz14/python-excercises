"""
Ejercicio: Cálculo de Áreas de Figuras Geométricas

Programa que calcula el área de diferentes figuras geométricas.
"""

import math


def area_triangulo(base, altura):
    """Calcula el área de un triángulo."""
    return (base * altura) / 2


def area_cuadrado(lado):
    """Calcula el área de un cuadrado."""
    return lado ** 2


def area_rectangulo(largo, ancho):
    """Calcula el área de un rectángulo."""
    return largo * ancho


def area_circulo(radio):
    """Calcula el área de un círculo."""
    return math.pi * (radio ** 2)


def area_rombo(diagonal1, diagonal2):
    """Calcula el área de un rombo."""
    return (diagonal1 * diagonal2) / 2


def area_trapecio(base1, base2, altura):
    """Calcula el área de un trapecio."""
    return ((base1 + base2) * altura) / 2


def area_pentagono(lado, apotema):
    """Calcula el área de un pentágono regular."""
    perimetro = 5 * lado
    return (perimetro * apotema) / 2


def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n" + "="*50)
    print("CALCULADORA DE ÁREAS")
    print("="*50)
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Rectángulo")
    print("4. Círculo")
    print("5. Rombo")
    print("6. Trapecio")
    print("7. Pentágono")
    print("8. Salir")
    print("="*50)


def main():
    """Función principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-8): ")

        if opcion == "1":
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
            area = area_triangulo(base, altura)
            print(f"Área del triángulo: {area:.2f} unidades²")

        elif opcion == "2":
            lado = float(input("Ingresa el lado del cuadrado: "))
            area = area_cuadrado(lado)
            print(f"Área del cuadrado: {area:.2f} unidades²")

        elif opcion == "3":
            largo = float(input("Ingresa el largo del rectángulo: "))
            ancho = float(input("Ingresa el ancho del rectángulo: "))
            area = area_rectangulo(largo, ancho)
            print(f"Área del rectángulo: {area:.2f} unidades²")

        elif opcion == "4":
            radio = float(input("Ingresa el radio del círculo: "))
            area = area_circulo(radio)
            print(f"Área del círculo: {area:.2f} unidades²")

        elif opcion == "5":
            diagonal1 = float(input("Ingresa la primera diagonal del rombo: "))
            diagonal2 = float(input("Ingresa la segunda diagonal del rombo: "))
            area = area_rombo(diagonal1, diagonal2)
            print(f"Área del rombo: {area:.2f} unidades²")

        elif opcion == "6":
            base1 = float(input("Ingresa la primera base del trapecio: "))
            base2 = float(input("Ingresa la segunda base del trapecio: "))
            altura = float(input("Ingresa la altura del trapecio: "))
            area = area_trapecio(base1, base2, altura)
            print(f"Área del trapecio: {area:.2f} unidades²")

        elif opcion == "7":
            lado = float(input("Ingresa el lado del pentágono: "))
            apotema = float(input("Ingresa el apotema del pentágono: "))
            area = area_pentagono(lado, apotema)
            print(f"Área del pentágono: {area:.2f} unidades²")

        elif opcion == "8":
            print("\n¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")


if __name__ == "__main__":
    main()
