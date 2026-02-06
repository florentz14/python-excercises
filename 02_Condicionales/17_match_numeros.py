"""
Switch - Ejemplo 4: match / case con números
===========================================
Tema: Condicionales - Switch (02_Condicionales)
Descripción: match con valores numéricos y caso por defecto.
"""

numero = 2

match numero:
    case 1:
        print("Uno")
    case 2:
        print("Dos")
    case 3:
        print("Tres")
    case _:
        print("Otro número")
