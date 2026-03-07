"""
16_Files - Exercise 17: Working with temporary files using tempfile
==================================================================
Temporary files are useful for scripts, testing, and intermediate data.
They are automatically cleaned up when closed (or on program exit).
"""

import tempfile
import os

# Create a temporary file that is automatically deleted when closed
print("Creating temporary file with NamedTemporaryFile:")
with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".txt") as temp_file:
    temp_file.write("This is temporary data.\n")
    temp_file.write("It will be deleted automatically.\n")
    temp_filename = temp_file.name
    print(f"Temporary file created: {temp_filename}")

# Read back the temporary file
with open(temp_filename, "r") as f:
    content = f.read()
    print(f"Content: {content}")

# Manually delete (since delete=False)
os.unlink(temp_filename)
print("Temporary file manually deleted.")

# Temporary file that deletes automatically
print("\nCreating temporary file that auto-deletes:")
with tempfile.NamedTemporaryFile(mode="w+", suffix=".log") as temp_file:
    temp_file.write("Log entry 1\n")
    temp_file.write("Log entry 2\n")
    temp_filename = temp_file.name
    print(f"Temporary file: {temp_filename}")
    print(f"File exists inside context: {os.path.exists(temp_filename)}")

print(f"File exists after context: {os.path.exists(temp_filename)}")

# Temporary directory
print("\nCreating temporary directory:")
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Temporary directory: {temp_dir}")
    temp_file_path = os.path.join(temp_dir, "data.txt")
    with open(temp_file_path, "w") as f:
        f.write("Data in temp directory")
    print(f"Created file in temp dir: {temp_file_path}")
    print(f"Directory exists: {os.path.exists(temp_dir)}")

print(f"Directory exists after context: {os.path.exists(temp_dir)}")

# Spooled temporary file (keeps in memory until threshold)
print("\nSpooled temporary file:")
with tempfile.SpooledTemporaryFile(mode="w+", max_size=100) as temp_file:
    for i in range(10):
        temp_file.write(f"Line {i}\n")
    temp_file.seek(0)
    content = temp_file.read()
    print(f"Spooled content: {content[:50]}...")