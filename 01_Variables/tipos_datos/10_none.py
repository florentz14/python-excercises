"""
El tipo None en Python
=======================
Tema: Variables (01_Variables_y_Tipos_Datos)
Descripción: None representa ausencia de valor, verificación con is None.
"""
# None es el único valor del tipo NoneType
resultado = None
print("resultado =", resultado)
print("type(None):", type(None))

# Uso típico: valor por defecto, indicar "sin valor"
def buscar(nombre):
    # Simula búsqueda que puede no encontrar nada
    if nombre == "Ana":
        return 25
    return None  # No encontrado

edad = buscar("Ana")
print(f"\nbuscar('Ana'): {edad}")

edad = buscar("X")
print(f"buscar('X'): {edad}")

# Verificar None con 'is' (no con ==)
if edad is None:
    print("No se encontró la edad.")

# None es falsy (evaluado como False en contexto booleano)
print(f"\nbool(None): {bool(None)}")
