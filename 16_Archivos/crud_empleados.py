#!/usr/bin/env python3
# -------------------------------------------------
# 16_Archivos - CRUD de empleados con archivos (JSON)
# Crear, listar, editar, eliminar registros y eliminar archivo.
# -------------------------------------------------

import json
from pathlib import Path

# Ruta del archivo de datos (misma carpeta que este script)
CARPETA = Path(__file__).parent
ARCHIVO_DATOS = CARPETA / "empleados.json"


def cargar_empleados() -> list[dict]:
    """Lee el archivo JSON y devuelve la lista de empleados. Si no existe, devuelve []."""
    if not ARCHIVO_DATOS.is_file():
        return []
    with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_empleados(empleados: list[dict]) -> None:
    """Guarda la lista de empleados en el archivo JSON."""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(empleados, f, indent=2, ensure_ascii=False)


def generar_id(empleados: list[dict]) -> int:
    """Devuelve el siguiente ID disponible (máximo actual + 1)."""
    if not empleados:
        return 1
    return max(e["id"] for e in empleados) + 1


def mostrar_empleado(e: dict) -> None:
    """Imprime un empleado formateado."""
    print(f"  ID: {e['id']}")
    print(f"  Nombre: {e['nombre']}")
    print(f"  Puesto: {e['puesto']}")
    print(f"  Departamento: {e['departamento']}")
    print(f"  Salario: {e['salario']}")
    print(f"  Email: {e['email']}")


# --- CREAR ---
def crear_empleado(empleados: list[dict]) -> list[dict]:
    """Pide datos por teclado, crea un empleado y lo añade a la lista. Devuelve la lista actualizada."""
    print("\n--- Crear empleado ---")
    nombre = input("Nombre: ").strip()
    puesto = input("Puesto: ").strip()
    departamento = input("Departamento: ").strip()
    try:
        salario = float(input("Salario: ").strip().replace(",", "."))
    except ValueError:
        salario = 0.0
    email = input("Email: ").strip()

    nuevo = {
        "id": generar_id(empleados),
        "nombre": nombre,
        "puesto": puesto,
        "departamento": departamento,
        "salario": salario,
        "email": email,
    }
    empleados.append(nuevo)
    guardar_empleados(empleados)
    print(f"Empleado creado con ID {nuevo['id']}.")
    return empleados


# --- LISTAR ---
def listar_empleados(empleados: list[dict]) -> None:
    """Muestra todos los empleados."""
    print("\n--- Listado de empleados ---")
    if not empleados:
        print("No hay empleados registrados.")
        return
    for e in empleados:
        mostrar_empleado(e)
        print("-" * 40)


# --- BUSCAR POR ID ---
def buscar_por_id(empleados: list[dict], id_buscar: int) -> dict | None:
    """Devuelve el empleado con ese ID o None."""
    for e in empleados:
        if e["id"] == id_buscar:
            return e
    return None


# --- EDITAR ---
def editar_empleado(empleados: list[dict]) -> list[dict]:
    """Pide ID, modifica los campos que el usuario indique y guarda."""
    print("\n--- Editar empleado ---")
    if not empleados:
        print("No hay empleados para editar.")
        return empleados
    try:
        id_editar = int(input("ID del empleado a editar: ").strip())
    except ValueError:
        print("ID no válido.")
        return empleados

    emp = buscar_por_id(empleados, id_editar)
    if not emp:
        print(f"No existe un empleado con ID {id_editar}.")
        return empleados

    print("Deja en blanco para no cambiar.")
    nombre = input(f"Nuevo nombre [{emp['nombre']}]: ").strip()
    puesto = input(f"Nuevo puesto [{emp['puesto']}]: ").strip()
    departamento = input(f"Nuevo departamento [{emp['departamento']}]: ").strip()
    salario_str = input(f"Nuevo salario [{emp['salario']}]: ").strip()
    email = input(f"Nuevo email [{emp['email']}]: ").strip()

    if nombre:
        emp["nombre"] = nombre
    if puesto:
        emp["puesto"] = puesto
    if departamento:
        emp["departamento"] = departamento
    if salario_str:
        try:
            emp["salario"] = float(salario_str.replace(",", "."))
        except ValueError:
            pass
    if email:
        emp["email"] = email

    guardar_empleados(empleados)
    print("Empleado actualizado.")
    return empleados


# --- ELIMINAR REGISTRO ---
def eliminar_registro(empleados: list[dict]) -> list[dict]:
    """Pide ID, elimina ese empleado de la lista y guarda el archivo."""
    print("\n--- Eliminar registro ---")
    if not empleados:
        print("No hay empleados para eliminar.")
        return empleados
    try:
        id_eliminar = int(input("ID del empleado a eliminar: ").strip())
    except ValueError:
        print("ID no válido.")
        return empleados

    emp = buscar_por_id(empleados, id_eliminar)
    if not emp:
        print(f"No existe un empleado con ID {id_eliminar}.")
        return empleados

    confirmar = input(f"¿Eliminar a {emp['nombre']}? (s/n): ").strip().lower()
    if confirmar == "s":
        empleados = [e for e in empleados if e["id"] != id_eliminar]
        guardar_empleados(empleados)
        print("Registro eliminado.")
    else:
        print("Operación cancelada.")
    return empleados


# --- ELIMINAR ARCHIVO ---
def eliminar_archivo(empleados: list[dict]) -> list[dict]:
    """Borra el archivo de datos y devuelve lista vacía."""
    print("\n--- Eliminar archivo de datos ---")
    if not ARCHIVO_DATOS.exists():
        print("El archivo de datos no existe.")
        return []
    confirmar = input("¿Borrar el archivo y todos los registros? (s/n): ").strip().lower()
    if confirmar == "s":
        ARCHIVO_DATOS.unlink()
        print("Archivo eliminado. La lista de empleados queda vacía.")
        return []
    print("Operación cancelada.")
    return empleados


def ver_uno(empleados: list[dict]) -> None:
    """Muestra un empleado por ID."""
    print("\n--- Ver empleado por ID ---")
    if not empleados:
        print("No hay empleados registrados.")
        return
    try:
        id_ver = int(input("ID del empleado: ").strip())
    except ValueError:
        print("ID no válido.")
        return
    emp = buscar_por_id(empleados, id_ver)
    if emp:
        mostrar_empleado(emp)
    else:
        print(f"No existe un empleado con ID {id_ver}.")


def menu() -> None:
    """Menú principal del CRUD."""
    empleados = cargar_empleados()

    while True:
        print("\n" + "=" * 50)
        print("  CRUD EMPLEADOS (archivo: empleados.json)")
        print("=" * 50)
        print("  1. Crear empleado")
        print("  2. Listar todos los empleados")
        print("  3. Ver empleado por ID")
        print("  4. Editar empleado")
        print("  5. Eliminar registro (un empleado)")
        print("  6. Eliminar archivo (borrar todos los datos)")
        print("  0. Salir")
        print("=" * 50)
        opcion = input("Opción: ").strip()

        if opcion == "1":
            empleados = crear_empleado(empleados)
        elif opcion == "2":
            listar_empleados(empleados)
        elif opcion == "3":
            ver_uno(empleados)
        elif opcion == "4":
            empleados = editar_empleado(empleados)
        elif opcion == "5":
            empleados = eliminar_registro(empleados)
        elif opcion == "6":
            empleados = eliminar_archivo(empleados)
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
