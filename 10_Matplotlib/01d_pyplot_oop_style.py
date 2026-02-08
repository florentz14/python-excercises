# -------------------------------------------------
# File Name: 01d_pyplot_oop_style.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Object-oriented approach (fig, ax). Includes print summary block.
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Figure and Axes (Object-Oriented approach)
# =========================================================================

# Method 1: pyplot interface (simple, used above)
# plt.plot(), plt.title(), plt.show()

# Method 2: Object-oriented (more control)
fig, ax = plt.subplots(figsize=(6, 4))  # subplots() returns a Figure and Axes object for OOP control
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
ax.set_title("Object-Oriented Style")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
plt.show()

# --- Quick reference of the most common pyplot functions ---
print("\n--- Summary ---")
print("import matplotlib.pyplot as plt  -> Import the module")
print("plt.plot(x, y)                   -> Create a line plot")
print("plt.title('Title')               -> Set the title")
print("plt.xlabel('X') / plt.ylabel('Y')-> Set axis labels")
print("plt.legend()                     -> Show legend")
print("plt.show()                       -> Display the plot")
print("plt.savefig('file.png')          -> Save to file")
