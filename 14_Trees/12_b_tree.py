# -------------------------------------------------
# File Name: 12_b_tree.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: B-Tree for disk/databases; nodes hold multiple keys.
# -------------------------------------------------

class BTreeNode:
    """B-Tree node with multiple keys and children."""

    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf


class BTree:
    """B-Tree of order t (min t-1, max 2t-1 keys per node)."""

    def __init__(self, t=3):
        self.root = BTreeNode(leaf=True)
        self.t = t  # minimum degree

    def search(self, key, node=None):
        """Search for key. Returns (node, index) or None."""
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return (node, i)
        if node.leaf:
            return None
        return self.search(key, node.children[i])

    def insert(self, key):
        """Insert key into B-Tree."""
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(new_root, key)
        else:
            self._insert_non_full(root, key)

    def _insert_non_full(self, node, key):
        """Insert into non-full node."""
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(0)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, i):
        """Split full child at index i."""
        t = self.t
        full = parent.children[i]
        new_node = BTreeNode(leaf=full.leaf)
        parent.children.insert(i + 1, new_node)
        parent.keys.insert(i, full.keys[t - 1])
        new_node.keys = full.keys[t:]
        full.keys = full.keys[: t - 1]
        if not full.leaf:
            new_node.children = full.children[t:]
            full.children = full.children[:t]

    def traverse(self, node=None):
        """Inorder-like traversal (keys sorted)."""
        if node is None:
            node = self.root
        result = []
        for i in range(len(node.keys)):
            if not node.leaf:
                result.extend(self.traverse(node.children[i]))
            result.append(node.keys[i])
        if not node.leaf:
            result.extend(self.traverse(node.children[len(node.keys)]))
        return result


if __name__ == "__main__":
    print("=== B-Tree (order 3) ===\n")
    bt = BTree(t=3)
    for k in [10, 20, 5, 6, 12, 30, 7, 17]:
        bt.insert(k)
    print("Traversal (sorted):", bt.traverse())
    print("Search 6:", bt.search(6))
    print("Search 99:", bt.search(99))
    print("Used in: databases, file systems. O(log n) per operation.")
