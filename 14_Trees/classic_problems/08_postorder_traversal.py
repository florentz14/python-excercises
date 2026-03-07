"""
#8 Binary Tree Postorder Traversal
LeetCode 145. Left -> Right -> Root
Time: O(n), Space: O(h)
"""

from common import TreeNode, build_example


def postorder_traversal(root: TreeNode | None) -> list[int]:
    """Postorder: Left -> Right -> Root."""
    if not root:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]


def postorder_iterative(root: TreeNode | None) -> list[int]:
    """Iterative: reverse of preorder (root, right, left)."""
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]


if __name__ == "__main__":
    root = build_example()
    print("Postorder (recursive):", postorder_traversal(root))
    print("Postorder (iterative):", postorder_iterative(root))
