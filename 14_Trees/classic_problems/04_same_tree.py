# -------------------------------------------------
# File Name: 04_same_tree.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: LeetCode 100 - Check if two trees have same structure and values.
# -------------------------------------------------

from common import TreeNode


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    """Returns True if both trees have the same structure and values."""
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == "__main__":
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    t2 = TreeNode(1, TreeNode(2), TreeNode(3))
    t3 = TreeNode(1, TreeNode(2), None)
    print(f"Same tree (1,2): {is_same_tree(t1, t2)}")  # True
    print(f"Same tree (1,3): {is_same_tree(t1, t3)}")  # False
