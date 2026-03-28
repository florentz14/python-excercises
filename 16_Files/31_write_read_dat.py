# -------------------------------------------------
# File Name: 31_write_read_dat.py
# Created: 2026-03-28
# Author: Florentino Báez
# Date: 2026-03-28
# Description: Write and read a .dat file (.dat is a generic extension; here we use UTF-8 text).
# -------------------------------------------------

from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "sample.dat"

# --- write ---
lines = [
    "record_id=1;name=Alpha;score=10\n",
    "record_id=2;name=Beta;score=22\n",
]
with open(DATA_FILE, "w", encoding="utf-8") as f:
    f.writelines(lines)
print(f"Wrote {len(lines)} lines to {DATA_FILE.name}")

# --- read ---
with open(DATA_FILE, "r", encoding="utf-8") as f:
    content = f.read()
print("Contents:")
print(content, end="")
