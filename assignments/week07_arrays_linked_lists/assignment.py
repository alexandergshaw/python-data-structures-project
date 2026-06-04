from __future__ import annotations

"""Week 07 assignment starter for Arrays and Linked Lists."""

from dataclasses import dataclass
from typing import Any

WEEK_NUMBER = 7
TOPIC = 'Arrays and Linked Lists'
FEATURE_NAME = 'Data Structures Showcase'

LEARNING_OBJECTIVES = [
    "Implement a dynamic array wrapper.",
    "Build linked list nodes and traversal helpers.",
    "Compare sequential data structures.",
]


class DynamicArray:
    """Minimal dynamic array implementation backed by a list."""

    def __init__(self) -> None:
        self.items: list[Any] = []

    def append(self, value: Any) -> None:
        self.items.append(value)

    def __len__(self) -> int:
        return len(self.items)


@dataclass
class Node:
    value: Any
    next: Node | None = None


class LinkedList:
    """Singly linked list with append and to_list helpers."""

    def __init__(self) -> None:
        self.head: Node | None = None

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def to_list(self) -> list[Any]:
        values: list[Any] = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values


def is_complete() -> bool:
    """Return completion status for this week's assignment starter."""
    return False


def get_unlocked_feature() -> str:
    """Return the dashboard feature unlocked by this week."""
    return FEATURE_NAME


def get_week_summary() -> dict[str, object]:
    """Return a dashboard-friendly summary for this week."""
    return {
        'week': WEEK_NUMBER,
        'topic': TOPIC,
        'feature': FEATURE_NAME,
        'objectives': LEARNING_OBJECTIVES,
        'complete': is_complete(),
    }

