"""
Helper module: re-exports ArbolBST from 06_bst.
Python cannot import modules whose names start with a number.
"""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "bst",
    Path(__file__).resolve().parent / "06_bst.py",
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

ArbolBST = _mod.ArbolBST
