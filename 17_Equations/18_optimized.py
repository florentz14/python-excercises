# -------------------------------------------------
# File Name: 18_optimized.py
# Author: Florentino Báez
# Date: 17_Equations
# Description: Optimized integration with details and error estimate.
# -------------------------------------------------

from integracion_util import f_original, integrar_funcion


if __name__ == "__main__":
    print("=== Versión 2: Optimizada y Mejorada ===\n")
    print("Integración optimizada:")
    resultado, error = integrar_funcion(f_original, -4, -3)
