# ---------------------------------------------------------------------------
# Lista Simple - 17: Copiar Listas
# ---------------------------------------------------------------------------
# Descripcion: En Python, asignar una lista a otra variable NO crea una
#              copia, sino una REFERENCIA al mismo objeto. Para crear una
#              copia independiente se usan copy(), list() o slicing.
# Metodos:     lista.copy()  /  list(lista)  /  lista[:]
# ---------------------------------------------------------------------------

# --- El problema de la asignacion directa ---
original = ["apple", "banana", "cherry"]
referencia = original  # NO es una copia, es la misma lista

referencia.append("pear")
print("Original:", original)    # ['apple', 'banana', 'cherry', 'pear']
print("Referencia:", referencia) # ['apple', 'banana', 'cherry', 'pear']
print("Son el mismo objeto:", original is referencia)  # True
# Ambas variables apuntan al MISMO objeto en memoria

# ---------------------------------------------------------------------------
# Formas correctas de copiar una lista (copia superficial / shallow copy)
# ---------------------------------------------------------------------------

original = ["apple", "banana", "cherry"]

# Metodo 1: copy()
copia1 = original.copy()
copia1.append("strawberry")
print("\n--- copy() ---")
print("Original:", original)  # Sin cambios
print("Copia 1:", copia1)     # Con el nuevo elemento

# Metodo 2: list()
copia2 = list(original)
copia2.append("mango")
print("\n--- list() ---")
print("Original:", original)  # Sin cambios
print("Copia 2:", copia2)     # Con el nuevo elemento

# Metodo 3: slicing [:]
copia3 = original[:]
copia3.append("grape")
print("\n--- slicing [:] ---")
print("Original:", original)  # Sin cambios
print("Copia 3:", copia3)     # Con el nuevo elemento

# Verificar que son objetos diferentes
print("\n--- Verificacion ---")
print("original is copia1:", original is copia1)  # False
print("original is copia2:", original is copia2)  # False
print("original is copia3:", original is copia3)  # False

# ---------------------------------------------------------------------------
# Cuidado con listas anidadas (shallow copy vs deep copy)
# ---------------------------------------------------------------------------
import copy

anidada = [[1, 2], [3, 4], [5, 6]]

shallow = anidada.copy()       # Copia superficial
deep = copy.deepcopy(anidada)  # Copia profunda

anidada[0][0] = 99

print("\n--- Shallow vs Deep Copy ---")
print("Original:", anidada)  # [[99, 2], [3, 4], [5, 6]]
print("Shallow:", shallow)   # [[99, 2], [3, 4], [5, 6]] <- afectada!
print("Deep:", deep)         # [[1, 2], [3, 4], [5, 6]]  <- independiente
