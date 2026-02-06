# ---------------------------------------------------------------------------
# Part 2: Tuples - Exercise 3
# ---------------------------------------------------------------------------
# Descripción: Las tuplas son inmutables: no se puede asignar a un índice
#              para cambiar su valor. La línea comentada produciría error.
# ---------------------------------------------------------------------------

nums = (1, 2, 3)
# Si descomentamos la siguiente línea, Python lanza TypeError:
# "tuple object does not support item assignment"
#nums[0] = 99  # Error: las tuplas no permiten modificar elementos

print(nums)
