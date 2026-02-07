# ---------------------------------------------------------------------------
# Lista Simple - 25: Operador 'in' (Membresia)
# ---------------------------------------------------------------------------
# Descripcion: El operador 'in' verifica si un valor existe en la lista.
#              Retorna True si lo encuentra, False si no. 'not in' hace
#              la comprobacion inversa.
# Sintaxis:    valor in lista       -> True/False
#              valor not in lista   -> True/False
# Complejidad: O(n) - recorre la lista hasta encontrar el elemento
# ---------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "pineapple", "grape", "mango", "blueberry"]

# --- Verificar si un elemento ESTA en la lista ---
print("banana" in fruits)      # True
print("pear" in fruits)        # False

# --- Verificar si un elemento NO ESTA en la lista ---
print("pear" not in fruits)    # True
print("banana" not in fruits)  # False

# ---------------------------------------------------------------------------
# Uso en condicionales
# ---------------------------------------------------------------------------
user_input = "cherry"

if user_input in fruits:
    print(f"\n'{user_input}' is available")
else:
    print(f"\n'{user_input}' is not available")

# ---------------------------------------------------------------------------
# Uso practico: validacion de entrada
# ---------------------------------------------------------------------------
opciones_validas = ["si", "no", "cancelar"]
respuesta = "si"

if respuesta.lower() in opciones_validas:
    print(f"Respuesta valida: {respuesta}")
else:
    print(f"Respuesta no valida. Opciones: {opciones_validas}")

# ---------------------------------------------------------------------------
# Uso con bucle while para menu interactivo (ejemplo conceptual)
# ---------------------------------------------------------------------------
available_fruits = ["apple", "banana", "cherry", "grape", "mango", "orange", "kiwi"]
cart = []
requested = ["banana", "peach", "mango", "lychee"]

for fruit in requested:
    if fruit in available_fruits and fruit not in cart:
        cart.append(fruit)
        print(f"  Added: {fruit}")
    elif fruit in cart:
        print(f"  Already in cart: {fruit}")
    else:
        print(f"  Not available: {fruit}")

print(f"\nFinal cart: {cart}")
# Output: ['banana', 'mango']

# ---------------------------------------------------------------------------
# Nota: Para listas muy grandes, usar 'in' con un set es mucho mas
#       rapido (O(1) vs O(n)). Convierte la lista a set si haces muchas
#       busquedas:  mi_set = set(mi_lista)
# ---------------------------------------------------------------------------
