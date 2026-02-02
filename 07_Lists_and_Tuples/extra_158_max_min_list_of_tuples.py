# 158. Max and Min Values in List of Tuples (by numeric element)

def max_min_tuples(tuples: list[tuple], index: int = 1) -> tuple:
    values = [t[index] for t in tuples if len(t) > index]
    return (max(values), min(values)) if values else (None, None)


sample = [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
print(max_min_tuples(sample))  # (78, 60)
