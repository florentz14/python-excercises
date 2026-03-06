"""Match-case: Movement command.
Maps cardinal direction (n/s/e/w) to movement message.
"""
# Author: Florentino Báez


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
