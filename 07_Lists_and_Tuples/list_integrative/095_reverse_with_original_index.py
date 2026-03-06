# ---------------------------------------------------------------------------
# 195. Traverse List in Reverse with Original Index
# ---------------------------------------------------------------------------
# Descripción: Traverse List in Reverse with Original Index
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def reverse_with_index(lst: list) -> None:
    for i in range(len(lst) - 1, -1, -1):
        print(i, lst[i])


sample = ['red', 'green', 'white', 'black']
reverse_with_index(sample)
