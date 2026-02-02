"""
Diccionarios - Ejemplo 7: Recorrer con items()
==============================================
Tema: Diccionarios (01_Variables_y_Tipos_Datos)
Descripción: for clave, valor in dic.items() para obtener pares clave-valor.
"""

print("Example 7: Loop with items()")
print("-" * 40)
products = {"laptop": 1200, "phone": 800, "tablet": 400}
print("Products:", products)
for product, price in products.items():
    print(f"{product}: ${price}")
