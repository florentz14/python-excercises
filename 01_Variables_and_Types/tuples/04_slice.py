# -------------------------------------------------
# File Name: 04_slice.py
# Author: Florentino Báez
# Date: Variables - Tuples
# Description: Slice a Tuple.
#              Slicing extracts sub-tuples with the syntax
#              tuple[start:stop:step]. Omitting start defaults
#              to 0, omitting stop defaults to len(). A step
#              of -1 reverses the tuple.
# -------------------------------------------------

print("Example 4: Slice a tuple")
print("-" * 40)

letters = ("a", "b", "c", "d", "e", "f")
print("Original tuple:", letters)

print("First 3 elements:", letters[0:3])       # ('a', 'b', 'c')
print("Elements from index 2 to 4:", letters[2:5])  # ('c', 'd', 'e')
print("Every second element:", letters[::2])   # ('a', 'c', 'e') — step of 2

nums = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print("\nOriginal tuple:", nums)

# Básico [start:stop]
print("\n--- Básico [start:stop] ---")
print("nums[:] (copia completa):", nums[:])
print("nums[0:3] (primeros 3):", nums[0:3])
print("nums[:3] (primeros 3):", nums[:3])
print("nums[3:] (desde índice 3):", nums[3:])
print("nums[2:5] (índices 2 a 4):", nums[2:5])
print("nums[5:] (desde índice 5):", nums[5:])
print("nums[:5] (hasta índice 5):", nums[:5])
print("nums[2:] (desde índice 2):", nums[2:])

# Índices negativos
print("\n--- Índices negativos ---")
print("nums[-3:] (últimos 3):", nums[-3:])
print("nums[:-2] (todos menos últimos 2):", nums[:-2])
print("nums[-5:-2] (del 5º al 2º desde el final):", nums[-5:-2])

# Con step [start:stop:step]
print("\n--- Con step ---")
print("nums[::2] (cada 2º elemento):", nums[::2])
print("nums[::3] (cada 3º elemento):", nums[::3])
print("nums[1::2] (cada 2º desde índice 1):", nums[1::2])
print("nums[2:8:2] (índices 2-7, cada 2º):", nums[2:8:2])

# Reverso
print("\n--- Reverso ---")
print("nums[::-1] (invertir):", nums[::-1]) # (100, 90, 80, 70, 60, 50, 40, 30, 20, 10)
print("nums[::-2] (invertir cada 2º):", nums[::-2]) # (100, 80, 60, 40, 20)
print("nums[8:2:-1] (del índice 8 al 3 en reverso):", nums[8:2:-1]) # (90, 80, 70, 60, 50, 40, 30, 20, 10)

# slicing en strings
print("\n--- Slicing en strings word ---")
word = "Hello, World!"
print("Original word:", word) # 'Hello, World!'
print("Copia de word:", word[:]) # 'Hello, World!'
print("word[1:4]:", word[1:4]) # 'ell'
print("word[1:4:2]:", word[1:4:2]) # 'el' -> 'el'
print("word[::-1]:", word[::-1]) # '!dlroW ,olleH' -> '!dlroW ,olleH'

# slicing en strings
print("\n--- Slicing en strings word2 ---")
word2 = "Python"
print("Original word2:", word2) # 'Python'
print("Copia de word2:", word2[:]) # 'Python'
print("word2[1:4]:", word2[1:4]) # 'yth'
print("word2[1:4:2]:", word2[1:4:2]) # 'yh'
print("word2[::-1]:", word2[::-1]) # 'nohtyP' -> 'nohtyP'



