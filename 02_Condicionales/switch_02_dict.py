"""
Switch - Ejemplo 2: Emular switch con diccionario
=================================================
Tema: Condicionales - Switch (02_Condicionales)
Descripción: Mapear valor → resultado con un diccionario (sin if/elif).
"""

opcion = "B"

# Diccionario: clave = caso, valor = resultado
resultados = {
    "A": "Has elegido A",
    "B": "Has elegido B",
    "C": "Has elegido C",
}

# get(clave, valor_por_defecto) para el caso "default"
mensaje = resultados.get(opcion, "Opción no válida")
print(mensaje)
