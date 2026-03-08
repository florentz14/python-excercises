# -------------------------------------------------
# File Name: 11_hash_table_vs_dict.py
# Author: Florentino Báez
# Date: 19_Hash_Tables
# Description: Compare custom HashTable with Python dict (CPython open addressing).
# -------------------------------------------------

import time
from pathlib import Path
import importlib.util

# Load chaining module (filename starts with digit)
_spec = importlib.util.spec_from_file_location(
    "ht_chaining", Path(__file__).parent / "01_hash_table_chaining.py"
)
ht_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ht_module)
HashTable = ht_module.HashTable


def benchmark_insert(n, use_dict=True):
    if use_dict:
        d = {}
        start = time.perf_counter()
        for i in range(n):
            d[f"key_{i}"] = i
        return time.perf_counter() - start
    else:
        ht = HashTable(size=n * 2)  # avoid high load
        start = time.perf_counter()
        for i in range(n):
            ht.insert(f"key_{i}", i)
        return time.perf_counter() - start


def benchmark_lookup(n, use_dict=True):
    if use_dict:
        d = {f"key_{i}": i for i in range(n)}
        start = time.perf_counter()
        for i in range(n):
            _ = d[f"key_{i}"]
        return time.perf_counter() - start
    else:
        ht = HashTable(size=n * 2)
        for i in range(n):
            ht.insert(f"key_{i}", i)
        start = time.perf_counter()
        for i in range(n):
            _ = ht.get(f"key_{i}")
        return time.perf_counter() - start


if __name__ == "__main__":
    print("=" * 50)
    print("HASH TABLE vs dict")
    print("=" * 50)

    n = 10_000
    t_dict_ins = benchmark_insert(n, True)
    t_ht_ins = benchmark_insert(n, False)
    t_dict_lk = benchmark_lookup(n, True)
    t_ht_lk = benchmark_lookup(n, False)

    print(f"\nn = {n}")
    print(f"Insert:  dict={t_dict_ins:.4f}s  HashTable={t_ht_ins:.4f}s  ratio={t_ht_ins/t_dict_ins:.1f}x")
    print(f"Lookup:  dict={t_dict_lk:.4f}s  HashTable={t_ht_lk:.4f}s  ratio={t_ht_lk/t_dict_lk:.1f}x")
    print("\nCPython dict uses open addressing, optimized C implementation.")
    print("Our HashTable is Python; dict is typically 10-100x faster.")
