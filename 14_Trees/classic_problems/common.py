# -------------------------------------------------
# File Name: common.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: Common TreeNode class (LeetCode-style) for classic tree problems.
# -------------------------------------------------

class TreeNode:
    """Binary tree node (LeetCode style)."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
