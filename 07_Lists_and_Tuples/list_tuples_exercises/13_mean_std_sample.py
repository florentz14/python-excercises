# -------------------------------------------------
# File Name: 13_mean_std_sample.py
# Description: Sample numbers (comma separated), show mean and stdev
# -------------------------------------------------

import statistics
line = input("Enter numbers separated by commas: ")
nums = [float(x.strip()) for x in line.split(",")]
print(f"Mean: {statistics.mean(nums)}")
print(f"Stdev: {statistics.stdev(nums) if len(nums) > 1 else 0}")
