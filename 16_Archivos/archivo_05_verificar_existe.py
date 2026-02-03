# -------------------------------------------------
# 16_Archivos - Ejercicio 05: Verificar si un archivo o carpeta existe
# Path.exists(), Path.is_file(), Path.is_dir()
# -------------------------------------------------

from pathlib import Path

# Comprobar si existe (archivo o carpeta)
ruta_archivo = Path("ejemplo_01.txt")
ruta_carpeta = Path(__file__).parent

if ruta_archivo.exists():
    print(f"'{ruta_archivo}' existe.")
else:
    print(f"'{ruta_archivo}' no existe.")

# Diferenciar archivo y carpeta
if ruta_archivo.is_file():
    print("  → Es un archivo.")
if ruta_archivo.is_dir():
    print("  → Es un directorio.")

if ruta_carpeta.exists() and ruta_carpeta.is_dir():
    print(f"\n'{ruta_carpeta.name}' es un directorio que existe.")

# Comprobar antes de leer (evitar FileNotFoundError)
archivo_a_leer = Path("ejemplo_01.txt")
if archivo_a_leer.is_file():
    print(f"\nPodemos leer '{archivo_a_leer}' de forma segura.")
else:
    print(f"\nNo se puede leer: '{archivo_a_leer}' no es un archivo o no existe.")
