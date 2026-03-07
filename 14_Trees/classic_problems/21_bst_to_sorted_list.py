"""
#21 Convert BST to Sorted List (Inorder)
=========================================
BST inorder traversal yields sorted order.
Time: O(n), Space: O(n) for result, O(h) recursion.
"""

from common import TreeNode


def bst_to_sorted_list(root: TreeNode | None) -> list[int]:
    """Inorder traversal of BST returns sorted list."""
    result = []

    def inorder(node: TreeNode | None) -> None:
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    inorder(root)
    return result


if __name__ == "__main__":
    # BST:     4
    #        /   \
    #       2     6
    #      / \   / \
    #     1   3 5   7
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(6, TreeNode(5), TreeNode(7))
    print("BST to sorted list:", bst_to_sorted_list(root))
