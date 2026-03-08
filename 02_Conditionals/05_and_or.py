# -------------------------------------------------
# File Name: 05_and_or.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: Combinar condiciones con and (todas verdaderas) y or (al menos una).
# -------------------------------------------------

edad = 25
tiene_entrada = True

# and: ambas deben ser True
if edad >= 18 and tiene_entrada:
    print("Puedes pasar")

# or: al menos una True
hoy_es_lunes = False
hoy_es_feriado = True
if hoy_es_lunes or hoy_es_feriado:
    print("No hay clases")
