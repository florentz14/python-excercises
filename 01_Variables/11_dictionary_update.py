# Example 10: Update dictionary
print("Example 10: Update dictionary")
print("-" * 40)
config = {"host": "localhost", "port": 8000}
print("Original:", config)
new_config = {"port": 9000, "ssl": True}
config.update(new_config)
print("After update:", config)
