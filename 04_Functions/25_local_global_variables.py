# -------------------------------------------------
# File: 25_local_global_variables.py
# Description: Local and global variables demo.
#              Using 'global' keyword to modify variables.
# -------------------------------------------------

# Global variable - accessible from anywhere in the file
counter = 0
message = "Hello from global"

def increment_counter():
    """Uses global keyword to modify a global variable."""
    global counter  # Required to modify the global variable
    counter += 1
    print(f"Counter incremented to: {counter}")

def show_message():
    """Reads global variable without modifying it (no global keyword needed)."""
    print(f"Global message: {message}")

def use_local_variable():
    """Creates a local variable that only exists inside this function."""
    local_var = "I am local"  # Local variable
    print(f"Local variable: {local_var}")
    # This local_var will be destroyed when the function ends

def mix_local_and_global():
    """Shows both local and global variables in the same function."""
    global counter
    local_result = counter * 2  # local_result is local
    counter += 5                # counter is global
    print(f"Global counter: {counter}")
    print(f"Local result (counter * 2): {local_result}")

# Main execution
print("=== Local and Global Variables Demo ===\n")

print("1. Initial global counter:", counter)
print()

print("2. Calling increment_counter() three times:")
increment_counter()
increment_counter()
increment_counter()
print()

print("3. Reading global message:")
show_message()
print()

print("4. Using local variable:")
use_local_variable()
# print(local_var)  # This would cause an error - local_var doesn't exist here
print()

print("5. Mixing local and global:")
mix_local_and_global()
print()

print("6. Final global counter:", counter)
