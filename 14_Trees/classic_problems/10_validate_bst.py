"""
#10 Validate Binary Search Tree (LeetCode 98)
=============================================
Concept: BST property (Left < Root < Right)
Time: O(n), Space: O(h)

Essential for interviews.
"""

from common import TreeNode


def is_valid_bst(root: TreeNode | None, lo: int | float = float("-inf"), hi: int | float = float("inf")) -> bool:
    """Validate BST: every node must be in range (lo, hi)."""
    if root is None:
        return True
    if not (lo < root.val < hi):
        return False
    return is_valid_bst(root.left, lo, root.val) and is_valid_bst(root.right, root.val, hi)


if __name__ == "__main__":
    # Valid BST
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(f"is_valid_bst([2,1,3]): {is_valid_bst(root)}")  # True

    # Invalid: 1 > 2 on right
    bad = TreeNode(2, TreeNode(3), TreeNode(1))
    print(f"is_valid_bst([2,3,1]): {is_valid_bst(bad)}")  # False
