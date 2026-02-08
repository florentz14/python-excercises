# -------------------------------------------------
# File Name: 03f_markers_every_nth.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: markevery parameter (show every 10th point).
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np  # numpy is needed for np.linspace to generate evenly spaced points

# =========================================================================
# Every Nth marker (markevery)
# =========================================================================

x_dense = np.linspace(0, 10, 100)
y_dense = np.sin(x_dense)

plt.figure(figsize=(6, 4))
plt.plot(x_dense, y_dense, "b-o", markersize=6, markevery=10,  # markevery=N shows a marker on every Nth data point only
         label="markevery=10")
plt.title("Show Marker Every 10th Point")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
