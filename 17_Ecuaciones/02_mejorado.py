# Archivo: 25_02_mejorado.py
# Descripción: Versión optimizada y mejorada del resolver

from datos_sistema import A, b
from resolver_mejorado import resolver_sistema_mejorado


if __name__ == "__main__":
    print("=== Versión 2: Optimizada y Mejorada ===\n")
    print("Resolviendo con versión mejorada:")
    x, info = resolver_sistema_mejorado(A.copy(), b.copy())
