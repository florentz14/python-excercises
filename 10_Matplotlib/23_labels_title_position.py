# -------------------------------------------------
# File Name: 05c_labels_title_position.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Title alignment: left, center, right (3 subplots).
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 5, 4, 6, 8]

# =========================================================================
# Title position (loc parameter)
# =========================================================================

fig, axes = plt.subplots(1, 3, figsize=(12, 4))  # Three subplots to compare title alignment positions

axes[0].plot(x, y)
axes[0].set_title("Left Title", loc="left")  # loc="left" aligns the title to the left edge of the axes

axes[1].plot(x, y)
axes[1].set_title("Center Title (default)", loc="center")

axes[2].plot(x, y)
axes[2].set_title("Right Title", loc="right")

plt.tight_layout()
plt.show()
