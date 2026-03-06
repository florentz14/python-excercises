# ------------------------------------------------------------
# File: 15_tuples_chapter_tutorial.py
# Chapter: 11 - Tuples
#
# Purpose:
#   Tutorial covering tuple basics: creation, indexing,
#   immutability, conversion, unpacking, and list-of-tuples.
#
# Sections:
#   1. Basic concepts
#   2. Indexing and slicing
#   3. Immutability and conversion (tuple <-> list)
#   4. Packing and unpacking
#   5. List of tuples (iterating, dict.items())
#
# Author: Florentino Baez (adapted)
# ------------------------------------------------------------


# =============================================================================
# Section 1: Tuples - Basic Concepts
# Tuples are ordered, immutable sequences. Elements cannot be modified.
# =============================================================================

def section1_basics():
    """Create a tuple, show length, and iterate."""
    my_tuple = ("Bad Bunny", "Anuel", "Daddy Yankee", "Wisin")
    print("Tuple value:", my_tuple)
    print(f"Length: {len(my_tuple)}")
    print("Iterate over tuple:")
    # Use enumerate instead of index() to avoid O(n) lookup per iteration
    for i, artist in enumerate(my_tuple):
        print(f"  Artist {i}: {artist}")


# =============================================================================
# Section 2: Tuple Indexing
# Index like lists: positive (0-based), negative (-1 = last), slicing.
# =============================================================================

def section2_indexing():
    """Access elements by index and slice."""
    my_tuple = ("Bad Bunny", "Anuel", "Daddy Yankee", "Wisin")
    print("Tuple:", my_tuple)

    first = my_tuple[0]
    print(f"First element: {first}")

    last = my_tuple[-1]
    print(f"Last element: {last}")

    subtuple = my_tuple[1:3]
    print(f"Subtuple [1:3]: {subtuple}")


# =============================================================================
# Section 3: Modifying Tuples
# Tuples are immutable. To "modify", convert to list, change, then back.
# =============================================================================

def section3_immutability():
    """Demonstrate immutability and tuple <-> list conversion."""
    my_tuple = ("Bad Bunny", "Anuel", "Daddy Yankee", "Wisin")
    print("Tuple:", my_tuple)

    # These operations raise TypeError
    print("\nAttempting invalid operations:")
    try:
        del my_tuple[2]
    except Exception as e:
        print(f"  del tuple[i]: {type(e).__name__}")

    try:
        my_tuple.append("Yandel")
    except Exception as e:
        print(f"  tuple.append(): {type(e).__name__}")

    try:
        my_tuple[3] = "Yandel"
    except Exception as e:
        print(f"  tuple[i] = x: {type(e).__name__}")

    # Workaround: convert to list, modify, convert back
    print("\nConvert tuple -> list:")
    my_list = list(my_tuple)
    print(my_list)
    print("Add element to list:")
    my_list.append("Yandel")
    print(my_list)
    print("Convert list -> tuple:")
    my_tuple = tuple(my_list)
    print(my_tuple)

    print("Concatenate tuples:")
    tuple2 = ("Don Omar", "Tego Calderon", "Kendo Kapone")
    tuple3 = my_tuple + tuple2
    print(tuple3)


# =============================================================================
# Section 4: Packing and Unpacking
# Pack: group values into a tuple. Unpack: assign to separate variables.
# Use * to capture multiple elements.
# =============================================================================

def section4_unpacking():
    """Demonstrate packing and unpacking with * operator."""
    my_tuple = ("Bad Bunny", "Anuel", "Daddy Yankee")
    print("Tuple:", my_tuple)
    print("Unpack into variables:")
    artist1, artist2, artist3 = my_tuple
    print(f"  Artist 1: {artist1}, Artist 2: {artist2}, Artist 3: {artist3}")

    my_tuple = ("Bad Bunny", "Anuel", "Daddy Yankee", "Myke Towers", "Farruko", "C.Tangana")
    print("\nTuple:", my_tuple)
    print("Unpack with * (first two, rest in list):")
    first, second, *rest = my_tuple
    print(f"  First: {first}, Second: {second}")
    print(f"  Rest: {rest}")

    print("Unpack with * in middle (first, rest, last):")
    first, *rest, last = my_tuple
    print(f"  First: {first}, Last: {last}")
    print(f"  Rest: {rest}")


# =============================================================================
# Section 5: List of Tuples
# Tuples as list elements; iterate and unpack. Same pattern as dict.items().
# =============================================================================

def section5_list_of_tuples():
    """List of tuples and relation to dict.items()."""
    menu = [("starter", "macaroni"), ("main", "chicken"), ("dessert", "flan")]
    print("Today's menu:")
    for course, name in menu:
        print(f"  {course} -> {name}")

    print("\nThis is the same pattern as dict.items():")
    artists = {1: "C.Tangana", 2: "Duki", 3: "Khea"}
    print("Dictionary:", artists)
    items = artists.items()  # Returns view of (key, value) pairs
    print("items():", list(items))
    for key, value in artists.items():
        print(f"  {key}: {value}")


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("1. Tuples - Basic Concepts")
    print("=" * 55)
    section1_basics()

    print("\n" + "=" * 55)
    print("2. Tuple Indexing")
    print("=" * 55)
    section2_indexing()

    print("\n" + "=" * 55)
    print("3. Modifying Tuples (Immutability)")
    print("=" * 55)
    section3_immutability()

    print("\n" + "=" * 55)
    print("4. Packing and Unpacking")
    print("=" * 55)
    section4_unpacking()

    print("\n" + "=" * 55)
    print("5. List of Tuples")
    print("=" * 55)
    section5_list_of_tuples()
