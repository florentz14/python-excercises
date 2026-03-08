# -------------------------------------------------
# File Name: 04_huffman.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Huffman coding for lossless compression. Builds tree by merging lowest-frequency nodes. Assigns shorter codes to more frequent characters. O(n log n).
# -------------------------------------------------

import heapq


class HuffmanNode:
    """Node in the Huffman tree (leaf or internal)."""

    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

    def is_leaf(self):
        return self.left is None and self.right is None


def build_huffman_tree(frequencies):
    """Build Huffman tree from char->freq dict. Returns root node."""
    heap = []
    for char, freq in frequencies.items():
        heapq.heappush(heap, HuffmanNode(char, freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        # Merge into internal node with combined frequency
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0] if heap else None


def _generate_codes(node, code="", codes=None):
    """DFS: assign binary code to each leaf (character)."""
    if codes is None:
        codes = {}
    if node is None:
        return codes
    if node.is_leaf():
        codes[node.char] = code if code else "0"
        return codes
    _generate_codes(node.left, code + "0", codes)
    _generate_codes(node.right, code + "1", codes)
    return codes


def huffman_encode(text):
    """Returns (code_dict, encoded_string)."""
    frequencies = {}
    for c in text:
        frequencies[c] = frequencies.get(c, 0) + 1

    root = build_huffman_tree(frequencies)
    if root is None:
        return {}, ""

    codes = _generate_codes(root)
    encoded = ''.join(codes[c] for c in text)
    return codes, encoded


if __name__ == "__main__":
    print("=== Greedy Algorithms: Huffman Coding ===\n")

    text = "hello world"
    print(f"Original text: '{text}'")

    codes, encoded = huffman_encode(text)
    print("\nHuffman codes:")
    for char, code in sorted(codes.items()):
        print(f"  '{char}': {code}")

    print(f"\nEncoded string: {encoded}")
    print(f"Original length: {len(text) * 8} bits (ASCII)")
    print(f"Encoded length: {len(encoded)} bits")
    print(f"Compression: {len(encoded) / (len(text) * 8) * 100:.1f}%")
