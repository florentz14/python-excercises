#!/usr/bin/env python3
# -------------------------------------------------
# 16_Archivos - Ejercicio 06: Eliminar un archivo
# Path.unlink() o os.remove() eliminan el archivo (no carpetas).
# -------------------------------------------------

from pathlib import Path

# Crear un archivo de prueba para eliminar
archivo_prueba = Path("archivo_para_eliminar.txt")
archivo_prueba.write_text("Contenido temporal.\n", encoding="utf-8")
print(f"Archivo '{archivo_prueba}' creado.")

# Eliminar con pathlib
if archivo_prueba.exists():
    archivo_prueba.unlink()
    print(f"Archivo '{archivo_prueba}' eliminado con Path.unlink().")

# Alternativa con os
import os
archivo_prueba2 = Path("archivo_para_eliminar_2.txt")
archivo_prueba2.write_text("Otro temporal.\n", encoding="utf-8")
if archivo_prueba2.is_file():
    os.remove(archivo_prueba2)
    print(f"Archivo '{archivo_prueba2}' eliminado con os.remove().")

# Eliminar solo si existe (evitar error)
ruta = Path("no_existe.txt")
if ruta.exists():
    ruta.unlink()
else:
    print("\n'no_existe.txt' no existe; no hay nada que eliminar.")
