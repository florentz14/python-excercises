# -------------------------------------------------
# File Name: 56_subjects_grades_uppercase.py
# Description: Dict subjects->notes to uppercase keys and letter grades
# -------------------------------------------------

def note_to_grade(note: float) -> str:
    if note < 5:
        return "Fail"
    if note < 6:
        return "Pass"
    if note < 7:
        return "Good"
    if note < 9:
        return "Very Good"
    return "Excellent"


def subjects_to_grades(subjects: dict[str, float]) -> dict[str, str]:
    """Return dict with uppercase subject keys and letter grades."""
    return {k.upper(): note_to_grade(v) for k, v in subjects.items()}


if __name__ == "__main__":
    d = {"math": 7.5, "english": 4.2, "physics": 8.0}
    print(subjects_to_grades(d))
