# 203. Join Adjacent Members of List (pairs)

def join_adjacent(lst: list[str]) -> list[str]:
    return [lst[i] + lst[i + 1] for i in range(0, len(lst) - 1, 2)]


print(join_adjacent(['1', '2', '3', '4', '5', '6', '7', '8']))  # ['12', '34', '56', '78']
print(join_adjacent(['1', '2', '3']))  # ['12']
