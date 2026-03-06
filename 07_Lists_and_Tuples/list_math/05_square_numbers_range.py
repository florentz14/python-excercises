# ---------------------------------------------------------------------------
# 16. First and last 5 square numbers between 1 and 30
# ---------------------------------------------------------------------------
# Descripción: First and last 5 square numbers between 1 and 30
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

squares = [x * x for x in range(1, 31) if 1 <= x * x <= 30]
# Actually: squares between 1 and 30 (both included) -> 1,4,9,16,25
squares = [x * x for x in range(1, 6)]  # 1-5 squared
all_sq = [x * x for x in range(1, 31)]
first5 = all_sq[:5]
last5 = all_sq[-5:]
print("First 5:", first5)
print("Last 5:", last5)
