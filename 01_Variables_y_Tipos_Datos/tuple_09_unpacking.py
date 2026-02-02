"""
Tuplas - Ejemplo 9: Desempaquetado de tuplas
============================================
Tema: Tuplas (01_Variables_y_Tipos_Datos)
Descripción: Asigna cada elemento de la tupla a variables con name, age, profession = person.
"""

print("Example 9: Tuple unpacking")
print("-" * 40)
person = ("John", 25, "Engineer")
name, age, profession = person
print("Original tuple:", person)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")
