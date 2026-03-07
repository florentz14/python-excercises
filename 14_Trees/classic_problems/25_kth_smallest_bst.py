"""
#25 Kth Smallest Element in BST
================================
LeetCode 230. Inorder gives sorted order; kth element is answer.
Time: O(k) with early stop, O(n) worst. Space: O(h).
"""

from common import TreeNode


def kth_smallest(root: TreeNode | None, k: int) -> int:
    """Returns kth smallest value in BST (1-indexed)."""
    count = 0
    result = 0

    def inorder(node: TreeNode | None) -> None:
        nonlocal count, result
        if not node:
            return
        inorder(node.left)
        count += 1
        if count == k:
            result = node.val
            return
        inorder(node.right)

    inorder(root)
    return result


if __name__ == "__main__":
    # BST:     5
    #        /   \
    #       3     6
    #      / \
    #     2   4
    #    /
    #   1
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))
    root.right = TreeNode(6)
    print("K=3, kth smallest:", kth_smallest(root, 3))  # 3
