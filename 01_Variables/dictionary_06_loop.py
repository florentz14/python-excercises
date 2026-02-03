"""
Diccionarios - Ejemplo 6: Recorrer un diccionario
=================================================
Tema: Diccionarios (01_Variables_y_Tipos_Datos)
Descripción: Itera sobre las claves y accede a valores con dic[key].
"""

print("Example 6: Loop through dictionary")
print("-" * 40)
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
print("Scores:", scores)
for key in scores:
    print(f"{key}: {scores[key]}")
