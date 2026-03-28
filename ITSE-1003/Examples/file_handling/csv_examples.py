# -------------------------------------------------
# File Name: ITSE-1003/Examples/file_handling/csv_examples.py
# Author: Florentino
# Date: 3/21/26
# Description: Alias — ejecuta run_csv_workshop (nombre antiguo conservado por compatibilidad).
# -------------------------------------------------

import sys
from pathlib import Path

_EXAMPLES_ROOT = Path(__file__).resolve().parent.parent
_FILE_HANDLING_ROOT = Path(__file__).resolve().parent
for _p in (_EXAMPLES_ROOT, _FILE_HANDLING_ROOT):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from run_csv_workshop import main

if __name__ == "__main__":
    main()
