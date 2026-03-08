# -------------------------------------------------
# File Name: 02_improved.py
# Author: Florentino Báez
# Date: 17_Equations
# Description: Optimized and improved linear system solver.
# -------------------------------------------------

from datos_sistema import A, b
from resolver_mejorado import resolver_sistema_mejorado


if __name__ == "__main__":
    print("=== Versión 2: Optimizada y Mejorada ===\n")
    print("Resolviendo con versión mejorada:")
    x, info = resolver_sistema_mejorado(A.copy(), b.copy())
