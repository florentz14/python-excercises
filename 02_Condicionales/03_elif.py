"""
Condicional - Ejemplo 3: if / elif / else
==========================================
Tema: Condicionales (02_Condicionales)
Descripción: Varias ramas con elif; solo se ejecuta la primera condición verdadera.
"""

nota = 75

if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
elif nota >= 60:
    letra = "D"
else:
    letra = "F"

print(f"Nota {nota} → {letra}")
