# -------------------------------------------------
# File Name: ITSE-1003/Examples/file_handling/file_context_manager.py
# Author: Florentino
# Date: 3/20/2026
# Description: Context manager in a class.
# -------------------------------------------------

from pathlib import Path


class FileWriter:
    def __init__(self, path: str) -> None:
        self.path = path
        self.file = None

    def __enter__(self) -> "FileWriter":
        self.file = open(self.path, "w", encoding="utf-8")
        return self

    def write_line(self, text: str) -> None:
        if self.file is None:
            raise RuntimeError("File is not open.")
        self.file.write(text + "\n")

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.file is not None:
            self.file.close()


def main() -> None:
    note_path = Path(__file__).resolve().parent.parent / "temp_note.txt"
    with FileWriter(str(note_path)) as writer:
        writer.write_line("This file was created with a context manager class.")
        writer.write_line("It closes automatically.")
    print("File written successfully.")


if __name__ == "__main__":
    main()
