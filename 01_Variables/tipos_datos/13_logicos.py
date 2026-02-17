"""
Operadores lógicos: and, or, not
=================================
Tema: Variables (01_Variables_y_Tipos_Datos)
Descripción: Operadores lógicos, short-circuit, combinación con comparaciones.
"""
# and, or, not
p = True
q = False
print("p =", p, ", q =", q)
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)
print("not q:", not q)

# Combinar con comparaciones
print("\n--- Con comparaciones ---")
edad = 20
tiene_licencia = True
print("edad >= 18 and tiene_licencia:", edad >= 18 and tiene_licencia)

# Múltiples condiciones
x = 5
print("1 < x < 10:", 1 < x < 10)
print("x > 3 and x < 7:", x > 3 and x < 7)

# or: al menos una verdadera
es_fin_de_semana = False
es_feriado = True
print("\nes_fin_de_semana or es_feriado:", es_fin_de_semana or es_feriado)

# not: negación
llueve = True
print("not llueve:", not llueve)

# Short-circuit: or retorna el primer valor truthy
print("\n--- Short-circuit ---")
print("0 or 42:", 0 or 42)
print("'' or 'default':", "" or "default")
print("1 and 2:", 1 and 2)
