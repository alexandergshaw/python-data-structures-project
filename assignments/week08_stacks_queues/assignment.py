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

        Hint:
            self.items = []
        """
        self.items = None  # TODO: replace None — initialize as an empty list []

    def push(self, value: Any) -> None:
        """Add value to the top (end) of the stack.

        Examples:
            Pushing to an empty stack adds the first item:
                >>> s = Stack()
                >>> s.push('a')
                >>> s.items
                ['a']

            Each subsequent push adds to the end (top) of the stack:
                >>> s = Stack()
                >>> s.push('a')
                >>> s.push('b')
                >>> s.items
                ['a', 'b']

            Any type of value can be pushed:
                >>> s = Stack()
                >>> s.push(42)
                >>> s.items
                [42]

        Hint:
            self.items.append(value)
        """
        pass  # TODO: append value to self.items

    def pop(self) -> Any:
        """Remove and return the top (last) item.

        Examples:
            A single item is removed and returned, leaving the stack empty:
                >>> s = Stack()
                >>> s.push('a')
                >>> s.pop()
                'a'

            The most recently pushed item (LIFO order) is always returned first:
                >>> s = Stack()
                >>> s.push('a')
                >>> s.push('b')
                >>> s.pop()
                'b'

            After a pop, the remaining items are still in the stack:
                >>> s = Stack()
                >>> s.push(1)
                >>> s.push(2)
                >>> s.pop()
                2
                >>> s.items
                [1]

        Hint:
            return self.items.pop()
        """
        return None  # TODO: replace None — use self.items.pop() to remove and return the last item


class Queue:
    """First-In, First-Out (FIFO) data structure backed by a deque."""

    def __init__(self) -> None:
        """Initialize self.items as an empty deque.

        Hint:
            self.items = deque()
        """
        self.items = None  # TODO: replace None — initialize as deque()

    def enqueue(self, value: Any) -> None:
        """Add value to the back (right) of the queue.

        Examples:
            Enqueueing the first item makes it both front and back:
                >>> q = Queue()
                >>> q.enqueue('x')

            Multiple enqueues add items in order from front to back:
                >>> q = Queue()
                >>> q.enqueue('first')
                >>> q.enqueue('second')
                >>> q.dequeue()
                'first'

            Any type of value can be enqueued:
                >>> q = Queue()
                >>> q.enqueue(99)

        Hint:
            self.items.append(value)
        """
        pass  # TODO: use self.items.append(value) to add to the right side

    def dequeue(self) -> Any:
        """Remove and return the item at the front (left) of the queue.

        Examples:
            A single enqueued item is dequeued immediately:
                >>> q = Queue()
                >>> q.enqueue('x')
                >>> q.dequeue()
                'x'

            The first item enqueued is the first item dequeued (FIFO order):
                >>> q = Queue()
                >>> q.enqueue('first')
                >>> q.enqueue('second')
                >>> q.dequeue()
                'first'

            After dequeuing, the remaining items are still in the queue:
                >>> q = Queue()
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.dequeue()
                1
                >>> q.dequeue()
                2

        Hint:
            return self.items.popleft()
        """
        return None  # TODO: replace None — use self.items.popleft() to remove and return the front item


class DataPipeline:
    """An ordered list of named processing steps."""

    def __init__(self) -> None:
        """Initialize self.steps as an empty list.

        Hint:
            self.steps = []
        """
        self.steps = None  # TODO: replace None — initialize as an empty list []

    def add_step(self, step: str) -> None:
        """Append step name to self.steps.

        Examples:
            Adding a single step creates a one-item list:
                >>> p = DataPipeline()
                >>> p.add_step('extract')
                >>> p.steps
                ['extract']

            Each subsequent step is appended in order:
                >>> p = DataPipeline()
                >>> p.add_step('extract')
                >>> p.add_step('transform')
                >>> p.add_step('load')
                >>> p.steps
                ['extract', 'transform', 'load']

        Hint:
            self.steps.append(step)
        """
        pass  # TODO: append step to self.steps

    def run(self) -> list[str]:
        """Return a copy of self.steps.

        Examples:
            Run returns all steps in the order they were added:
                >>> p = DataPipeline()
                >>> p.add_step('extract')
                >>> p.run()
                ['extract']

            A full ETL pipeline returns all three steps:
                >>> p = DataPipeline()
                >>> p.add_step('extract')
                >>> p.add_step('transform')
                >>> p.add_step('load')
                >>> p.run()
                ['extract', 'transform', 'load']

            Modifying the returned list does not change the pipeline's internal steps:
                >>> p = DataPipeline()
                >>> p.add_step('extract')
                >>> result = p.run()
                >>> result.append('bonus')
                >>> p.steps
                ['extract']

        Hint:
            return self.steps[:]
        """
        return None  # TODO: replace None — return a copy of self.steps using self.steps[:]


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


