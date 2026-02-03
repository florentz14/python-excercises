# -------------------------------------------------
# 16_Archivos - Ejercicio 04: Listar archivos y carpetas de un directorio
# os.listdir() o pathlib.Path.iterdir() listan el contenido.
# -------------------------------------------------

import os
from pathlib import Path

# Ruta del directorio actual (donde está este script)
directorio = Path(__file__).parent

# Con pathlib
print("--- Contenido del directorio (pathlib) ---")
for item in directorio.iterdir():
    tipo = "📁 carpeta" if item.is_dir() else "📄 archivo"
    print(f"  {tipo}: {item.name}")

# Con os.listdir()
print("\n--- Contenido del directorio (os.listdir) ---")
for nombre in os.listdir(directorio):
    ruta = directorio / nombre
    tipo = "carpeta" if ruta.is_dir() else "archivo"
    print(f"  {tipo}: {nombre}")

# Solo archivos .py
print("\n--- Solo archivos .py ---")
for f in directorio.glob("*.py"):
    print(f"  {f.name}")
