# -------------------------------------------------
# File Name: 14_file_seek_tell.py
# Author: Florentino Báez
# Date: 16_Files
# Description: File seek and tell. Random access with seek() and tell().
# -------------------------------------------------

filename = "seek_tell_example.txt"
content = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Created '{filename}' with content: {content}")

# Demonstrate tell() and seek()
with open(filename, "r", encoding="utf-8") as f:
    print(f"Initial position: {f.tell()}")  # Should be 0

    # Read first 5 characters
    data = f.read(5)
    print(f"Read: '{data}', position now: {f.tell()}")

    # Seek to position 10
    f.seek(10)
    print(f"After seek(10), position: {f.tell()}")

    # Read from there
    data = f.read(5)
    print(f"Read from position 10: '{data}', position now: {f.tell()}")

    # Seek relative to current position
    f.seek(5, 1)  # 5 bytes from current position
    print(f"After seek(5, 1), position: {f.tell()}")

    # Seek relative to end
    f.seek(-5, 2)  # 5 bytes from end
    print(f"After seek(-5, 2), position: {f.tell()}")
    data = f.read()
    print(f"Read from near end: '{data}'")

# Binary file example
binary_file = "binary_example.bin"
with open(binary_file, "wb") as f:
    f.write(b"Hello World! Binary data here.")

with open(binary_file, "rb") as f:
    print(f"\nBinary file initial position: {f.tell()}")
    f.seek(6)  # Skip "Hello "
    data = f.read(5)
    print(f"Read from binary file: {data}, position: {f.tell()}")
