# -------------------------------------------------
# File Name: 23_diameter.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: LeetCode 543 - Diameter of binary tree (longest path).
# -------------------------------------------------

from common import TreeNode


def diameter_of_binary_tree(root: TreeNode | None) -> int:
    """Returns diameter (longest path between two nodes)."""
    diameter = 0

    def height(node: TreeNode | None) -> int:
        nonlocal diameter
        if not node:
            return 0
        left_h = height(node.left)
        right_h = height(node.right)
        diameter = max(diameter, left_h + right_h)
        return 1 + max(left_h, right_h)

    height(root)
    return diameter


if __name__ == "__main__":
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)
    print("Diameter:", diameter_of_binary_tree(root))  # 3 (path 4-2-1-3 or 4-2-5)
