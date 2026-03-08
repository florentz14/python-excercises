# -------------------------------------------------
# File Name: 05_symmetric_tree.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: LeetCode 101 - Check if tree is symmetric (left mirrors right).
# -------------------------------------------------

from common import TreeNode


def is_symmetric(root: TreeNode | None) -> bool:
    """Returns True if tree is mirror of itself around center."""
    if root is None:
        return True
    return _mirror(root.left, root.right)


def _mirror(a: TreeNode | None, b: TreeNode | None) -> bool:
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.val != b.val:
        return False
    return _mirror(a.left, b.right) and _mirror(a.right, b.left)


if __name__ == "__main__":
    # Symmetric:  1
    #           /   \
    #          2     2
    #         / \   / \
    #        3  4  4  3
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    print(f"Symmetric: {is_symmetric(root)}")  # True
