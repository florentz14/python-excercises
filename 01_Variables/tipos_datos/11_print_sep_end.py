"""
Control de print(): sep y end
==============================
Tema: Variables (01_Variables_y_Tipos_Datos)
Descripción: sep (separador entre argumentos), end (final de línea).
"""
# sep: separador entre múltiples argumentos (default: espacio)
print(1, 2, 3)
print(1, 2, 3, sep="-")
print(1, 2, 3, sep=", ")
print("a", "b", "c", sep="")

# end: qué imprimir al final (default: \n)
print("Sin salto", end="")
print(" de línea")
print("Línea 1", end=" | ")
print("Línea 2", end=" | ")
print("Línea 3")

# Combinar sep y end
print(10, 20, 30, sep=" + ", end=" = ")
print(60)
