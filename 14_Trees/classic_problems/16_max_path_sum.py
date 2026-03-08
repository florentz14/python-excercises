# -------------------------------------------------
# File Name: 16_max_path_sum.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: LeetCode 124 - Maximum path sum (path may not pass root).
# -------------------------------------------------

from common import TreeNode


def max_path_sum(root: TreeNode | None) -> int:
    """Returns maximum path sum. Path = any sequence of connected nodes."""
    max_sum = [float("-inf")]

    def gain(node: TreeNode | None) -> int:
        if node is None:
            return 0
        left_gain = max(0, gain(node.left))
        right_gain = max(0, gain(node.right))
        path_through = node.val + left_gain + right_gain
        max_sum[0] = max(max_sum[0], path_through)
        return node.val + max(left_gain, right_gain)

    gain(root)
    return int(max_sum[0])


if __name__ == "__main__":
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print("Max path sum:", max_path_sum(root))  # 42: 15+20+7
