# -------------------------------------------------
# File Name: 013_sum_input.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Demonstrates sum input.
# -------------------------------------------------

nums = []
# Repetimos 3 veces: pedir un número y añadirlo a la lista
for i in range(3):
    # input() devuelve texto; int() lo convierte a número entero
    n = int(input('Enter a number: '))
    # append() añade el número al final de la lista
    nums.append(n)
# sum() suma todos los elementos de la lista; mostramos el resultado
print(sum(nums))
