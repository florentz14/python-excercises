# -------------------------------------------------
# File Name: 02_multiply_items_in_list.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Multiplica todos los elementos de una lista entre sí.
# -------------------------------------------------

def multiply_list_items(lst: list[int | float]) -> int | float:
    # Acumulador: debe empezar en 1 (si fuera 0, el producto siempre sería 0)
    result = 1
    # Recorremos cada elemento de la lista
    for x in lst:
        # Multiplicamos el acumulador por el elemento actual
        result *= x
    # Devolvemos el producto total
    return result


# --- Ejemplo de uso ---
nums = [1, 2, 3, 4]
print(multiply_list_items(nums))  # 24
