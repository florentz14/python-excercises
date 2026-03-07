# operations/ - Mathematical and arithmetic operations

Programs related to mathematical operations, arithmetic, and numerical algorithms.

## Structure

| #   | File                                    | Description                                    |
| --- | --------------------------------------- | ---------------------------------------------- | --------------- |
| 01  | `01_arithmetic_operators.py`            | Basic arithmetic operators (+, -, \*, /, etc.) |
| 02  | `02_comparison_operators.py`            | Comparison operators (==, !=, <, >, etc.)      |
| 03  | `03_logical_operators.py`               | Logical operators (and, or, not)               |
| 04  | `04_assignment_operators.py`            | Assignment operators (=, +=, -=, etc.)         |
| 05  | `05_bitwise_operators.py`               | Bitwise operators (&,                          | , ^, ~, <<, >>) |
| 06  | `06_operator_precedence.py`             | Operator precedence rules                      |
| 07  | `07_absolute_round_power.py`            | Absolute value, rounding, power functions      |
| 08  | `08_floor_ceil_sqrt.py`                 | Floor, ceil, square root functions             |
| 09  | `09_division_types.py`                  | Different types of division (/, //, %)         |
| 10  | `10_modulo_examples.py`                 | Modulo operator examples                       |
| 11  | `11_even_odd_check.py`                  | Check if number is even or odd                 |
| 12  | `12_swap_variables.py`                  | Swap two variables without temp                |
| 13  | `13_increment_decrement.py`             | Increment and decrement operations             |
| 14  | `14_basic_calculator.py`                | Simple calculator with basic operations        |
| 15  | `15_percentage_calculations.py`         | Percentage calculations                        |
| 16  | `16_average_numbers.py`                 | Calculate average of numbers                   |
| 17  | `17_min_max_numbers.py`                 | Find min and max of numbers                    |
| 18  | `18_sum_numbers.py`                     | Sum of numbers                                 |
| 19  | `19_power_and_roots.py`                 | Power and root calculations                    |
| 20  | `20_temperature_conversion.py`          | Convert between Celsius and Fahrenheit         |
| 21  | `21_simple_interest.py`                 | Calculate simple interest                      |
| 22  | `22_compound_interest_basic.py`         | Basic compound interest calculation            |
| 23  | `23_distance_formula.py`                | Distance formula between two points            |
| 24  | `24_area_perimeter.py`                  | Area and perimeter calculations                |
| 25  | `25_basic_math_menu.py`                 | Menu-driven basic math operations              |
| 26  | `26_two_sum.py`                         | Find two indices that sum to the target        |
| 27  | `27_aritmeticos.py`                     | Arithmetic operators in Spanish                |
| 28  | `28_compound_assignment.py`             | Compound assignment operators                  |
| 29  | `29_logicos.py`                         | Logical operators in Spanish                   |
| 30  | `30_two_sum_v2.py`                      | Two Sum optimized (compact implementation)     |
| 31  | `31_two_sum_bruteforce.py`              | Two Sum bruteforce O(n²), no dictionary        |
| 32  | `32_two_sum_numpy.py`                   | Two Sum with NumPy                             |
| 33  | `33_max_subarray_sum_bruteforce.py`     | Max sum subarray bruteforce                    |
| 34  | `34_max_subarray_sum_sliding_window.py` | Max sum subarray sliding window                |

## Files

### Basic Operations (01-25)

These files demonstrate fundamental mathematical operations and calculations in Python.

### Algorithm Examples (26-34)

#### `26_two_sum.py` - Two Sum

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

#### `30_two_sum_v2.py` - Two Sum (v2, optimized)

Same algorithm as `26_two_sum`, with a more compact implementation: shorter
variable names, inlined complement, explicit dict type hint. **Best general solution.**

#### `31_two_sum_bruteforce.py` - Two Sum (bruteforce)

Double nested loop, no dictionary. Compare each number with all others. Great for
learning. **Time O(n²), Space O(1).**

#### `32_two_sum_numpy.py` - Two Sum (NumPy)

Two approaches: (A) NumPy + double loop, (B) matrix of sums (broadcasting).
NumPy is not ideal for Two Sum, but useful for comparison. Requires `numpy`.

#### Two Sum - Implementation comparison

| Version         | Time  | Space | Notes                                  |
| --------------- | ----- | ----- | -------------------------------------- |
| 26 / 30 (dict)  | O(n)  | O(n)  | **Optimal** – single pass, hash lookup |
| 31 (bruteforce) | O(n²) | O(1)  | Simple, good for learning              |
| 32 (NumPy A)    | O(n²) | O(n)  | Same as bruteforce, uses np.array      |
| 32 (NumPy B)    | O(n²) | O(n²) | Matrix of pairwise sums                |

#### `27_aritmeticos.py` - Arithmetic operators (Spanish)

Basic operators: addition (+), subtraction (-), multiplication (\*), division (/),
floor division (//), modulo (%), power (\*\*).

#### `28_compound_assignment.py` - Compound assignment

Shorthand +=, -=, \*=, /=, //= for operate-and-assign in one step.

#### `29_logicos.py` - Logical operators (Spanish)

and, or, not with practical examples (age + license → can drive).

#### `33_max_subarray_sum_bruteforce.py` - Max sum subarray (bruteforce)

For each possible window of size k, compute the sum from scratch.
**Time O(n·k), Space O(1).**

#### `34_max_subarray_sum_sliding_window.py` - Max sum subarray (sliding window)

Update the window sum incrementally: subtract element leaving, add element entering.
**Time O(n), Space O(1).**

## How to run

```bash
cd 01_Variables_and_Types/operations
python 01_arithmetic_operators.py
```

## Requirements

- Python 3.10+ (for `list[int]` type hints)
- `numpy` for `32_two_sum_numpy.py` only (`pip install numpy`)
