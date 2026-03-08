# -------------------------------------------------
# File Name: 17_binary_tree_paths.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: LeetCode 257 - Return all root-to-leaf paths as strings.
# -------------------------------------------------

from common import TreeNode


def binary_tree_paths(root: TreeNode | None) -> list[str]:
    """Returns all root-to-leaf paths like '1->2->5'."""
    result: list[str] = []

    def dfs(node: TreeNode | None, path: list[str]) -> None:
        if node is None:
            return
        path.append(str(node.val))
        if node.left is None and node.right is None:
            result.append("->".join(path))
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        path.pop()

    dfs(root, [])
    return result


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
    print("Paths:", binary_tree_paths(root))  # ['1->2->5', '1->3']
