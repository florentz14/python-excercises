# ---------------------------------------------------------------------------
# 201. Check If String Contains Any Element from List
# ---------------------------------------------------------------------------
# Descripción: Check If String Contains Any Element from List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def string_contains_any(s: str, lst: list[str]) -> bool:
    return any(elem in s for elem in lst)


url = "https://www.w3resource.com/python-exercises/list/"
print(string_contains_any(url, ['.com', '.edu', '.tv']))  # True
print(string_contains_any("https://www.w3resource.net", ['.com', '.edu', '.tv']))  # False
