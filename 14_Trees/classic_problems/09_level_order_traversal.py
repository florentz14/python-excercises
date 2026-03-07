"""
#9 Binary Tree Level Order Traversal
LeetCode 102. BFS level by level.
Time: O(n), Space: O(n)
"""

from collections import deque

from common import TreeNode, build_example


def level_order(root: TreeNode | None) -> list[list[int]]:
    """BFS: return list of levels."""
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result


if __name__ == "__main__":
    root = build_example()
    print("Level order:", level_order(root))
