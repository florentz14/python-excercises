# 140. Remove Specific Item from Given List of Lists (e.g. remove 'Red' from first sublist)

def remove_from_sublists(lists: list[list], item, from_index: int | None = None) -> list[list]:
    if from_index is not None:
        result = [sublist.copy() for sublist in lists]
        if 0 <= from_index < len(result):
            result[from_index] = [x for x in result[from_index] if x != item]
        return result
    return [[x for x in sublist if x != item] for sublist in lists]


sample = [['Red', 'Maroon', 'Yellow'], ['#FF0000', '#800000'], ['rgb(255,0,0)']]
print(remove_from_sublists(sample, 'Red', 0))
