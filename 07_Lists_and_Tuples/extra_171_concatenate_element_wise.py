# 171. Concatenate Three Lists Element-Wise (str)

def concat_element_wise(*lists: list[str]) -> list[str]:
    return [''.join(str(x) for x in t) for t in zip(*lists)]


a = ['0', '1', '2', '3', '4']
b = ['red', 'green', 'black', 'blue', 'white']
c = ['100', '200', '300', '400', '500']
print(concat_element_wise(a, b, c))  # ['0red100', '1green200', ...]
