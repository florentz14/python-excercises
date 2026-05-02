import numpy as np

print("=" * 50)
print("13. ARRAY FILTER")
print("=" * 50)

arr = np.array([10, 15, 20, 25, 30, 35, 40])

# Boolean mask
mask_even  = arr % 2 == 0
mask_gt20  = arr > 20

even_vals  = arr[mask_even]
gt20_vals  = arr[mask_gt20]
combined   = arr[(arr > 15) & (arr < 35)]   # AND
either     = arr[(arr < 15) | (arr > 35)]   # OR

# np.where como filtro condicional (reemplaza valores)
replaced = np.where(arr > 20, arr, 0)       # mantiene >20, el resto = 0

print(f"Array:               {arr}")
print(f"Mask even:           {mask_even}")
print(f"Even values:         {even_vals}")
print(f"Values > 20:         {gt20_vals}")
print(f"15 < x < 35:         {combined}")
print(f"x<15 OR x>35:        {either}")
print(f"np.where(>20, x, 0): {replaced}")
