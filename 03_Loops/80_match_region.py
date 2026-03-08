# -------------------------------------------------
# File Name: 80_match_region.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Region by state abbreviation.
# -------------------------------------------------

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
