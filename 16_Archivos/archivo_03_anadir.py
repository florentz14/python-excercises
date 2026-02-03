#!/usr/bin/env python3
# -------------------------------------------------
# 16_Archivos - Ejercicio 03: Añadir contenido al final (append)
# open() con modo "a" abre para añadir; no borra lo que ya hay.
# -------------------------------------------------

nombre_archivo = "ejemplo_03_append.txt"

# Crear archivo inicial si no existe
with open(nombre_archivo, "w", encoding="utf-8") as f:
    f.write("Primera línea.\n")

# Añadir más contenido sin borrar lo anterior
with open(nombre_archivo, "a", encoding="utf-8") as f:
    f.write("Línea añadida después.\n")
    f.write("Otra línea más.\n")

print(f"Contenido añadido a '{nombre_archivo}'.")

# Mostrar resultado
with open(nombre_archivo, "r", encoding="utf-8") as f:
    print("\nContenido actual:")
    print(f.read())
