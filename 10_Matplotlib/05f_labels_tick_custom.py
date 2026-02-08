# -------------------------------------------------
# File Name: 05f_labels_tick_custom.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Custom tick labels (month names, rotation).
# -------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 5, 4, 6, 8]

# =========================================================================
# Tick labels customization
# =========================================================================

plt.figure(figsize=(7, 5))
plt.plot(x, y, "b-o")

# Custom tick labels
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
plt.xticks(x, months, fontsize=11, rotation=45)  # xticks() replaces numeric tick positions with custom labels
plt.yticks(fontsize=11)

plt.title("Custom Tick Labels")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
