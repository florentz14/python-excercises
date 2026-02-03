#!/usr/bin/env python3
"""Match-case example: Region by State (Python 3.10+)

Demonstrates pattern matching with alternation (|) operator.
Takes state abbreviation input and returns the corresponding region.
"""


def get_region(abbr: str) -> str:
    match abbr:
        case "CA" | "OR" | "WA":
            return "West"
        case "TX" | "OK" | "LA":
            return "South"
        case "NY" | "MA" | "PA":
            return "Northeast"
        case _:
            return "Other"


if __name__ == "__main__":
    abbr = input("Enter state abbreviation (e.g., TX, CA, NY): ").upper()
    print(get_region(abbr))
