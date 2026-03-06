"""
16_Files - Exercise 08: Copy and move files
===========================================
shutil.copy() / copy2() for copying; shutil.move() for moving/renaming.
"""

import shutil
from pathlib import Path

# Create source file
source = Path("example_08_source.txt")
source.write_text("Content of source file.\n", encoding="utf-8")
print(f"Source file created: {source}")

# Copy file (shutil.copy: content only; copy2: also metadata)
copy_dest = Path("example_08_copy.txt")
shutil.copy2(source, copy_dest)
print(f"Copied to: {copy_dest}")

# Move (or rename) file
move_dest = Path("example_08_moved.txt")
shutil.move(str(source), str(move_dest))
print(f"Moved/renamed to: {move_dest}")

# Verify: source no longer exists, others do
print(f"\nDoes source exist? {source.exists()}")
print(f"Does copy exist? {copy_dest.exists()}")
print(f"Does moved exist? {move_dest.exists()}")

# Optional cleanup (uncomment to remove after running)
# copy_dest.unlink()
# move_dest.unlink()
