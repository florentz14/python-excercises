# -------------------------------------------------
# File: 52_complexity.py (Sorting - Complexity Analysis)
# -------------------------------------------------
# Author: Florentino Báez
# Module: Data Structures - Sorting Algorithms
#
# Description:
#   Comparative table of time complexity (best, average, worst) for
#   all sorting algorithms. Includes space complexity and stability.
#   Selection guide based on data type and constraints.
# -------------------------------------------------


def analyze_complexity():
    """Prints complexity table for all sorting algorithms."""
    print("\nTime complexity of sorting methods:")
    print("=" * 90)
    print(f"{'Method':<28} {'Best':<14} {'Average':<14} {'Worst':<14} {'Space':<10} {'Stable'}")
    print("-" * 90)
    datos = [
        # O(n²) algorithms - Simple comparison-based
        ("Bubble Sort",             "O(n)",       "O(n²)",      "O(n²)",      "O(1)",   "Yes"),
        ("Bubble Sort Optimized",   "O(n)",       "O(n²)",      "O(n²)",      "O(1)",   "Yes"),
        ("Selection Sort",          "O(n²)",      "O(n²)",      "O(n²)",      "O(1)",   "No"),
        ("Insertion Sort",          "O(n)",       "O(n²)",      "O(n²)",      "O(1)",   "Yes"),
        ("Cocktail Sort",           "O(n)",       "O(n²)",      "O(n²)",      "O(1)",   "Yes"),
        ("Comb Sort",               "O(n log n)", "O(n²/2^p)",  "O(n²)",      "O(1)",   "No"),

        # O(n log n) algorithms - Efficient comparison-based
        ("Shell Sort (Knuth)",      "O(n log n)", "O(n^(4/3))", "O(n^(3/2))", "O(1)",   "No"),
        ("Merge Sort",              "O(n log n)", "O(n log n)", "O(n log n)", "O(n)",   "Yes"),
        ("Quick Sort",              "O(n log n)", "O(n log n)", "O(n²)",      "O(log n)", "No"),
        ("Heap Sort",               "O(n log n)", "O(n log n)", "O(n log n)", "O(1)",   "No"),
        ("Tim Sort",                "O(n)",       "O(n log n)", "O(n log n)", "O(n)",   "Yes"),

        # Non-comparison algorithms
        ("Counting Sort",           "O(n + k)",   "O(n + k)",   "O(n + k)",   "O(k)",   "Yes"),
        ("Radix Sort",              "O(nk)",      "O(nk)",      "O(nk)",      "O(n+k)", "Yes"),
        ("Bucket Sort",             "O(n + k)",   "O(n + k)",   "O(n²)",      "O(n+k)", "Yes"),

        # Python built-in
        ("Python sorted() (Tim)",   "O(n)",       "O(n log n)", "O(n log n)", "O(n)",   "Yes"),
    ]
    for method, best, avg, worst, space, stable in datos:
        print(f"{method:<28} {best:<14} {avg:<14} {worst:<14} {space:<10} {stable}")
    print("=" * 90)

    print("""
Notes:
  n = number of elements
  k = value range (Counting/Radix) or number of buckets (Bucket)
  p = number of increments (Comb Sort)
  Stable  = preserves relative order of equal elements
  In-place = O(1) extra space (excluding original list)

Summary:
  - Small lists (<50):     Insertion Sort
  - General purpose:      Tim Sort (Python sorted()) or Merge Sort
  - Nearly sorted data:   Tim Sort or Insertion Sort
  - Bounded integer range: Counting Sort or Radix Sort
  - Uniform distribution: Bucket Sort
  - Fast in-place:        Quick Sort or Heap Sort
  - Shell Sort:           Good balance of simplicity and speed
""")


if __name__ == "__main__":
    print("=== Complexity Analysis ===\n")
    analyze_complexity()
