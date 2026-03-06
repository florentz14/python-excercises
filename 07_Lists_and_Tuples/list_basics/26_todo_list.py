# ---------------------------------------------------------------------------
# Lista Simple - 26: Todo List con Ciclo While
# ---------------------------------------------------------------------------
# Descripcion: Una aplicacion de lista de tareas que usa un ciclo while para
#              mostrar un menu y permitir agregar, eliminar, ver y marcar
#              tareas como completadas. Utiliza operaciones basicas de listas.
# Metodos:     append(), remove(), in, len(), indices
# ---------------------------------------------------------------------------

# Lista para almacenar las tareas
tareas = []
tareas_completadas = []

# Ciclo principal con while - se ejecuta hasta que el usuario elige salir
while True:
    print("\n" + "=" * 40)
    print("       MENU - LISTA DE TAREAS")
    print("=" * 40)
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Ver tareas pendientes")
    print("4. Marcar tarea como completada")
    print("5. Ver tareas completadas")
    print("6. Salir")
    print("=" * 40)

    opcion = input("\nElige una opcion (1-6): ").strip()

    # Opcion 1: Agregar tarea
    if opcion == "1":
        nueva_tarea = input("Escribe la tarea a agregar: ").strip()
        if nueva_tarea:
            tareas.append(nueva_tarea)
            print(f"  --> Tarea agregada: '{nueva_tarea}'")
        else:
            print("  --> No se puede agregar una tarea vacia.")

    # Opcion 2: Eliminar tarea
    elif opcion == "2":
        if not tareas:
            print("  --> No hay tareas pendientes para eliminar.")
        else:
            print("\nTareas pendientes:")
            for i, tarea in enumerate(tareas, 1):
                print(f"  {i}. {tarea}")
            try:
                indice = int(input("\nNumero de tarea a eliminar: "))
                if 1 <= indice <= len(tareas):
                    eliminada = tareas.pop(indice - 1)
                    print(f"  --> Tarea eliminada: '{eliminada}'")
                else:
                    print("  --> Numero invalido.")
            except ValueError:
                print("  --> Debes ingresar un numero.")

    # Opcion 3: Ver tareas pendientes
    elif opcion == "3":
        if not tareas:
            print("  --> No hay tareas pendientes.")
        else:
            print("\nTareas pendientes:")
            for i, tarea in enumerate(tareas, 1):
                print(f"  {i}. {tarea}")

    # Opcion 4: Marcar como completada
    elif opcion == "4":
        if not tareas:
            print("  --> No hay tareas pendientes.")
        else:
            print("\nTareas pendientes:")
            for i, tarea in enumerate(tareas, 1):
                print(f"  {i}. {tarea}")
            try:
                indice = int(input("\nNumero de tarea completada: "))
                if 1 <= indice <= len(tareas):
                    completada = tareas.pop(indice - 1)
                    tareas_completadas.append(completada)
                    print(f"  --> Tarea marcada como completada: '{completada}'")
                else:
                    print("  --> Numero invalido.")
            except ValueError:
                print("  --> Debes ingresar un numero.")

    # Opcion 5: Ver tareas completadas
    elif opcion == "5":
        if not tareas_completadas:
            print("  --> No hay tareas completadas.")
        else:
            print("\nTareas completadas:")
            for i, tarea in enumerate(tareas_completadas, 1):
                print(f"  {i}. {tarea}")

    # Opcion 6: Salir
    elif opcion == "6":
        print("\n  --> Saliendo del programa. Hasta luego!")
        break

    # Opcion invalida
    else:
        print("  --> Opcion no valida. Elige un numero del 1 al 6.")

# ---------------------------------------------------------------------------
# Nota: El ciclo while True se usa para mantener el programa corriendo hasta
#       que el usuario elija "Salir". Dentro del ciclo se usan las listas
#       con append(), pop(), enumerate() e indices para manipular las tareas.
# ---------------------------------------------------------------------------
