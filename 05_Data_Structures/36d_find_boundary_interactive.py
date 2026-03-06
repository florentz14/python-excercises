# ------------------------------------------------------------
# File: 36d_find_boundary_interactive.py
# Find First True - Interactive version (matches the script from the image)
#
# Input: space-separated "true" or "false" (e.g. "false false true true")
# Output: index of first True, or -1
#
# Run: python 36d_find_boundary_interactive.py
#      Then enter: false false true true
# ------------------------------------------------------------


def find_boundary(arr: list[bool]) -> int:
    """Index of first True in boolean list, or -1."""
    if not arr:
        return -1
    left, right = 0, len(arr) - 1
    boundary_index = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index


if __name__ == "__main__":
    arr = [x.lower() == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)
