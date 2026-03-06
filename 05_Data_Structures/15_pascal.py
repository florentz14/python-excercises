# -------------------------------------------------
# File: 15_pascal.py (Pascal's Triangle & Binomial Coefficients)
# -------------------------------------------------
# Author: Florentino Báez
# Module: Data Structures - Mathematical Algorithms
#
# Description:
#   Pascal's Triangle: each element is the sum of the two above it.
#   - pascal_rows(n): first n rows.
#   - binomial_coefficient(n, k): C(n,k) = n!/(k!(n-k)!).
#   - pascal_row_n(n): generates only row n.
#
# Complexity: O(n²) for n full rows; O(n) for single row.
# -------------------------------------------------


def pascal_rows(n):
    """Generates the first n rows of Pascal's Triangle."""
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle


def print_pascal(n):
    """Prints Pascal's Triangle in centered visual form."""
    triangle = pascal_rows(n)
    width = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        print(' '.join(map(str, row)).center(width))


def binomial_coefficient(n, k):
    """Returns C(n, k) = n! / (k! * (n-k)!)."""
    if k > n or k < 0:
        return 0
    if k > n - k:
        k = n - k
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result


def pascal_row_n(n):
    """Generates only row n of Pascal's Triangle (0-indexed)."""
    row = [1]
    for k in range(n):
        next_val = row[k] * (n - k) // (k + 1)
        row.append(next_val)
    return row


if __name__ == "__main__":
    print("=== Mathematical Algorithms: Pascal's Triangle ===\n")

    print("Pascal's Triangle (10 rows):")
    print_pascal(10)
    print(f"\nBinomial coefficient C(5, 2) = {binomial_coefficient(5, 2)}")
    print(f"Row 5 of Pascal's Triangle: {pascal_row_n(5)}")
