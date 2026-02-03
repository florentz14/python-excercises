"""
Listas - Ejemplo 12: Ordenar, enumerate y zip
==============================================
sorted/sort/reverse, enumerate(), zip() para combinar listas.
"""

print("=== Metodos avanzados (ordenar) ===")
lista = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Lista original: {lista}")
lista_ordenada = sorted(lista)
print(f"Ordenada (sorted): {lista_ordenada}")
lista.sort()
print(f"Despues de sort(): {lista}")
lista.reverse()
print(f"Despues de reverse(): {lista}\n")

print("=== Enumerar elementos ===")
frutas = ["manzana", "banana", "naranja"]
for indice, fruta in enumerate(frutas):
    print(f"  Indice {indice}: {fruta}")
print()

print("=== zip - combinar listas ===")
nombres = ["Ana", "Carlos", "Maria"]
edades = [25, 30, 28]
ciudades = ["Madrid", "Barcelona", "Valencia"]
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"  {nombre}, {edad} anos, {ciudad}")
combinada = list(zip(nombres, edades, ciudades))
print(f"Lista combinada: {combinada}")
