#!/usr/bin/env python3
"""Match-case example: Movement Command (Python 3.10+)

Demonstrates simple pattern matching for directional commands.
Takes cardinal direction input (n/s/e/w) and returns the movement message.
"""


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
