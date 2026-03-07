# ------------------------------------------------------------
# File: 34_numpy_summary.py
# Purpose: Summary: Python lists vs NumPy equivalence.
# Description: Quick reference for vector/matrix operations.
# ------------------------------------------------------------

import numpy as np

# ---------------------------------------------------------------------------
# VECTORS
# ---------------------------------------------------------------------------
# Python (lists)              |  NumPy (np.array)
# ----------------------------|------------------------------------------
# v = [1, 2, 3]               |  v = np.array([1, 2, 3])
# [v[i] + w[i] for i in ...] |  v + w
# [k * x for x in v]         |  k * v
# sum(v[i]*w[i] for i in ...)|  np.dot(v, w)  or  v @ w
# math.sqrt(sum(x*x for x in v)) |  np.linalg.norm(v)
# len(v)                      |  v.shape  (e.g. (3,))

# ---------------------------------------------------------------------------
# MATRICES
# ---------------------------------------------------------------------------
# Python (list of lists)      |  NumPy
# ----------------------------|------------------------------------------
# A = [[1,2],[3,4]]           |  A = np.array([[1,2],[3,4]])
# loops for A+B               |  A + B
# loops for k*A               |  k * A
# transpose with list comp    |  A.T
# loops for A*B               |  A @ B  or  np.dot(A, B)
# len(A), len(A[0])           |  A.shape  (e.g. (2, 2))

print("Summary: run files 29–33 for each step.")
print("NumPy benefits: concise syntax, fast (C), rich API (linalg, etc.).")
