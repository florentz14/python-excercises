# -------------------------------------------------
# File Name: 57_subjects_passed_only.py
# Description: Dict subjects->notes to uppercase keys, only passed grades
# -------------------------------------------------


def note_to_grade(note: float) -> str:
    if note < 5:
        return None
    if note < 6:
        return "Pass"
    if note < 7:
        return "Good"
    if note < 9:
        return "Very Good"
    return "Excellent"


def passed_subjects_grades(subjects: dict[str, float]) -> dict[str, str]:
    """Return dict with uppercase keys and grades, only for passed subjects."""
    return {
        k.upper(): note_to_grade(v)
        for k, v in subjects.items()
        if note_to_grade(v) is not None
    }


if __name__ == "__main__":
    d = {"math": 7.5, "english": 4.2, "physics": 8.0}
    print(passed_subjects_grades(d))
