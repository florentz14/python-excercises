"""
Flujos de control: if, for, while
==================================
Tema: Variables (01_Variables_y_Tipos_Datos)
Descripción: Introducción a estructuras de control de flujo.
"""
# if / elif / else
edad = 17
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

# elif: múltiples condiciones
nota = 85
if nota >= 90:
    print("\nExcelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")

# for: iterar secuencia
print("\n--- for ---")
for i in range(3):
    print("Hola", i + 1)

for letra in "abc":
    print(letra, end=" ")
print()

# while: repetir mientras condición sea verdadera
print("\n--- while ---")
n = 0
while n < 3:
    print("n =", n)
    n += 1
