# operations/ - Mathematical and arithmetic operations

Programs related to mathematical operations, arithmetic, and numerical algorithms.

## Structure

| # | File                        | Description                                  |
|---|-----------------------------|----------------------------------------------|
| 01 | `01_two_sum.py`            | Find two indices that sum to the target      |
| 02 | `02_aritmeticos.py`        | Operators +, -, *, /, //, %, **              |
| 03 | `03_asignacion_compuesta.py`| Operators +=, -=, *=, etc.                   |
| 04 | `04_logicos.py`            | Operators and, or, not                      |
| 05 | `05_two_sum_v2.py`         | Two Sum optimized (compact implementation)  |
| 06 | `06_two_sum_bruteforce.py` | Two Sum bruteforce O(n²), no dictionary     |
| 07 | `07_two_sum_numpy.py`      | Two Sum with NumPy (basic + matrix)         |

## Files

### `01_two_sum.py` - Two Sum

**What it does:** Given an array of integers and a target value, finds the indices
of two elements that sum exactly to that target. Returns an empty list if no such
pair exists.

**Input:**
- First line: space-separated numbers (e.g. `2 7 11 15`)
- Second line: target value (e.g. `9`)

**Output:**
- The two indices separated by space (e.g. `0 1`)
- Empty string if no solution

**Example:**
```
2 7 11 15
9
0 1
```

**Complexity:** O(n) time, O(n) space (uses hash map for single pass).

### `05_two_sum_v2.py` - Two Sum (v2, optimized)

Same algorithm as `01_two_sum`, with a more compact implementation: shorter
variable names, inlined complement, explicit dict type hint. **Best general solution.**

### `06_two_sum_bruteforce.py` - Two Sum (bruteforce)

Double nested loop, no dictionary. Compare each number with all others. Great for
learning. **Time O(n²), Space O(1).**

### `07_two_sum_numpy.py` - Two Sum (NumPy)

Two approaches: (A) NumPy + double loop, (B) matrix of sums (broadcasting).
NumPy is not ideal for Two Sum, but useful for comparison. Requires `numpy`.

### Two Sum - Implementation comparison

| Version       | Time   | Space  | Notes                                    |
|---------------|--------|--------|------------------------------------------|
| 01 / 05 (dict)| O(n)   | O(n)   | **Optimal** – single pass, hash lookup   |
| 06 (bruteforce)| O(n²) | O(1)   | Simple, good for learning                |
| 07 (NumPy A)  | O(n²)  | O(n)   | Same as bruteforce, uses np.array        |
| 07 (NumPy B)  | O(n²)  | O(n²)  | Matrix of pairwise sums                 |

### `02_aritmeticos.py` - Arithmetic operators

Basic operators: addition (+), subtraction (-), multiplication (*), division (/),
floor division (//), modulo (%), power (**).

### `03_asignacion_compuesta.py` - Compound assignment

Shorthand +=, -=, *=, /=, //= for operate-and-assign in one step.

### `04_logicos.py` - Logical operators

and, or, not with practical examples (age + license → can drive).

## How to run

```bash
cd 01_Variables_and_Types/operations
python 01_two_sum.py
```

## Requirements

- Python 3.10+ (for `list[int]` type hints)
- `numpy` for `07_two_sum_numpy.py` only (`pip install numpy`)
