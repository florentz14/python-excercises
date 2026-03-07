# -------------------------------------------------
# File: 13_len_method.py
# Description: __len__ magic method.
#              Making objects work with len() function.
# -------------------------------------------------

from typing import Any


class ShoppingCart:
    """Shopping cart with __len__ method."""

    def __init__(self):
        self.items = []

    def add_item(self, item: Any, quantity: int = 1) -> None:
        """Add item to cart."""
        self.items.append((item, quantity))
        print(f"Added {quantity} x {item}")

    def __len__(self):
        """Return total number of items in cart."""
        return sum(quantity for _, quantity in self.items)

    def get_total_items(self) -> int:
        """Regular method to get total items."""
        return len(self)  # Uses our __len__ method


class Sentence:
    """Sentence class with __len__ for word count."""

    def __init__(self, text: str) -> None:
        self.text = text

    def __len__(self) -> int:
        """Return number of words in sentence."""
        return len(self.text.split())

    def get_word_count(self):
        """Regular method for word count."""
        return len(self)


class Playlist:
    """Music playlist with __len__ for song count."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.songs = []

    def add_song(self, title: str, artist: str, duration: float) -> None:
        """Add song to playlist."""
        self.songs.append({
            'title': title,
            'artist': artist,
            'duration': duration
        })

    def __len__(self):
        """Return number of songs in playlist."""
        return len(self.songs)

    def total_duration(self):
        """Calculate total duration of all songs."""
        return sum(song['duration'] for song in self.songs)


class CustomList:
    """Custom list implementation with __len__."""

    def __init__(self):
        self._data = []

    def append(self, item):
        """Add item to list."""
        self._data.append(item)

    def __len__(self):
        """Return length of custom list."""
        return len(self._data)

    def __getitem__(self, index):
        """Enable indexing."""
        return self._data[index]

    def __repr__(self):
        """String representation."""
        return f"CustomList({self._data})"


# Demonstration
if __name__ == "__main__":
    print("=== __len__ Magic Method Demo ===\n")

    # Shopping cart example
    cart = ShoppingCart()
    cart.add_item("Apple", 3)
    cart.add_item("Banana", 2)
    cart.add_item("Orange", 5)

    print(f"Cart has {len(cart)} items total")
    print(f"Total items (via method): {cart.get_total_items()}")

    # Empty cart
    empty_cart = ShoppingCart()
    print(f"Empty cart has {len(empty_cart)} items")

    print("\n=== Sentence Word Count ===")

    sentences = [
        Sentence("Hello world"),
        Sentence("This is a longer sentence with more words"),
        Sentence("")
    ]

    for sentence in sentences:
        word_count = len(sentence)
        print(f"'{sentence.text}' -> {word_count} words")

    print("\n=== Playlist Song Count ===")

    playlist = Playlist("My Favorites")
    playlist.add_song("Bohemian Rhapsody", "Queen", 355)
    playlist.add_song("Stairway to Heaven", "Led Zeppelin", 482)
    playlist.add_song("Hotel California", "Eagles", 391)

    print(f"Playlist '{playlist.name}' has {len(playlist)} songs")
    print(f"Total duration: {playlist.total_duration()} seconds")

    print("\n=== Custom List ===")

    my_list = CustomList()
    my_list.append("first")
    my_list.append("second")
    my_list.append("third")

    print(f"Custom list: {my_list}")
    print(f"Length: {len(my_list)}")
    print(f"First item: {my_list[0]}")

    print("\n=== Built-in Functions that Use __len__ ===")
    print("- len(obj)")
    print("- bool(obj) - empty sequences are falsy")
    print("- list comprehensions and generators")

    # Bool conversion
    print(f"bool(empty_cart): {bool(empty_cart)}")
    print(f"bool(cart): {bool(cart)}")

    print("\n=== When to Implement __len__ ===")
    print("- When your object represents a collection")
    print("- When length is a meaningful concept for your class")
    print("- To make your objects work with len(), bool(), etc.")
    print("- For consistency with Python's data model")