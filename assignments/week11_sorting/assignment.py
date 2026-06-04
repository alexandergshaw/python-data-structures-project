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
    """Sort data ascending by key using the bubble sort algorithm.

    Example:
        >>> data = [{"score": 3}, {"score": 1}, {"score": 2}]
        >>> bubble_sort(data, "score")
        [{'score': 1}, {'score': 2}, {'score': 3}]

    Algorithm:
        1. items = data[:]            # copy the list
        2. Outer loop: for i in range(len(items))
        3. Inner loop: for j in range(len(items) - 1 - i)
        4.     if items[j][key] > items[j+1][key]:
                   items[j], items[j+1] = items[j+1], items[j]
        5. return items
    """
    # TODO: Implement bubble sort using nested loops
    pass


def insertion_sort(data: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    """Return data sorted ascending by key.

    Hint:
        sorted(data, key=lambda row: row.get(key))
    """
    # TODO: Return data sorted by key (use sorted())
    pass


def merge_sort(data: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    """Return data sorted ascending by key.

    Hint:
        sorted(data, key=lambda row: row.get(key))
    """
    # TODO: Return data sorted by key (use sorted())
    pass


def quick_sort(data: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    """Return data sorted ascending by key.

    Hint:
        sorted(data, key=lambda row: row.get(key))
    """
    # TODO: Return data sorted by key (use sorted())
    pass


def compare_sort_algorithms(data: list[dict[str, Any]], key: str) -> dict[str, list[dict[str, Any]]]:
    """Run all four sorts and return their outputs in a single dict.

    The dict must have keys: "bubble", "insertion", "merge", "quick".

    Example:
        >>> compare_sort_algorithms([{"score": 2}, {"score": 1}], "score")
        {'bubble': [...], 'insertion': [...], 'merge': [...], 'quick': [...]}

    Hint:
        Call each of the four sorting functions and put the results in a dict.
    """
    # TODO: Call all four sort functions and return their results in a dict
    pass


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

