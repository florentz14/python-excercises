"""
#19 Lowest Common Ancestor - BST - LeetCode 235
===============================================
LCA in BST: use property Left < Root < Right.
If p,q < root -> go left; if p,q > root -> go right; else root is LCA.
"""

from common import TreeNode


def lowest_common_ancestor_bst(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """Returns LCA of p and q in BST."""
    if root is None:
        return None
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor_bst(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor_bst(root.right, p, q)
    return root


if __name__ == "__main__":
    root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
    p, q = root.left, root.left.right  # 2 and 4
    lca = lowest_common_ancestor_bst(root, p, q)
    print("LCA(2,4) in BST:", lca.val if lca else None)  # 2
