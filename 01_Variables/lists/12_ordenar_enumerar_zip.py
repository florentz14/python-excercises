# -------------------------------------------------
# File Name: 12_ordenar_enumerar_zip.py
# Author: Florentino Báez
# Date: Variables - Lists
# Description: Sort, Enumerate, and Zip.
#              sorted() returns a new sorted list; sort()
#              sorts in place. enumerate() pairs indices with
#              values. zip() combines multiple iterables into
#              tuples element-by-element.
# -------------------------------------------------

print("=== Advanced sorting methods ===")
lista = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original list: {lista}")

lista_ordenada = sorted(lista)            # Returns a new sorted list
print(f"sorted() (new list): {lista_ordenada}")

lista.sort()                              # Sorts the list in place
print(f"After sort() (in place): {lista}")

lista.reverse()                           # Reverses the list in place
print(f"After reverse(): {lista}\n")

print("=== enumerate — index + value ===")
frutas = ["manzana", "banana", "naranja"]
# enumerate() yields (index, element) pairs
for indice, fruta in enumerate(frutas):
    print(f"  Index {indice}: {fruta}")
print()

print("=== zip — combine multiple lists ===")
nombres = ["Ana", "Carlos", "Maria"]
edades = [25, 30, 28]
ciudades = ["Madrid", "Barcelona", "Valencia"]

# zip() pairs elements from each iterable by position
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"  {nombre}, {edad} years, {ciudad}")

# Convert zip object to a list of tuples
combinada = list(zip(nombres, edades, ciudades))
print(f"Combined list: {combinada}")
