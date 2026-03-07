"""
#7 Binary Tree Inorder Traversal
LeetCode 94. Left -> Root -> Right (BST gives sorted order)
Time: O(n), Space: O(h)
"""

from common import TreeNode, build_example


def inorder_traversal(root: TreeNode | None) -> list[int]:
    """Inorder: Left -> Root -> Right."""
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


def inorder_iterative(root: TreeNode | None) -> list[int]:
    """Iterative using stack."""
    result, stack = [], []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.val)
        node = node.right
    return result


if __name__ == "__main__":
    root = build_example()
    print("Inorder (recursive):", inorder_traversal(root))
    print("Inorder (iterative):", inorder_iterative(root))
