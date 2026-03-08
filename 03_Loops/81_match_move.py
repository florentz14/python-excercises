# -------------------------------------------------
# File Name: 81_match_move.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Movement command.
# -------------------------------------------------

def move(cmd: str) -> str:
    match cmd:
        case "n":
            return "Moving north"
        case "s":
            return "Moving south"
        case "e":
            return "Moving east"
        case "w":
            return "Moving west"
        case _:
            return "Unknown command"


if __name__ == "__main__":
    cmd = input("Enter command (n/s/e/w): ").lower()
    print(move(cmd))
