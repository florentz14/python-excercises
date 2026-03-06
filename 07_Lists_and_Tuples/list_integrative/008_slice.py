# ---------------------------------------------------------------------------
# Part 1: Lists - Exercise 6
# ---------------------------------------------------------------------------
# Descripción: Obtener un trozo (slice) de la lista: desde el índice 2
#              hasta el 5 (sin incluir el 5). Sintaxis: lista[inicio:fin].
# ---------------------------------------------------------------------------

nums = [10, 20, 30, 40, 50, 60]
# [2:5] toma los elementos en posiciones 2, 3 y 4 (el 5 queda excluido)
# 2->30, 3->40, 4->50 -> resultado [30, 40, 50]
print(nums[2:5])
