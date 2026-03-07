"""
#12 Insert into a Binary Search Tree (LeetCode 701)
====================================================
Concept: Find correct position by BST property, insert as leaf
Time: O(h), Space: O(h)
"""

from common import TreeNode


def insert_into_bst(root: TreeNode | None, val: int) -> TreeNode:
    """Insert val into BST. Return root (new if was None)."""
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root


if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    root = insert_into_bst(root, 5)
    print("After insert(5):", root.right.left.val if root.right and root.right.left else "N/A")  # 5
