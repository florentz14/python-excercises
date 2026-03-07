"""
14_Trees - Trie (Prefix Tree)
=========================================
Structure for strings. O(word_length) insert/search.
Used in: autocomplete, dictionaries, search engines.
"""


class TrieNode:
    """Trie node with children map."""

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    """Trie (prefix tree) for string storage and search."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert word. O(m) where m = len(word)."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        """Return True if word exists. O(m)."""
        node = self._traverse(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        """Return True if any word has prefix. O(m)."""
        return self._traverse(prefix) is not None

    def _traverse(self, s):
        """Traverse to node for string s. Returns node or None."""
        node = self.root
        for char in s:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def autocomplete(self, prefix):
        """Return all words with given prefix."""
        node = self._traverse(prefix)
        if node is None:
            return []
        result = []

        def _collect(n, path):
            if n.is_end:
                result.append(prefix + path)
            for char, child in n.children.items():
                _collect(child, path + char)

        _collect(node, "")
        return result


if __name__ == "__main__":
    print("=== Trie (Prefix Tree) ===\n")
    trie = Trie()
    for w in ["car", "card", "care", "cat", "can"]:
        trie.insert(w)
    print("search('car'):", trie.search("car"))
    print("search('care'):", trie.search("care"))
    print("starts_with('ca'):", trie.starts_with("ca"))
    print("autocomplete('car'):", trie.autocomplete("car"))
    print("\nO(word_length). Used in: autocomplete, dictionaries.")
