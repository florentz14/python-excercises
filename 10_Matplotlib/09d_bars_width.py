# -------------------------------------------------
# File Name: 09d_bars_width.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Bar width comparison (thin vs wide, 2 subplots).
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Bar width customization
# =========================================================================

categories = ["Python", "JavaScript", "Java", "C++", "Go"]
values = [92, 78, 65, 55, 48]

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.bar(categories, values, width=0.3, color="steelblue")
plt.title("Thin bars (width=0.3)")

plt.subplot(1, 2, 2)
plt.bar(categories, values, width=0.9, color="coral")
plt.title("Wide bars (width=0.9)")

plt.tight_layout()
plt.show()
