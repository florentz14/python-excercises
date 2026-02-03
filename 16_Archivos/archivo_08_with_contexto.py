# -------------------------------------------------
# 16_Archivos - Ejercicio 08: Usar "with" (gestor de contexto)
# with open(...) cierra el archivo automáticamente al salir del bloque,
# incluso si hay una excepción. Evita olvidar .close() y fugas de recursos.
# -------------------------------------------------

# Sin "with": hay que cerrar manualmente (no recomendado)
# f = open("archivo.txt", "r")
# contenido = f.read()
# f.close()  # Si hay error antes, el archivo puede quedar abierto

# Con "with": el archivo se cierra solo al terminar el bloque
nombre = "ejemplo_08_with.txt"
with open(nombre, "w", encoding="utf-8") as archivo:
    archivo.write("Escrito dentro del bloque with.\n")
    # No hace falta archivo.close()
# Aquí el archivo ya está cerrado

print(f"Archivo '{nombre}' escrito y cerrado correctamente.")

# Leer con with
with open(nombre, "r", encoding="utf-8") as archivo:
    texto = archivo.read()
    print("Contenido leído:")
    print(texto)

# Varios archivos en el mismo with (Python 3.10+)
with (
    open("ejemplo_08_a.txt", "w", encoding="utf-8") as a,
    open("ejemplo_08_b.txt", "w", encoding="utf-8") as b,
):
    a.write("Archivo A\n")
    b.write("Archivo B\n")
print("Archivos A y B creados con un solo with.")
