# -------------------------------------------------
# File Name: 13_delete_bst.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: LeetCode 450 - Delete node in BST (3 cases: 0, 1, 2 children).
# -------------------------------------------------

from common import TreeNode


def min_value_node(node: TreeNode) -> TreeNode:
    """Find leftmost (minimum) node in subtree."""
    while node.left:
        node = node.left
    return node


def delete_node(root: TreeNode | None, key: int) -> TreeNode | None:
    """Delete node with key from BST. Return root."""
    if root is None:
        return None
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        # Two children: replace with inorder successor (min of right subtree)
        successor = min_value_node(root.right)
        root.val = successor.val
        root.right = delete_node(root.right, successor.val)
    return root


if __name__ == "__main__":
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6))
    root = delete_node(root, 3)
    print("After delete(3): root.left.val =", root.left.val if root and root.left else None)  # 4
