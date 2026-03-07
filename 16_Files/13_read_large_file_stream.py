"""
16_Files - Exercise 13: Reading large files efficiently with streaming
======================================================================
Reading large files line by line prevents loading the entire file into memory.
Useful for log processing, data analysis, etc.
"""

# Create a large file for demonstration (simulate large data)
large_file = "large_file.txt"
with open(large_file, "w", encoding="utf-8") as f:
    for i in range(10000):  # Simulate 10,000 lines
        f.write(f"Line {i}: This is a line of data.\n")

print(f"Created '{large_file}' with 10,000 lines.")

# Read the large file efficiently line by line
line_count = 0
total_length = 0

with open(large_file, "r", encoding="utf-8") as f:
    for line in f:
        line_count += 1
        total_length += len(line.strip())
        # Process each line (here we just count and sum lengths)
        if line_count <= 5:  # Print first 5 lines as example
            print(f"Processing: {line.strip()}")

print(f"\nProcessed {line_count} lines.")
print(f"Total characters in lines: {total_length}")

# Alternative: read in chunks for binary files or very large text
chunk_size = 1024  # 1KB chunks
bytes_read = 0

with open(large_file, "rb") as f:
    while chunk := f.read(chunk_size):
        bytes_read += len(chunk)
        # Process chunk here

print(f"Read {bytes_read} bytes in chunks.")
