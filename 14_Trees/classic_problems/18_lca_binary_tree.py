"""
#18 Lowest Common Ancestor - Binary Tree - LeetCode 236
========================================================
Find LCA of two nodes (nodes exist in tree).
Pattern: Recursion, return node if found.
"""

from common import TreeNode


def lowest_common_ancestor(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """Returns LCA of p and q in binary tree."""
    if root is None or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right


if __name__ == "__main__":
    # Tree: 3(5(6,2(7,4)), 1(0,8))
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n4 = TreeNode(4)
    n2 = TreeNode(2, n7, n4)
    n5 = TreeNode(5, n6, n2)
    n0 = TreeNode(0)
    n8 = TreeNode(8)
    n1 = TreeNode(1, n0, n8)
    root = TreeNode(3, n5, n1)
    lca = lowest_common_ancestor(root, n6, n4)
    print("LCA(6,4):", lca.val if lca else None)  # 5
