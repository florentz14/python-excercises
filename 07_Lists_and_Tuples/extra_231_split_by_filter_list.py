# ---------------------------------------------------------------------------
# 231. Split Values by Filter List (two groups: where filter True vs False)
# ---------------------------------------------------------------------------
# Descripción: Split Values by Filter List (two groups: where filter True vs False)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def split_by_filter_list(lst: list, filter_list: list[bool]) -> list[list]:
    yes = [lst[i] for i in range(min(len(lst), len(filter_list))) if filter_list[i]]
    no = [lst[i] for i in range(min(len(lst), len(filter_list))) if not filter_list[i]]
    return [yes, no]


colors = ['red', 'green', 'blue', 'pink']
filter_l = [True, True, False, True]
print(split_by_filter_list(colors, filter_l))  # [['red', 'green', 'pink'], ['blue']]
