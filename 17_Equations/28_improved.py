# -------------------------------------------------
# File Name: 28_improved.py
# Author: Florentino Báez
# Date: 17_Equations
# Description: Solve system with optimized version.
# -------------------------------------------------

from datos_ejemplo_33 import A, b
from resolver_mejorado import resolver_sistema_mejorado


if __name__ == "__main__":
    print("=== Versión 2: Optimizada y Mejorada ===\n")
    print("Resolviendo sistema con versión mejorada:")
    print("Sistema: x + y + z = 2,  2x + z = 1,  x + 2y = 5\n")
    x, info = resolver_sistema_mejorado(A.copy(), b.copy())
