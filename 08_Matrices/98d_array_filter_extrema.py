# -------------------------------------------------
# File Name: 98d_array_filter_extrema.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: filter/comprehension and min/max with index.
# -------------------------------------------------

SEPARATOR = "=" * 60
BASE_ARRAY = [15, 42, 8, 73, 31, 56, 4, 99, 27, 61]


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


def main() -> None:
    data = BASE_ARRAY
    title("6e-6f. FILTER, COMPREHENSION, MIN/MAX")

    subtitle("6e. Search with filter() and comprehension")
    greater_than_50 = list(filter(lambda x: x > 50, data))
    print(f"  Elements > 50 (filter)      : {greater_than_50}")
    even_values = [x for x in data if x % 2 == 0]
    print(f"  Even elements (comprehension): {even_values}")

    subtitle("6f. Find minimum and maximum with index")
    print(f"  Minimum: {min(data)} at index {data.index(min(data))}")
    print(f"  Maximum: {max(data)} at index {data.index(max(data))}")


if __name__ == "__main__":
    main()
