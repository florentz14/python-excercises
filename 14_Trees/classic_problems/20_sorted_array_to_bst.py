"""
#20 Convert Sorted Array to BST
================================
LeetCode 108. Build a height-balanced BST from sorted array.
Time: O(n), Space: O(log n) recursion stack.
"""

from common import TreeNode


def sorted_array_to_bst(nums: list[int]) -> TreeNode | None:
    """Build height-balanced BST. Pick middle as root, recurse left/right."""
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid + 1 :])
    return root


def inorder(root: TreeNode | None) -> list[int]:
    """Inorder returns sorted values for BST."""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


if __name__ == "__main__":
    arr = [-10, -3, 0, 5, 9]
    tree = sorted_array_to_bst(arr)
    print("Sorted array:", arr)
    print("Inorder (should match):", inorder(tree))
