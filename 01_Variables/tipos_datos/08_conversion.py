"""
Conversión entre tipos de datos
================================
Tema: Variables (01_Variables_y_Tipos_Datos)
Descripción: int(), float(), str(), bool(), list(), tuple(), set(), dict().
"""
# Conversión numérica
print("--- Conversión numérica ---")
print("int(3.9):", int(3.9))      # Trunca decimales
print("float(7):", float(7))
print("int('42'):", int("42"))
print("float('3.14'):", float("3.14"))

# Conversión a string
print("\n--- Conversión a string ---")
print("str(100):", str(100))
print("str(3.14):", str(3.14))
print("str(True):", str(True))

# Conversión a bool (valores truthy/falsy)
print("\n--- Conversión a bool ---")
print("bool(1):", bool(1))
print("bool(0):", bool(0))
print("bool(''):", bool(""))
print("bool('texto'):", bool("texto"))
print("bool([]):", bool([]))
print("bool([1,2]):", bool([1, 2]))

# Conversión entre secuencias
print("\n--- Conversión entre secuencias ---")
lista = [1, 2, 3]
tupla = tuple(lista)
print("tuple([1,2,3]):", tupla)

cadena = "abc"
lista_chars = list(cadena)
print("list('abc'):", lista_chars)

conjunto = set([1, 2, 2, 3])
print("set([1,2,2,3]):", conjunto)
