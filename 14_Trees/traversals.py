# -------------------------------------------------
# File Name: traversals.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: Re-exports ArbolRecorridos from 05_traversals.
# -------------------------------------------------

import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "traversals",
    Path(__file__).resolve().parent / "05_traversals.py",
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

ArbolRecorridos = _mod.ArbolRecorridos
