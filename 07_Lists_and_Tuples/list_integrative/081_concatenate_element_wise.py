# -------------------------------------------------
# File Name: 081_concatenate_element_wise.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Concatenate Three Lists Element-Wise (str)
# -------------------------------------------------

def concat_element_wise(*lists: list[str]) -> list[str]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [''.join(str(x) for x in t) for t in zip(*lists)]


a = ['0', '1', '2', '3', '4']
b = ['red', 'green', 'black', 'blue', 'white']
c = ['100', '200', '300', '400', '500']
print(concat_element_wise(a, b, c))  # ['0red100', '1green200', ...]
