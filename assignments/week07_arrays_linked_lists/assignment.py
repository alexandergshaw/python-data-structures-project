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
    """A minimal wrapper around a Python list (dynamic array)."""

    def __init__(self) -> None:
        """Initialize self.items as an empty list.

        Hint:
            self.items = []
        """
        self.items = None  # TODO: replace None — initialize as an empty list []

    def append(self, value: Any) -> None:
        """Add value to the end of self.items.

        Example:
            >>> arr = DynamicArray()
            >>> arr.append(10)
            >>> arr.items
            [10]

        Hint:
            self.items.append(value)
        """
        pass  # TODO: append value to self.items

    def __len__(self) -> int:
        """Return the number of items stored.

        Example:
            >>> arr = DynamicArray()
            >>> arr.append(5)
            >>> len(arr)
            1

        Hint:
            return len(self.items)
        """
        return None  # TODO: replace None — use len() on self.items


@dataclass
class Node:
    """A single node in a linked list. Already implemented — do not modify."""
    value: Any
    next: Node | None = None


class LinkedList:
    """A singly linked list."""

    def __init__(self) -> None:
        """Initialize an empty list with self.head = None.

        Hint:
            self.head = None
        """
        self.head = None  # this is correct — head starts as None (empty list)

    def append(self, value: Any) -> None:
        """Add a new node with value at the end of the list.

        Example:
            >>> ll = LinkedList()
            >>> ll.append(1)
            >>> ll.head.value
            1

        Hints:
            1. Create new_node = Node(value).
            2. If self.head is None, set self.head = new_node and return.
            3. Otherwise, walk from self.head until current.next is None.
            4. Set current.next = new_node.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        pass  # TODO: set current.next to new_node to attach it at the end

    def to_list(self) -> list[Any]:
        """Return all node values as a plain Python list, head to tail.

        Example:
            >>> ll = LinkedList()
            >>> ll.append(1)
            >>> ll.append(2)
            >>> ll.to_list()
            [1, 2]

        Hints:
            1. Start with values = [] and current = self.head.
            2. While current is not None:
                   values.append(current.value)
                   current = current.next
            3. Return values.
        """
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = None  # TODO: replace None — advance to the next node (current.next)
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

