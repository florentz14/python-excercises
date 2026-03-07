# ------------------------------------------------------------
# File: 29_numpy_install_import.py
# Purpose: Install and import NumPy.
# Description: pip install numpy, import as np, check version.
# ------------------------------------------------------------

# In terminal (once):
#   pip install numpy

import numpy as np

# Optional: verify version
print("NumPy installed. Version:", np.__version__)

# Use "np" for NumPy operations:
#   np.array(...)   → create arrays
#   np.dot(...)     → dot product / matrix multiply
#   np.zeros(...)   → zero matrix
#   etc.
