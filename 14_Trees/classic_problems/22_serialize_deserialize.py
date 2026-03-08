# -------------------------------------------------
# File Name: 22_serialize_deserialize.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: LeetCode 297 - Serialize/deserialize binary tree to string.
# -------------------------------------------------

from common import TreeNode


def serialize(root: TreeNode | None) -> str:
    """Preorder: root,left,right. Use 'null' for None."""
    if not root:
        return "null"
    return f"{root.val},{serialize(root.left)},{serialize(root.right)}"


def deserialize(data: str) -> TreeNode | None:
    """Parse preorder string back to tree."""
    it = iter(data.split(","))

    def build() -> TreeNode | None:
        val = next(it, "null")
        if val == "null":
            return None
        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node

    return build()


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    s = serialize(root)
    print("Serialized:", s)
    restored = deserialize(s)
    print("Deserialized root val:", restored.val if restored else None)
