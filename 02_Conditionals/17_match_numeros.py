# -------------------------------------------------
# File Name: 17_match_numeros.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: match con valores numéricos y caso por defecto.
# -------------------------------------------------

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
