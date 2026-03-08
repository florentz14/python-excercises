# -------------------------------------------------
# File Name: 64_two_pointers_pattern.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Two pointers pattern. Common technique for array/string problems.
# -------------------------------------------------

def is_palindrome(s: str) -> bool:
    """Two pointers from both ends. O(n)."""
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """Two pointers (sorted array). Returns indices (1-based). O(n)."""
    l, r = 0, len(nums) - 1
    while l < r:
        total = nums[l] + nums[r]
        if total == target:
            return [l + 1, r + 1]
        if total < target:
            l += 1
        else:
            r -= 1
    return []


def max_area(height: list[int]) -> int:
    """Container with most water. Two pointers. O(n)."""
    l, r = 0, len(height) - 1
    best = 0
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        best = max(best, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return best


if __name__ == "__main__":
    print("Palindrome 'A man a plan a canal: Panama':", is_palindrome("A man a plan a canal: Panama"))
    print("Two Sum sorted [2,7,11,15], target=9:", two_sum_sorted([2, 7, 11, 15], 9))
    print("Max Area [1,8,6,2,5,4,8,3,7]:", max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
