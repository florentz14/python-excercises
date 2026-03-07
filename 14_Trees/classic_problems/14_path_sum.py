"""
#14 Path Sum - LeetCode 112
================================
Check if there exists a root-to-leaf path with target sum.
Pattern: DFS recursion.
"""

from common import TreeNode


def has_path_sum(root: TreeNode | None, target: int) -> bool:
    """Returns True if any root-to-leaf path sums to target."""
    if root is None:
        return False
    if root.left is None and root.right is None:
        return root.val == target
    remaining = target - root.val
    return has_path_sum(root.left, remaining) or has_path_sum(root.right, remaining)


if __name__ == "__main__":
    # Tree: 5 -> 4 -> 11 (leaf), path 5+4+11=20
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
    print("Path Sum 22:", has_path_sum(root, 22))  # True: 5+4+11+2
    print("Path Sum 27:", has_path_sum(root, 27))  # True: 5+8+13+1
    print("Path Sum 100:", has_path_sum(root, 100))  # False
