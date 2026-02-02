# 217. Split Values into Two Groups by Filtering Function

def split_by_filter(lst: list, predicate) -> tuple[list, list]:
    yes = [x for x in lst if predicate(x)]
    no = [x for x in lst if not predicate(x)]
    return yes, no


sample = ['red', 'green', 'white', 'black']
white, other = split_by_filter(sample, lambda x: x == 'white')
print([white, other])  # [['white'], ['red', 'green', 'black']]
