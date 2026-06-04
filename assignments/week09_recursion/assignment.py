"""Week 09 assignment starter for Recursion."""

WEEK_NUMBER = 9
TOPIC = 'Recursion'
FEATURE_NAME = 'Nested Data Explorer'

from typing import Any

LEARNING_OBJECTIVES = [
    "Sum data recursively.",
    "Search recursively.",
    "Flatten nested structures.",
]


def recursive_sum(data: list[int]) -> int:
    """Return the sum of all integers in data using recursion (no sum()).

    Example:
        >>> recursive_sum([1, 2, 3])
        6
        >>> recursive_sum([])
        0

    """
    if not data:
        return 0
    return None  # TODO


def recursive_search(data: list[Any], target: Any, index: int = 0) -> int:
    """Return the index of the first occurrence of target, or -1 if not found.

    Example:
        >>> recursive_search(['a', 'b', 'c'], 'b')
        1
        >>> recursive_search(['a', 'b', 'c'], 'z')
        -1

    """
    if index >= len(data):
        return -1
    if data[index] == target:
        return index
    return None  # TODO


def flatten_nested(data: list[Any]) -> list[Any]:
    """Return a flat list from a nested list structure.

    Example:
        >>> flatten_nested([1, [2, [3]]])
        [1, 2, 3]
        >>> flatten_nested([1, 2, 3])
        [1, 2, 3]

    """
    flat = []
    for item in data:
        if isinstance(item, list):
            pass  # TODO
        else:
            pass  # TODO
    return flat


def recursive_count(data: list[Any]) -> int:
    """Return the total number of non-list items in a nested list.

    Example:
        >>> recursive_count([1, [2, [3]]])
        3

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

