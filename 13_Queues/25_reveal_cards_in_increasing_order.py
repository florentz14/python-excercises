# -------------------------------------------------
# File Name: 25_reveal_cards_in_increasing_order.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Reveal cards in increasing order with queue indices.
# -------------------------------------------------

from collections import deque

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def deck_revealed_increasing(deck: list[int]) -> list[int]:
    """Return deck order so revealed sequence is increasing."""
    n = len(deck)
    indices = deque(range(n))
    answer = [0] * n

    for card in sorted(deck):
        answer[indices.popleft()] = card
        if indices:
            indices.append(indices.popleft())

    return answer


def simulate_reveal(order: list[int]) -> list[int]:
    """Simulate reveal process to verify increasing result."""
    q = deque(order)
    revealed = []
    while q:
        revealed.append(q.popleft())
        if q:
            q.append(q.popleft())
    return revealed


def demo() -> None:
    title("REVEAL CARDS IN INCREASING ORDER")
    deck = [17, 13, 11, 2, 3, 5, 7]
    order = deck_revealed_increasing(deck)
    revealed = simulate_reveal(order)
    print(f"  Original deck values: {deck}")
    print(f"  Required initial order: {order}")
    print(f"  Revealed sequence: {revealed}")


if __name__ == "__main__":
    demo()
