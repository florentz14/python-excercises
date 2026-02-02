"""
Condicional - Ejemplo 6: Operador ternario
==========================================
Tema: Condicionales (02_Condicionales)
Descripción: valor_si_true if condición else valor_si_false (en una línea).
"""

edad = 20

# Forma larga:
# if edad >= 18:
#     mensaje = "Mayor"
# else:
#     mensaje = "Menor"

mensaje = "Mayor" if edad >= 18 else "Menor"
print(mensaje)

# Otro ejemplo: máximo de dos números
a, b = 5, 9
maximo = a if a > b else b
print(f"max({a}, {b}) = {maximo}")
