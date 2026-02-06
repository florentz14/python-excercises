"""
Listas - Ejemplo 14: Slice avanzado
===================================
[:n], [-n:], [a:b], [::paso], [::-1] para invertir.
"""

print("=== Slice avanzado ===")
lista = list(range(10))
print(f"Lista: {lista}")
print(f"Primeros 3: {lista[:3]}")
print(f"Ultimos 3: {lista[-3:]}")
print(f"Del indice 2 al 7: {lista[2:7]}")
print(f"Cada 2 elementos: {lista[::2]}")
print(f"Invertida: {lista[::-1]}")
