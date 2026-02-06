"""
if.py - Ejemplo 3: Asignar nota según puntuación
================================================
Tema: Condicionales (02_Condicionales)
Descripción: if/elif/else para convertir score en letra (A–F).
"""

print("Example 3: Grade Assignment")
print("-" * 40)
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")
