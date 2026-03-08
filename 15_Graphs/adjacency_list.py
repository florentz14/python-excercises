# -------------------------------------------------
# File Name: adjacency_list.py
# Author: Florentino Báez
# Date: 15_Graphs
# Description: Re-export GrafoListaAdyacencia from 05_adjacency_list. Python cannot import modules whose names start with a number (e.g. 05_adjacency_list).
# -------------------------------------------------

import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "adjacency_list",
    Path(__file__).resolve().parent / "05_adjacency_list.py",
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

GrafoListaAdyacencia = _mod.GrafoListaAdyacencia
