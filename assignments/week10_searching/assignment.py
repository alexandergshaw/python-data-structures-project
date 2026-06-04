"""Week 10 assignment starter for Searching Algorithms."""

WEEK_NUMBER = 10
TOPIC = 'Searching Algorithms'
FEATURE_NAME = 'Advanced Dataset Search'

from typing import Any

LEARNING_OBJECTIVES = [
    "Implement linear search.",
    "Implement binary search.",
    "Compare search strategies.",
]


def linear_search(data: list[dict[str, Any]], target: Any, key: str) -> int:
    """Return the index of the first row where row[key] == target, or -1.

    Example:
        >>> data = [{"id": 1}, {"id": 2}, {"id": 3}]
        >>> linear_search(data, 2, "id")
        1
        >>> linear_search(data, 9, "id")
        -1

    """
    for index, row in enumerate(data):
        if row.get(key) == target:
            return None  # TODO
    return -1


def binary_search(sorted_data: list[dict[str, Any]], target: Any, key: str) -> int:
    """Return the index of the row where row[key] == target in a sorted list, or -1.

    sorted_data MUST already be sorted by key in ascending order.

    Example:
        >>> data = [{"id": 1}, {"id": 2}, {"id": 3}]
        >>> binary_search(data, 3, "id")
        2

    """
    low = 0
    high = len(sorted_data) - 1
    while low <= high:
        mid = (low + high) // 2
        value = sorted_data[mid].get(key)
        if value == target:
            return mid
        elif value < target:
            low = None  # TODO
        else:
            high = None  # TODO
    return -1


def compare_search_algorithms(data: list[dict[str, Any]], target: Any, key: str) -> dict[str, int]:
    """Run linear and binary search, return both result indices.

    Example:
        >>> data = [{"id": 1}, {"id": 2}, {"id": 3}]
        >>> compare_search_algorithms(data, 1, "id")
        {'linear_index': 0, 'binary_index': 0}

    """
    sorted_data = sorted(data, key=lambda r: r.get(key))
    return {
        "linear_index": linear_search(data, target, key),
        "binary_index": binary_search(sorted_data, target, key),
    }


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

