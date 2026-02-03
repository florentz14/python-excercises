#!/usr/bin/env python3
# -------------------------------------------------
# 16_Archivos - Ejercicio 02: Leer un archivo
# open() con modo "r" (por defecto) abre para lectura.
# -------------------------------------------------

nombre_archivo = "ejemplo_01.txt"

# Leer todo el contenido de una vez
with open(nombre_archivo, "r", encoding="utf-8") as f:
    contenido = f.read()

print("--- read() (todo el archivo) ---")
print(contenido)

# Leer línea a línea (útil para archivos grandes)
print("\n--- readline() / iterar ---")
with open(nombre_archivo, "r", encoding="utf-8") as f:
    for i, linea in enumerate(f, 1):
        print(f"Línea {i}: {linea.rstrip()}")

# Leer todas las líneas como lista
with open(nombre_archivo, "r", encoding="utf-8") as f:
    lineas = f.readlines()
print("\n--- readlines() ---")
print(lineas)
