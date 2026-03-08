# -------------------------------------------------
# File Name: 55_notes_to_grades.py
# Description: Convert list of numeric grades to letter grades
# -------------------------------------------------


def note_to_grade(note: float) -> str:
    """Convert 0-10 note to letter grade."""
    if note < 5:
        return "Fail"
    if note < 6:
        return "Pass"
    if note < 7:
        return "Good"
    if note < 9:
        return "Very Good"
    return "Excellent"


def notes_to_grades(notes: list[float]) -> list[str]:
    """Return list of grades for each note."""
    return [note_to_grade(n) for n in notes]


if __name__ == "__main__":
    print(notes_to_grades([3.5, 5.2, 6.8, 8.1, 9.5]))
