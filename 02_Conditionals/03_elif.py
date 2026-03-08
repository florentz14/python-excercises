# -------------------------------------------------
# File Name: 03_elif.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: Varias ramas con elif; solo se ejecuta la primera condición verdadera.
# -------------------------------------------------

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
