# 12_06_type_hints_generadores.py - Type hints y funciones generadoras

print("=== Type Hints y Generadores ===\n")

# Función con tipo hints (type hints)
print("=== Type Hints ===")
def multiplicar(a: int, b: int) -> int:
    return a * b

resultado = multiplicar(4, 7)
print(f"multiplicar(4, 7) = {resultado}\n")

# Función generadora (yield)
print("=== Función Generadora ===")
def numeros_pares(limite):
    for i in range(0, limite, 2):
        yield i

print("Primeros 5 números pares:")
for num in numeros_pares(10):
    print(f"  {num}")
print()
