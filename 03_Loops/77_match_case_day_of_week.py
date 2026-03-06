"""Match-case example: Day of Week (Python 3.10+)

Demonstrates a simple match/case switch-like structure.
"""

def day_of_week(day: int) -> str:
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Unknown"


if __name__ == "__main__":
    # Example usage
    day = 6
    print(day_of_week(day))
