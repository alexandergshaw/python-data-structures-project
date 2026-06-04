"""Week 08 assignment starter for Stacks and Queues."""

WEEK_NUMBER = 8
TOPIC = 'Stacks and Queues'
FEATURE_NAME = 'Data Pipeline Monitor'

from collections import deque
from typing import Any

LEARNING_OBJECTIVES = [
    "Implement stack behavior.",
    "Implement queue behavior.",
    "Model a simple data pipeline.",
]


class Stack:
    """Last-In, First-Out (LIFO) data structure."""

    def __init__(self) -> None:
        """Initialize self.items as an empty list.

        """
        self.items = None  # TODO

    def push(self, value: Any) -> None:
        """Add value to the top (end) of the stack.

        Example:
            >>> s = Stack()
            >>> s.push('a')
            >>> s.items
            ['a']

        """
        pass  # TODO

    def pop(self) -> Any:
        """Remove and return the top (last) item.

        Example:
            >>> s = Stack()
            >>> s.push('a')
            >>> s.pop()
            'a'

        """
        return None  # TODO


class Queue:
    """First-In, First-Out (FIFO) data structure backed by a deque."""

    def __init__(self) -> None:
        """Initialize self.items as an empty deque.

        """
        self.items = None  # TODO

    def enqueue(self, value: Any) -> None:
        """Add value to the back (right) of the queue.

        Example:
            >>> q = Queue()
            >>> q.enqueue('x')

        """
        pass  # TODO

    def dequeue(self) -> Any:
        """Remove and return the item at the front (left) of the queue.

        Example:
            >>> q = Queue()
            >>> q.enqueue('x')
            >>> q.dequeue()
            'x'

        """
        return None  # TODO


class DataPipeline:
    """An ordered list of named processing steps."""

    def __init__(self) -> None:
        """Initialize self.steps as an empty list.

        """
        self.steps = None  # TODO

    def add_step(self, step: str) -> None:
        """Append step name to self.steps.

        Example:
            >>> p = DataPipeline()
            >>> p.add_step('extract')
            >>> p.steps
            ['extract']

        """
        pass  # TODO

    def run(self) -> list[str]:
        """Return a copy of self.steps.

        Example:
            >>> p = DataPipeline()
            >>> p.add_step('extract')
            >>> p.run()
            ['extract']

        """
        return None  # TODO


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


