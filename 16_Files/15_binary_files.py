# -------------------------------------------------
# File Name: 15_binary_files.py
# Author: Florentino Báez
# Date: 16_Files
# Description: Binary file operations. Read/write bytes with 'rb' and 'wb'.
# -------------------------------------------------

import os

# Create a binary file with some data
binary_file = "binary_data.bin"
data = b"Hello, this is binary data!\x00\x01\x02\x03\xff"

with open(binary_file, "wb") as f:
    f.write(data)

print(f"Created binary file '{binary_file}' with {len(data)} bytes.")

# Read the binary file
with open(binary_file, "rb") as f:
    read_data = f.read()
    print(f"Read {len(read_data)} bytes: {read_data}")
    print(
        f"As string (if text): {read_data.decode('utf-8', errors='replace')}")

# Copy an image file (if exists) or simulate
image_file = "sample_image.png"
if os.path.exists(image_file):
    with open(image_file, "rb") as src, open("copy_image.png", "wb") as dst:
        dst.write(src.read())
    print("Copied image file.")
else:
    # Create a fake image binary data
    fake_image_data = b"\x89PNG\r\n\x1a\n" + b"fake image data" * 100
    with open("fake_image.png", "wb") as f:
        f.write(fake_image_data)
    print("Created fake image file for demonstration.")

# Read in chunks
chunk_size = 10
with open(binary_file, "rb") as f:
    print("\nReading in chunks:")
    while chunk := f.read(chunk_size):
        print(f"Chunk: {chunk}")

# Append to binary file
with open(binary_file, "ab") as f:
    f.write(b"\nAppended binary data.")

print(
    f"\nAppended to '{binary_file}'. Final size: {os.path.getsize(binary_file)} bytes.")
