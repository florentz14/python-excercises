# ---------------------------------------------------------------------------
# 119. Check If Substring Appears in Any String in List
# ---------------------------------------------------------------------------
# Descripción: Check If Substring Appears in Any String in List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def substring_in_list(lst: list[str], sub: str) -> bool:
    return any(sub in s for s in lst)


sample = ['red', 'black', 'white', 'green', 'orange']
print(substring_in_list(sample, 'ack'))  # True
print(substring_in_list(sample, 'abc'))  # False
