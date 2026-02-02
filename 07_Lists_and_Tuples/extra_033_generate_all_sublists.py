# 33. Generate All Sublists (powerset of list as contiguous sublists - or all subsets)

def all_sublists(lst: list) -> list:
    """All contiguous sublists."""
    return [lst[i:j] for i in range(len(lst)) for j in range(i + 1, len(lst) + 1)]


# Or all subsets (non-contiguous):
def all_subsets(lst: list) -> list:
    import itertools
    return [list(c) for r in range(len(lst) + 1) for c in itertools.combinations(lst, r)]


print(all_sublists([1, 2, 3]))
