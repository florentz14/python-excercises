"""
14_Trees - Red-Black Tree
=========================================
Self-balancing BST with color rules. O(log n) operations.
Used in: std::map (C++), TreeMap (Java), database internals.

Rules: root black, no two consecutive reds, same black count on all paths.
"""


class RBNode:
    """Red-Black tree node."""
    RED = "R"
    BLACK = "B"

    def __init__(self, value, color=RED):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    """Red-Black tree: self-balancing BST with O(log n) operations."""

    def __init__(self):
        self.nil = RBNode(0, RBNode.BLACK)
        self.root = self.nil

    def insert(self, value):
        """Insert value maintaining Red-Black invariants."""
        node = RBNode(value)
        node.left = node.right = self.nil

        parent = None
        curr = self.root
        while curr != self.nil:
            parent = curr
            if value < curr.value:
                curr = curr.left
            else:
                curr = curr.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif value < parent.value:
            parent.left = node
        else:
            parent.right = node

        node.color = RBNode.RED
        self._fix_insert(node)

    def _fix_insert(self, node):
        """Fix Red-Black invariants after insert."""
        while node.parent and node.parent.color == RBNode.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == RBNode.RED:
                    node.parent.color = RBNode.BLACK
                    uncle.color = RBNode.BLACK
                    node.parent.parent.color = RBNode.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = RBNode.BLACK
                    node.parent.parent.color = RBNode.RED
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == RBNode.RED:
                    node.parent.color = RBNode.BLACK
                    uncle.color = RBNode.BLACK
                    node.parent.parent.color = RBNode.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = RBNode.BLACK
                    node.parent.parent.color = RBNode.RED
                    self._rotate_left(node.parent.parent)
        self.root.color = RBNode.BLACK

    def _rotate_left(self, x):
        """Left rotation."""
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        """Right rotation."""
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder(self):
        """Inorder traversal (sorted order)."""
        result = []

        def _inorder(node):
            if node != self.nil:
                _inorder(node.left)
                result.append((node.value, node.color))
                _inorder(node.right)

        _inorder(self.root)
        return result


if __name__ == "__main__":
    print("=== Red-Black Tree ===\n")
    rbt = RedBlackTree()
    for v in [7, 3, 18, 10, 22, 8, 11, 26]:
        rbt.insert(v)
    print("Inorder (value, color):", rbt.inorder())
    print("O(log n) insert, search, delete. Used in TreeMap, std::map.")
