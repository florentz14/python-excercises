# 83. Round Every Number, Print Total Sum * Length

def round_sum_times_length(lst: list[float]) -> int | float:
    rounded = [round(x) for x in lst]
    return sum(rounded) * len(rounded)


sample = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
print(round_sum_times_length(sample))  # 243
