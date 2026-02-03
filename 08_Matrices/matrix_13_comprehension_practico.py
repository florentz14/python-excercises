"""
08_Matrices - Crear matriz por comprensión y ejemplo práctico (notas)
======================================================================
Ejemplos 19-20: tabla de multiplicar, matriz de notas de estudiantes.
"""

# Matriz 4x4 tabla de multiplicar (comprehension)
mult = [[i * j for j in range(1, 5)] for i in range(1, 5)]
print("Tabla de multiplicar (4x4):")
for row in mult:
    print(row)

# Ejemplo práctico: notas por estudiante
grades = [
    ["Math", "Science", "English"],
    ["Alice", 85, 90, 88],
    ["Bob", 78, 88, 82],
    ["Charlie", 92, 95, 90],
]
print("\nNotas (cabecera + filas por estudiante):")
for row in grades:
    print(row)
print("Nota de Bob en Math:", grades[2][1])
print("Todas las notas de Charlie:", grades[3][1:])
