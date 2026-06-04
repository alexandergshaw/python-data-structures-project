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

    Examples:
        Searching for id=2 in a three-row list finds it at index 1:
            >>> data = [{"id": 1}, {"id": 2}, {"id": 3}]
            >>> linear_search(data, 2, "id")
            1

        A target that doesn't exist in any row returns -1:
            >>> data = [{"id": 1}, {"id": 2}, {"id": 3}]
            >>> linear_search(data, 9, "id")
            -1

        The first matching row is returned even when duplicates exist:
            >>> data = [{"id": 5}, {"id": 5}, {"id": 5}]
            >>> linear_search(data, 5, "id")
            0

        An empty dataset always returns -1:
            >>> linear_search([], 1, "id")
            -1

        Works with string values, not just integers:
            >>> data = [{"name": "Alice"}, {"name": "Bob"}]
            >>> linear_search(data, "Bob", "name")
            1

    Hints:
        1. Use enumerate(data) to get both index and row.
        2. Return index when row.get(key) == target.
        3. Return -1 after the loop.
    """
    for index, row in enumerate(data):
        if row.get(key) == target:
            return None  # TODO: replace None — return the index of this matching row
    return -1


def binary_search(sorted_data: list[dict[str, Any]], target: Any, key: str) -> int:
    """Return the index of the row where row[key] == target in a sorted list, or -1.

    sorted_data MUST already be sorted by key in ascending order.

    Examples:
        Target found at the last position in a sorted three-row list:
            >>> data = [{"id": 1}, {"id": 2}, {"id": 3}]
            >>> binary_search(data, 3, "id")
            2

        Target found at the first position:
            >>> data = [{"id": 1}, {"id": 2}, {"id": 3}]
            >>> binary_search(data, 1, "id")
            0

        A target that doesn't exist returns -1:
            >>> data = [{"id": 1}, {"id": 2}, {"id": 3}]
            >>> binary_search(data, 99, "id")
            -1

        An empty dataset always returns -1:
            >>> binary_search([], 1, "id")
            -1

    Hints:
        1. low = 0, high = len(sorted_data) - 1
        2. While low <= high:
               mid = (low + high) // 2
               value = sorted_data[mid].get(key)
               if value == target: return mid
               elif value < target: low = mid + 1
               else: high = mid - 1
        3. Return -1
    """
    low = 0
    high = len(sorted_data) - 1
    while low <= high:
        mid = (low + high) // 2
        value = sorted_data[mid].get(key)
        if value == target:
            return mid
        elif value < target:
            low = None  # TODO: replace None — move the lower bound past mid
        else:
            high = None  # TODO: replace None — move the upper bound below mid
    return -1


def compare_search_algorithms(data: list[dict[str, Any]], target: Any, key: str) -> dict[str, int]:
    """Run linear and binary search, return both result indices.

    Examples:
        Both algorithms find target=1 at index 0 in already-sorted data:
            >>> data = [{"id": 1}, {"id": 2}, {"id": 3}]
            >>> compare_search_algorithms(data, 1, "id")
            {'linear_index': 0, 'binary_index': 0}

        Both return -1 when the target is missing:
            >>> data = [{"id": 1}, {"id": 2}, {"id": 3}]
            >>> compare_search_algorithms(data, 99, "id")
            {'linear_index': -1, 'binary_index': -1}

        Binary search sorts the data internally before searching, so indices
        may differ from linear when the input is unsorted:
            >>> data = [{"id": 3}, {"id": 1}, {"id": 2}]
            >>> result = compare_search_algorithms(data, 1, "id")
            >>> result['linear_index']
            1

    Hints:
        1. sorted_data = sorted(data, key=lambda r: r.get(key))
        2. linear_index = linear_search(data, target, key)
        3. binary_index = binary_search(sorted_data, target, key)
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

