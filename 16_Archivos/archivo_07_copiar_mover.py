#!/usr/bin/env python3
# -------------------------------------------------
# 16_Archivos - Ejercicio 07: Copiar y mover archivos
# shutil.copy() / copy2() para copiar; shutil.move() para mover/renombrar.
# -------------------------------------------------

import shutil
from pathlib import Path

# Crear archivo de origen
origen = Path("ejemplo_07_origen.txt")
origen.write_text("Contenido del archivo origen.\n", encoding="utf-8")
print(f"Archivo origen creado: {origen}")

# Copiar archivo (shutil.copy: contenido; copy2: también metadatos)
destino_copia = Path("ejemplo_07_copia.txt")
shutil.copy2(origen, destino_copia)
print(f"Copiado a: {destino_copia}")

# Mover (o renombrar) archivo
destino_mover = Path("ejemplo_07_movido.txt")
shutil.move(str(origen), str(destino_mover))
print(f"Movido/renombrado a: {destino_mover}")

# Verificar: origen ya no existe, los otros sí
print(f"\n¿Origen existe? {origen.exists()}")
print(f"¿Copia existe? {destino_copia.exists()}")
print(f"¿Movido existe? {destino_mover.exists()}")

# Limpieza opcional (descomenta si quieres borrar al final)
# destino_copia.unlink()
# destino_mover.unlink()
