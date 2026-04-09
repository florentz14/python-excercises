# -------------------------------------------------
# File Name: 98b_array_membership_index.py
# Author: Florentino Baez
# Date: 08_Matrices
# Description: `in`, index(), and count() on lists.
# -------------------------------------------------

SEPARATOR = "=" * 60
BASE_ARRAY = [15, 42, 8, 73, 31, 56, 4, 99, 27, 61]


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


def main() -> None:
    data = BASE_ARRAY
    title("6b-6c. MEMBERSHIP, index(), count()")
    print(f"  Array : {data}")

    subtitle("6b. Search with 'in' (membership)")
    for value in [42, 100]:
        print(f"  Is {value} in the array? -> {value in data}")

    subtitle("6c. Search with index() and count()")
    print(f"  Index of 56           : {data.index(56)}")
    duplicated = data + [42, 42]
    print(f"  Count of 42 in {duplicated}: {duplicated.count(42)}")


if __name__ == "__main__":
    main()
