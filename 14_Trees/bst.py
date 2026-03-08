# -------------------------------------------------
# File Name: bst.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: Re-exports ArbolBST from 06_bst.
# -------------------------------------------------

import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "bst",
    Path(__file__).resolve().parent / "06_bst.py",
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

ArbolBST = _mod.ArbolBST
