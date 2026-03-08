# -------------------------------------------------
# File Name: 08_load_factor_analysis.py
# Author: Florentino Báez
# Date: 19_Hash_Tables
# Description: Analyze performance vs load factor α = n/m.
# -------------------------------------------------

import random

def _hash(key, size):
    if isinstance(key, int):
        return key % size
    return sum(ord(c) for c in str(key)) % size


def count_probes_linear(keys, size):
    """Count average probes for linear probing."""
    table = [None] * size
    total_probes = 0

    for key in keys:
        index = _hash(key, size)
        probes = 0
        while table[index] is not None:
            index = (index + 1) % size
            probes += 1
        table[index] = key
        total_probes += probes

    return total_probes / len(keys)


def count_probes_chaining(keys, size):
    """Count average chain length for chaining."""
    table = [[] for _ in range(size)]

    for key in keys:
        index = _hash(key, size)
        table[index].append(key)

    total = sum(len(chain) for chain in table)
    return total / len(keys)


if __name__ == "__main__":
    print("=" * 50)
    print("LOAD FACTOR ANALYSIS (α = n/m)")
    print("=" * 50)

    sizes = [100, 200, 500]
    for m in sizes:
        n = int(m * 0.5)  # α = 0.5
        keys = list(range(n))
        random.shuffle(keys)

        avg_linear = count_probes_linear(keys, m)
        avg_chain = count_probes_chaining(keys, m)

        alpha = n / m
        print(f"\nm={m}, n={n}, α={alpha:.2f}")
        print(f"  Linear probing avg probes/insert: {avg_linear:.2f}")
        print(f"  Chaining avg chain length: {avg_chain:.2f}")

    print("\n--- High load (α=0.9) ---")
    m, n = 100, 90
    keys = list(range(n))
    random.shuffle(keys)
    avg = count_probes_linear(keys, m)
    print(f"α=0.9: avg probes = {avg:.2f} (degradation)")
