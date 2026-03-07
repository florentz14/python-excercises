"""
Helper module: re-exports ArbolBinario, NodoArbol from 04_basic_binary.
Python cannot import modules whose names start with a number.
"""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "basic_binary",
    Path(__file__).resolve().parent / "04_basic_binary.py",
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

ArbolBinario = _mod.ArbolBinario
NodoArbol = _mod.NodoArbol
