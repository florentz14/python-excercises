# -------------------------------------------------
# File Name: 33_power_set.py
# Purpose: Generate all subsets (power set)
# Description: Power set P(A) contains all subsets of A.
#              Size is 2^n. Recursive and iterative generation.
# -------------------------------------------------

print("Power Set (All Subsets)")
print("-" * 40)


def power_set_iterative(elements):
    """Iterative: build subsets by including or excluding each element."""
    result = [set()]
    for x in elements:
        result += [s | {x} for s in result]
    return result


def power_set_recursive(elements):
    """Recursive: include or exclude first element, recurse on rest."""
    if not elements:
        return [set()]
    first, rest = elements[0], elements[1:]
    without = power_set_recursive(rest)
    with_first = [s | {first} for s in without]
    return without + with_first


# Example
A = {1, 2, 3}
elements = list(A)

ps_iter = power_set_iterative(elements)
ps_rec = power_set_recursive(elements)

print("Set A =", A)
print("Power set (iterative):", ps_iter)
print("Power set (recursive):", ps_rec)
print("Count:", len(ps_iter), "= 2^" + str(len(A)), "=", 2 ** len(A))
