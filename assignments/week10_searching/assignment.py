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
    """Return the index of the first matching record."""
    for index, row in enumerate(data):
        if row.get(key) == target:
            return index
    return -1


def binary_search(sorted_data: list[dict[str, Any]], target: Any, key: str) -> int:
    """Binary search a sorted list of dictionaries."""
    low = 0
    high = len(sorted_data) - 1
    while low <= high:
        mid = (low + high) // 2
        value = sorted_data[mid].get(key)
        if value == target:
            return mid
        if value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def compare_search_algorithms(data: list[dict[str, Any]], target: Any, key: str) -> dict[str, int]:
    """Compare linear and binary search results."""
    sorted_data = sorted(data, key=lambda row: row.get(key))
    return {
        'linear_index': linear_search(data, target, key),
        'binary_index': binary_search(sorted_data, target, key),
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

