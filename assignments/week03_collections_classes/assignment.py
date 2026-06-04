"""Week 03 assignment starter for Collections and Classes."""

WEEK_NUMBER = 3
TOPIC = 'Collections and Classes'
FEATURE_NAME = 'KPI Dashboard'

LEARNING_OBJECTIVES = [
    "Remove duplicates with a set and sort a list.",
    "Count word occurrences with a dictionary.",
    "Build a simple class with an __init__ and methods.",
]


def get_unique_items(items: list) -> list:
    """Return a sorted list of unique items from the input list.

    Example:
        >>> get_unique_items([3, 1, 2, 1, 3])
        [1, 2, 3]
        >>> get_unique_items(["b", "a", "b"])
        ['a', 'b']
        >>> get_unique_items([1, 2, 3])
        [1, 2, 3]

    """
    return None  # TODO


def word_frequency(words: list[str]) -> dict[str, int]:
    """Return a dict mapping each word to how many times it appears.

    Example:
        >>> word_frequency(["hi", "bye", "hi"])
        {'hi': 2, 'bye': 1}
        >>> word_frequency([])
        {}

    """
    freq = {}
    for word in words:
        pass  # TODO
    return freq


class Counter:
    """A simple integer counter that can be incremented, decremented, and reset."""

    def __init__(self, start: int = 0) -> None:
        """Store the starting value in self.count.

        Example:
            >>> c = Counter()
            >>> c.count
            0
            >>> c = Counter(10)
            >>> c.count
            10

        """
        self.count = None  # TODO

    def increment(self) -> None:
        """Add 1 to self.count.

        Example:
            >>> c = Counter()
            >>> c.increment()
            >>> c.count
            1

        """
        pass  # TODO

    def decrement(self) -> None:
        """Subtract 1 from self.count.

        Example:
            >>> c = Counter(5)
            >>> c.decrement()
            >>> c.count
            4

        """
        pass  # TODO

    def reset(self) -> None:
        """Set self.count back to 0.

        Example:
            >>> c = Counter(5)
            >>> c.reset()
            >>> c.count
            0

        """
        pass  # TODO

    def get_value(self) -> int:
        """Return the current count.

        Example:
            >>> c = Counter(7)
            >>> c.get_value()
            7

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
