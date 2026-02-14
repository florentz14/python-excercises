"""
Entrada de datos con input()
=============================
Tema: Variables (01_Variables_y_Tipos_Datos)
Descripción: input() siempre retorna str, conversión a int/float, validación básica.
"""
# input() siempre retorna un string
nombre = input("Escribe tu nombre: ")
print(f"Hola, {nombre}!")

# Para números hay que convertir explícitamente
edad_str = input("\n¿Cuántos años tienes? ")
edad = int(edad_str)
print(f"En 10 años tendrás {edad + 10} años.")

# Conversión directa en la misma línea
precio = float(input("\nIntroduce un precio: $"))
cantidad = int(input("Introduce la cantidad: "))
total = precio * cantidad
print(f"Total: ${total:,.2f}")

# input() con mensaje vacío o por defecto
respuesta = input("\n¿Continuar? (s/n): ").strip().lower()
if respuesta == "s":
    print("Continuando...")
else:
    print("Finalizando.")
