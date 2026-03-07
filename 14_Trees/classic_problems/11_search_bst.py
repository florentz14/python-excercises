"""
#11 Search in a Binary Search Tree (LeetCode 700)
==================================================
Concept: BST property - go left if target < root, right if target > root
Time: O(h), Space: O(h)
"""

from common import TreeNode


def search_bst(root: TreeNode | None, val: int) -> TreeNode | None:
    """Return subtree rooted at node with val, or None."""
    if root is None or root.val == val:
        return root
    return search_bst(root.left, val) if val < root.val else search_bst(root.right, val)


if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    node = search_bst(root, 2)
    print(f"search_bst(2): {node.val if node else None}")  # 2
    print(f"search_bst(5): {search_bst(root, 5)}")  # None
