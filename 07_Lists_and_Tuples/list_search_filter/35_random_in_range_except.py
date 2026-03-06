# ---------------------------------------------------------------------------
# 145. Generate Number in Range Except Specific Numbers
# ---------------------------------------------------------------------------
# Descripción: Generate Number in Range Except Specific Numbers
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

import random

def random_except(low: int, high: int, exclude: list[int]) -> int:
    choices = [x for x in range(low, high + 1) if x not in exclude]
    # Se devuelve un valor u otro según la condición.
    return random.choice(choices) if choices else None


print(random_except(1, 10, [2, 9, 10]))
print(random_except(-5, 5, [-5, 0, 4, 3, 2]))
