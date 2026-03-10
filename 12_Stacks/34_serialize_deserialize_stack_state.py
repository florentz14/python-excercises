# -------------------------------------------------
# File Name: 34_serialize_deserialize_stack_state.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Serialize and deserialize stack state snapshots.
# -------------------------------------------------

"""
============================================================
  SERIALIZE / DESERIALIZE STACK STATE - Python 3.14
  Save and restore stack snapshots to support persistence,
  checkpoints, and replay.

  This file demonstrates:
    - stack snapshot export
    - JSON serialization
    - deserialization to stack object
    - replay of operations from snapshots
============================================================
"""

import json

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


class SerializableStack:
    """Simple stack that supports serialization."""

    def __init__(self, initial: list[int] | None = None) -> None:
        self._data = list(initial) if initial else []

    def push(self, value: int) -> None:
        self._data.append(value)

    def pop(self) -> int:
        if not self._data:
            raise IndexError("Pop from empty stack.")
        return self._data.pop()

    def top(self) -> int:
        if not self._data:
            raise IndexError("Top from empty stack.")
        return self._data[-1]

    def is_empty(self) -> bool:
        return not self._data

    def size(self) -> int:
        return len(self._data)

    def to_list(self) -> list[int]:
        return self._data[:]

    def serialize(self) -> str:
        """Export state as JSON string."""
        payload = {
            "type": "SerializableStack",
            "version": 1,
            "size": self.size(),
            "items_base_to_top": self.to_list(),
        }
        return json.dumps(payload, separators=(",", ":"))

    @classmethod
    def deserialize(cls, data: str) -> "SerializableStack":
        """Restore stack from JSON string."""
        payload = json.loads(data)
        if payload.get("type") != "SerializableStack":
            raise ValueError("Unsupported serialized type.")
        items = payload.get("items_base_to_top", [])
        return cls(items)

    def __repr__(self) -> str:
        return f"SerializableStack({self._data})"


def demo() -> None:
    title("SERIALIZE / DESERIALIZE STACK STATE")

    stack = SerializableStack()
    print("  Building stack with pushes: 10, 20, 30")
    for x in [10, 20, 30]:
        stack.push(x)
    print(f"  Current stack (base->top): {stack.to_list()}")

    snapshot_1 = stack.serialize()
    print(f"\n  Snapshot 1 (JSON): {snapshot_1}")

    print("\n  Mutate stack: pop(), push(99)")
    stack.pop()
    stack.push(99)
    print(f"  Current stack (base->top): {stack.to_list()}")

    snapshot_2 = stack.serialize()
    print(f"\n  Snapshot 2 (JSON): {snapshot_2}")

    print("\n  Restore from snapshot 1")
    restored_1 = SerializableStack.deserialize(snapshot_1)
    print(f"  Restored stack 1: {restored_1.to_list()}")

    print("\n  Restore from snapshot 2")
    restored_2 = SerializableStack.deserialize(snapshot_2)
    print(f"  Restored stack 2: {restored_2.to_list()}")

    print("\n  Replay check:")
    print(f"  top(snapshot1) = {restored_1.top()}")
    print(f"  top(snapshot2) = {restored_2.top()}")


if __name__ == "__main__":
    demo()
