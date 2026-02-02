# 52. Difference Between Two Lists (Color1-Color2 and Color2-Color1)

def list_differences(a: list, b: list) -> tuple[list, list]:
    set_a, set_b = set(a), set(b)
    return (list(set_a - set_b), list(set_b - set_a))


color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]
diff1, diff2 = list_differences(color1, color2)
print("Color1-Color2:", diff1)
print("Color2-Color1:", diff2)
