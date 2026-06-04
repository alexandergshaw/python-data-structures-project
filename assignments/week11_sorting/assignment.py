"""Week 11 assignment starter for Sorting Algorithms."""

WEEK_NUMBER = 11
TOPIC = 'Sorting Algorithms'
FEATURE_NAME = 'Ranking and Leaderboard Dashboard'

from typing import Any

LEARNING_OBJECTIVES = [
    "Implement foundational sorting algorithms.",
    "Compare sorted outputs.",
    "Benchmark sorting approaches conceptually.",
]


def bubble_sort(data: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    """Return data sorted by key using Python's sort as a placeholder."""
    items = data[:]
    items.sort(key=lambda row: row.get(key))
    return items


def insertion_sort(data: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    """Return data sorted by key."""
    return sorted(data, key=lambda row: row.get(key))


def merge_sort(data: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    """Return data sorted by key."""
    return sorted(data, key=lambda row: row.get(key))


def quick_sort(data: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    """Return data sorted by key."""
    return sorted(data, key=lambda row: row.get(key))


def compare_sort_algorithms(data: list[dict[str, Any]], key: str) -> dict[str, list[dict[str, Any]]]:
    """Return outputs from multiple sorting approaches."""
    return {
        'bubble': bubble_sort(data, key),
        'insertion': insertion_sort(data, key),
        'merge': merge_sort(data, key),
        'quick': quick_sort(data, key),
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

