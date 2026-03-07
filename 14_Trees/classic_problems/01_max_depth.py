"""
LeetCode 104 - Maximum Depth of Binary Tree
============================================
Concept: Recursion. Base: empty = 0. Recursive: 1 + max(left, right).
Time: O(n), Space: O(h)
"""

from common import TreeNode


def max_depth(root: TreeNode | None) -> int:
    """Returns the maximum depth (height) of a binary tree."""
    if root is None:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1


if __name__ == "__main__":
    # Tree:    3
    #        /   \
    #       9    20
    #           /  \
    #          15   7
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(f"Max depth: {max_depth(root)}")  # 3
