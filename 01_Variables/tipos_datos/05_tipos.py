"""
Tipos de datos en Python
=========================
Tema: Variables (01_Variables_y_Tipos_Datos)
Descripción: int, float, str, bool, type(), conversión entre tipos.
"""
# Tipos numéricos
entero = 42
decimal = 3.14
print("int:", entero, "->", type(entero))
print("float:", decimal, "->", type(decimal))

# Strings y booleanos
texto = "Hola"
verdadero = True
falso = False
print("str:", texto, "->", type(texto))
print("bool:", verdadero, "->", type(verdadero))

# Verificar tipo con type()
print("\ntype(entero):", type(entero))

# Conversión entre tipos
num_str = "100"
num_int = int(num_str)
print("\nint('100'):", num_int)

num_float = float("3.14")
print("float('3.14'):", num_float)

str_num = str(42)
print("str(42):", str_num, "->", type(str_num))

# bool() - valores "falsy": 0, 0.0, "", None, [], ()
print("\nbool(1):", bool(1))
print("bool(0):", bool(0))
print("bool(''):", bool(""))
print("bool('hola'):", bool("hola"))
