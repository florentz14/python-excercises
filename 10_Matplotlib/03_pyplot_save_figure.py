# -------------------------------------------------
# File Name: 01c_pyplot_save_figure.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Saving a figure to file demo.
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Saving a figure to a file
# =========================================================================

plt.figure(figsize=(6, 4))
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.title("Saved Figure")
# plt.savefig("my_plot.png", dpi=150, bbox_inches="tight")
# Supported formats: png, jpg, svg, pdf
print("To save: plt.savefig('filename.png', dpi=150)")

plt.show()
