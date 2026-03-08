# -------------------------------------------------
# File Name: 10_update.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Merge dictionaries with update(). Existing keys overwritten,
# -------------------------------------------------

print("Example 10: Update dictionary")
print("-" * 40)

config = {"host": "localhost", "port": 8000}
print("Original:", config)

new_config = {"port": 9000, "ssl": True}    # "port" will overwrite, "ssl" is new
config.update(new_config)                     # Merge new_config into config
print("After update:", config)
