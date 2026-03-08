# -------------------------------------------------
# File Name: 15_path_sum_ii.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: LeetCode 113 - Find all root-to-leaf paths with target sum.
# -------------------------------------------------

from common import TreeNode


def path_sum_ii(root: TreeNode | None, target: int) -> list[list[int]]:
    """Returns all root-to-leaf paths that sum to target."""
    result: list[list[int]] = []

    def dfs(node: TreeNode | None, remaining: int, path: list[int]) -> None:
        if node is None:
            return
        path.append(node.val)
        if node.left is None and node.right is None and remaining == node.val:
            result.append(path[:])
        else:
            dfs(node.left, remaining - node.val, path)
            dfs(node.right, remaining - node.val, path)
        path.pop()

    dfs(root, target, [])
    return result


if __name__ == "__main__":
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    print("Paths summing to 22:", path_sum_ii(root, 22))
