# -------------------------------------------------
# File Name: 16_slice_avanzado.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Advanced Slicing.
# -------------------------------------------------

print("=== Advanced slicing ===")
lista = list(range(10))                    # [0, 1, 2, ..., 9]
print(f"List: {lista}")

print(f"First 3:         {lista[:3]}")     # [0, 1, 2]
print(f"Last 3:          {lista[-3:]}")    # [7, 8, 9]
print(f"Index 2 to 7:    {lista[2:7]}")    # [2, 3, 4, 5, 6]
print(f"Every 2nd:       {lista[::2]}")    # [0, 2, 4, 6, 8]
print(f"Reversed:        {lista[::-1]}")   # [9, 8, 7, ..., 0]
