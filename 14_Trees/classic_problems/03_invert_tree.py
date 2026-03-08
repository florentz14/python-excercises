# -------------------------------------------------
# File Name: 03_invert_tree.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: LeetCode 226 - Invert binary tree by swapping left/right.
# -------------------------------------------------

from common import TreeNode


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    """Inverts the tree: swap left and right at each node."""
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root


if __name__ == "__main__":
    # Before:  4     After:  4
    #        /   \         /   \
    #       2     7       7     2
    #      / \   / \     / \   / \
    #     1  3  6  9    9  6  3  1
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    invert_tree(root)
    print(f"Inverted - root.left.val: {root.left.val}, root.right.val: {root.right.val}")  # 7, 2
