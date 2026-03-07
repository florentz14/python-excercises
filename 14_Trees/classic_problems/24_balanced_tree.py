"""
#24 Balanced Binary Tree
=========================
LeetCode 110. Check if height difference of left/right subtrees <= 1 for all nodes.
Time: O(n), Space: O(h).
"""

from common import TreeNode


def is_balanced(root: TreeNode | None) -> bool:
    """Returns True if tree is height-balanced."""

    def check(node: TreeNode | None) -> int:
        """Returns height, or -1 if unbalanced."""
        if not node:
            return 0
        left_h = check(node.left)
        if left_h == -1:
            return -1
        right_h = check(node.right)
        if right_h == -1:
            return -1
        if abs(left_h - right_h) > 1:
            return -1
        return 1 + max(left_h, right_h)

    return check(root) != -1


if __name__ == "__main__":
    # Balanced
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    print("Balanced (1,2,3):", is_balanced(root1))

    # Unbalanced: 1-2-3
    root2 = TreeNode(1, TreeNode(2, TreeNode(3)), None)
    print("Unbalanced (1-2-3):", is_balanced(root2))
