# Archivo: 42_02_seleccion_actividades.py
# Descripción: Problema de selección de actividades (greedy)

print("=== 2. Problema de Selección de Actividades ===\n")


def seleccion_actividades(inicios, fines):
    """
    Encuentra el máximo número de actividades que no se solapan.
    Estrategia: Seleccionar actividades que terminan primero.
    Complejidad: O(n log n)
    """
    n = len(inicios)
    actividades = list(zip(inicios, fines, range(n)))
    actividades.sort(key=lambda x: x[1])

    seleccionadas = []
    ultimo_fin = 0

    for inicio, fin, indice in actividades:
        if inicio >= ultimo_fin:
            seleccionadas.append(indice)
            ultimo_fin = fin

    return seleccionadas


if __name__ == "__main__":
    inicios = [1, 3, 0, 5, 8, 5]
    fines = [2, 4, 6, 7, 9, 9]

    print("Actividades:")
    for i, (inicio, fin) in enumerate(zip(inicios, fines)):
        print(f"  Actividad {i}: [{inicio}, {fin}]")

    seleccionadas = seleccion_actividades(inicios, fines)
    print(f"\nNúmero máximo de actividades: {len(seleccionadas)}")
    print(f"Actividades seleccionadas: {seleccionadas}")
    for indice in seleccionadas:
        print(f"  Actividad {indice}: [{inicios[indice]}, {fines[indice]}]")
