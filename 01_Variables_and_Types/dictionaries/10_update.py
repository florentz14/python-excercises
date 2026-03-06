# -------------------------------------------------
# File Name: 10_update.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Update a Dictionary with Another Dictionary.
#              update() merges key-value pairs from another
#              dict. Existing keys are overwritten; new keys
#              are added. Modifies the dict in place.
# -------------------------------------------------

# Example 10: Update dictionary
print("Example 10: Update dictionary")
print("-" * 40)

config = {"host": "localhost", "port": 8000}
print("Original:", config)

new_config = {"port": 9000, "ssl": True}    # "port" will overwrite, "ssl" is new
config.update(new_config)                     # Merge new_config into config
print("After update:", config)
