# -------------------------------------------------
# File Name: 06_preorder_traversal.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: LeetCode 144 - Binary tree preorder traversal (Root, Left, Right).
# -------------------------------------------------

from common import TreeNode, build_example


def preorder_traversal(root: TreeNode | None) -> list[int]:
    """Preorder: Root -> Left -> Right."""
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


def preorder_iterative(root: TreeNode | None) -> list[int]:
    """Iterative using stack."""
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


if __name__ == "__main__":
    root = build_example()
    print("Preorder (recursive):", preorder_traversal(root))
    print("Preorder (iterative):", preorder_iterative(root))
