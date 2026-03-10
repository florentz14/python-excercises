# -------------------------------------------------
# File Name: 25_copy_list_with_random_pointer.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Deep copy of linked list with random pointers.
# -------------------------------------------------

SEPARATOR = "=" * 62


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


class RandomNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: "RandomNode | None" = None
        self.random: "RandomNode | None" = None


def copy_random_list(head: RandomNode | None) -> RandomNode | None:
    if head is None:
        return None

    old_to_new: dict[RandomNode, RandomNode] = {}
    current = head
    while current:
        old_to_new[current] = RandomNode(current.value)
        current = current.next

    current = head
    while current:
        copy = old_to_new[current]
        copy.next = old_to_new.get(current.next)
        copy.random = old_to_new.get(current.random)
        current = current.next

    return old_to_new[head]


def snapshot(head: RandomNode | None) -> list[tuple[int, int | None]]:
    nodes = []
    index_of = {}
    cur = head
    idx = 0
    while cur:
        nodes.append(cur)
        index_of[cur] = idx
        idx += 1
        cur = cur.next

    out = []
    for node in nodes:
        random_idx = index_of.get(node.random) if node.random else None
        out.append((node.value, random_idx))
    return out


def demo() -> None:
    title("COPY LIST WITH RANDOM POINTER")
    nodes = [RandomNode(7), RandomNode(13), RandomNode(11), RandomNode(10)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    nodes[1].random = nodes[0]
    nodes[2].random = nodes[3]
    nodes[3].random = nodes[1]

    original = nodes[0]
    copied = copy_random_list(original)

    print(f"  Original snapshot: {snapshot(original)}")
    print(f"  Copied snapshot:   {snapshot(copied)}")


if __name__ == "__main__":
    demo()
