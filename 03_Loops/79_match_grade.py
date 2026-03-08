# -------------------------------------------------
# File Name: 79_match_grade.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Letter grade with guards.
# -------------------------------------------------

def letter_grade(score: int) -> str:
    match score:
        case s if s >= 90:
            return "A"
        case s if 80 <= s < 90:
            return "B"
        case s if 70 <= s < 80:
            return "C"
        case s if 60 <= s < 70:
            return "D"
        case _:
            return "F"


if __name__ == "__main__":
    score = 87
    print(letter_grade(score))
