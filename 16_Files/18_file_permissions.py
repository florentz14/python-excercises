# -------------------------------------------------
# File Name: 18_file_permissions.py
# Author: Florentino Báez
# Date: 16_Files
# Description: File permissions. Check and modify file access modes.
# -------------------------------------------------

import os
import stat

# Create a sample file
filename = "permissions_example.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write("This file has permissions.")

print(f"Created '{filename}'.")

# Get current permissions
current_perms = os.stat(filename).st_mode
print(f"Current permissions (octal): {oct(current_perms)}")

# Set permissions to read/write for owner, read for group/others (Unix style)
# On Windows, this may not have full effect, but demonstrates the concept
try:
    os.chmod(filename, 0o644)  # rw-r--r--
    print("Set permissions to 0o644 (rw-r--r--)")
except OSError as e:
    print(f"chmod failed (expected on Windows): {e}")

# Check if file is readable/writable
print(f"File is readable: {os.access(filename, os.R_OK)}")
print(f"File is writable: {os.access(filename, os.W_OK)}")
print(f"File is executable: {os.access(filename, os.X_OK)}")

# Make file executable (add execute permission)
try:
    current = os.stat(filename).st_mode
    os.chmod(filename, current | stat.S_IEXEC)  # Add execute for owner
    print("Added execute permission for owner.")
except OSError as e:
    print(f"chmod failed: {e}")

# Create a script file and make it executable
script_file = "example_script.py"
with open(script_file, "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write("print('Hello from executable script!')\n")

try:
    os.chmod(script_file, 0o755)  # rwxr-xr-x
    print(f"Made '{script_file}' executable (0o755).")
except OSError as e:
    print(f"chmod failed: {e}")

# List files with permissions (basic)
print("\nFiles in current directory:")
for file in os.listdir("."):
    if file.endswith((".txt", ".py")):
        try:
            perms = oct(os.stat(file).st_mode)[-3:]
            print(f"{file}: {perms}")
        except:
            print(f"{file}: permission check failed")
