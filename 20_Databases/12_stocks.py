"""Backward-compatible launcher for data_ops_app (stocks)."""

from data_ops_app.app.main import run


if __name__ == "__main__":
    import sys

    sys.argv = [sys.argv[0], "stocks"]
    run()
