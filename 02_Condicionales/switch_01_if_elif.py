"""
Switch - Ejemplo 1: Emular switch con if / elif
===============================================
Tema: Condicionales - Switch (02_Condicionales)
Descripción: Varios casos (como switch) usando if/elif/else.
"""

dia = 3  # 1=Lunes, 2=Martes, ...

if dia == 1:
    nombre = "Lunes"
elif dia == 2:
    nombre = "Martes"
elif dia == 3:
    nombre = "Miércoles"
elif dia == 4:
    nombre = "Jueves"
elif dia == 5:
    nombre = "Viernes"
elif dia == 6:
    nombre = "Sábado"
elif dia == 7:
    nombre = "Domingo"
else:
    nombre = "Día no válido"

print(f"Día {dia} → {nombre}")
