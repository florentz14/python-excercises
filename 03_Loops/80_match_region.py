"""Match-case: Region by state abbreviation.
Uses alternation (|) to match multiple state codes per region.
"""
# Author: Florentino Báez


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
