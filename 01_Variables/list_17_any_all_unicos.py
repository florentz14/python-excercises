"""
Listas - Ejemplo 17: any, all y elementos únicos
=================================================
any()/all() con generadores; quitar duplicados manteniendo orden (dict.fromkeys).
"""

print("=== any y all ===")
numeros1 = [2, 4, 6, 8]
numeros2 = [2, 4, 5, 8]
print(f"Lista 1: {numeros1}")
print(f"  Todos pares? {all(x % 2 == 0 for x in numeros1)}")
print(f"Lista 2: {numeros2}")
print(f"  Alguno par? {any(x % 2 == 0 for x in numeros2)}")
print(f"  Todos pares? {all(x % 2 == 0 for x in numeros2)}\n")

print("=== Elementos unicos (manteniendo orden) ===")
con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5]
sin_duplicados = list(dict.fromkeys(con_duplicados))
print(f"Original: {con_duplicados}")
print(f"Sin duplicados: {sin_duplicados}")
