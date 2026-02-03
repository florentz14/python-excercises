# Archivo: 42_06_interval_scheduling.py
# Descripción: Programación de intervalos con pesos (versión simplificada)

print("=== 6. Programación de Intervalos con Pesos ===\n")


def interval_scheduling_pesos(intervals):
    """
    Interval Scheduling con pesos (Weighted Interval Scheduling).
    Versión simplificada; la versión completa usa programación dinámica.
    """
    intervals.sort(key=lambda x: x[1])
    n = len(intervals)
    pesos_acumulados = [0] * n

    for i, (inicio, fin, peso) in enumerate(intervals):
        mejor_peso = peso
        for j in range(i - 1, -1, -1):
            if intervals[j][1] <= inicio:
                if pesos_acumulados[j] + peso > mejor_peso:
                    mejor_peso = pesos_acumulados[j] + peso
                break
        pesos_acumulados[i] = mejor_peso

    seleccionados = []
    i = n - 1
    while i >= 0:
        if i == 0 or pesos_acumulados[i] > pesos_acumulados[i - 1]:
            seleccionados.append(i)
            fin_actual = intervals[i][0]
            i -= 1
            while i >= 0 and intervals[i][1] > fin_actual:
                i -= 1
        else:
            i -= 1

    seleccionados.reverse()
    peso_total = pesos_acumulados[-1] if pesos_acumulados else 0
    return seleccionados, peso_total


if __name__ == "__main__":
    intervalos_pesos = [
        (1, 4, 3),
        (3, 5, 4),
        (0, 6, 2),
        (5, 7, 1),
        (8, 9, 5),
        (5, 9, 2)
    ]

    print("Intervalos (inicio, fin, peso):")
    for i, (ini, fin, peso) in enumerate(intervalos_pesos):
        print(f"  Intervalo {i}: [{ini}, {fin}] peso={peso}")

    seleccionados, peso_total = interval_scheduling_pesos(intervalos_pesos)
    print(f"\nIntervalos seleccionados: {seleccionados}")
    print(f"Peso total: {peso_total}")
    for indice in seleccionados:
        ini, fin, peso = intervalos_pesos[indice]
        print(f"  Intervalo {indice}: [{ini}, {fin}] peso={peso}")
