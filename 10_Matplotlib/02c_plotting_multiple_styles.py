# -------------------------------------------------
# File Name: 02c_plotting_multiple_styles.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Multiple lines with format strings (r-o, g--s, b:^). Includes format string reference.
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Multiple lines with different styles
# =========================================================================

x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]     # quadratic
y2 = [0, 1, 2, 3, 4, 5]       # linear
y3 = [25, 16, 9, 4, 1, 0]     # reverse quadratic

plt.figure(figsize=(7, 5))
plt.plot(x, y1, "r-o", label="Quadratic")    # red, solid, circles
plt.plot(x, y2, "g--s", label="Linear")      # green, dashed, squares
plt.plot(x, y3, "b:^", label="Reverse")      # blue, dotted, triangles
plt.title("Multiple Lines with Format Strings")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

# =========================================================================
# Format string shortcuts: 'color marker line'
# =========================================================================
# Colors:  r=red, g=green, b=blue, c=cyan, m=magenta, y=yellow, k=black
# Markers: o=circle, s=square, ^=triangle, D=diamond, *=star, +=plus
# Lines:   - =solid, --=dashed, -.=dash-dot, : =dotted

print("Format string examples:")
print("  'ro'   -> red circles (no line)")
print("  'g--'  -> green dashed line")
print("  'b-o'  -> blue solid line with circles")
print("  'k:s'  -> black dotted line with squares")
