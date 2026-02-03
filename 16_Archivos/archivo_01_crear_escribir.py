# -------------------------------------------------
# 16_Archivos - Ejercicio 01: Crear y escribir en un archivo
# open() con modo "w" crea el archivo (o lo sobrescribe) y escribe.
# -------------------------------------------------

# Crear/sobrescribir archivo y escribir una línea
nombre_archivo = "ejemplo_01.txt"
contenido = "Hola, este es el contenido del archivo.\nSegunda línea.\n"

with open(nombre_archivo, "w", encoding="utf-8") as f:
    f.write(contenido)

print(f"Archivo '{nombre_archivo}' creado y escrito correctamente.")

# Alternativa: writelines() para una lista de líneas
lineas = ["Línea A\n", "Línea B\n", "Línea C\n"]
with open("ejemplo_01_lineas.txt", "w", encoding="utf-8") as f:
    f.writelines(lineas)

print("Archivo 'ejemplo_01_lineas.txt' creado con writelines().")
