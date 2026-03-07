"""
Helper module: re-exports ArbolRecorridos from 05_traversals.
Python cannot import modules whose names start with a number.
"""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "traversals",
    Path(__file__).resolve().parent / "05_traversals.py",
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

ArbolRecorridos = _mod.ArbolRecorridos
