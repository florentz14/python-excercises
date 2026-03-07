"""
Common TreeNode for classic tree problems.
LeetCode-style: val, left, right.
"""


class TreeNode:
    """Binary tree node (LeetCode style)."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
