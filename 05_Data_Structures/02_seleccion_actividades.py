# -------------------------------------------------
# File Name: 02_seleccion_actividades.py
# Author: Florentino Báez
# Date: Data Structures - Greedy Algorithms
# Description: Activity Selection Problem (Greedy).
#              Finds the maximum number of non-overlapping
#              activities. The greedy strategy is to always
#              select the activity that finishes earliest.
#              Complexity: O(n log n) due to sorting.
# -------------------------------------------------

print("=== 2. Problema de Selección de Actividades ===\n")


def seleccion_actividades(inicios, fines):
    """
    Finds the maximum number of non-overlapping activities.
    Strategy: Select activities that finish earliest.
    Complexity: O(n log n)
    """
    n = len(inicios)
    # Combine start, end and index into a single list
    actividades = list(zip(inicios, fines, range(n)))
    # Sort by finish time (greedy key: earliest finish first)
    actividades.sort(key=lambda x: x[1])

    seleccionadas = []  # Indices of selected activities
    ultimo_fin = 0      # End time of the last selected activity

    for inicio, fin, indice in actividades:
        if inicio >= ultimo_fin:
            # Activity does not overlap with the previously selected one
            seleccionadas.append(indice)
            ultimo_fin = fin  # Update the most recent finish time

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
