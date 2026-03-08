# -------------------------------------------------
# File Name: 02_min_depth.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: LeetCode 111 - Minimum depth via BFS (first leaf = min depth).
# -------------------------------------------------

from collections import deque
from common import TreeNode


def min_depth(root: TreeNode | None) -> int:
    """Returns the minimum depth (distance to nearest leaf)."""
    if root is None:
        return 0
    q = deque([(root, 1)])
    while q:
        node, depth = q.popleft()
        if node.left is None and node.right is None:
            return depth
        if node.left:
            q.append((node.left, depth + 1))
        if node.right:
            q.append((node.right, depth + 1))
    return 0


if __name__ == "__main__":
    # Tree:    3
    #        /   \
    #       9    20
    #           /  \
    #          15   7
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(f"Min depth: {min_depth(root)}")  # 2 (3 -> 9)
