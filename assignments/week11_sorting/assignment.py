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

    Examples:
        Three rows sorted by "score" in ascending order:
            >>> data = [{"score": 3}, {"score": 1}, {"score": 2}]
            >>> bubble_sort(data, "score")
            [{'score': 1}, {'score': 2}, {'score': 3}]

        Already-sorted data is returned unchanged:
            >>> data = [{"score": 1}, {"score": 2}, {"score": 3}]
            >>> bubble_sort(data, "score")
            [{'score': 1}, {'score': 2}, {'score': 3}]

        An empty list returns an empty list:
            >>> bubble_sort([], "score")
            []

        A single-element list is trivially sorted:
            >>> bubble_sort([{"score": 5}], "score")
            [{'score': 5}]

        The original list is not modified — a copy is returned:
            >>> original = [{"score": 3}, {"score": 1}]
            >>> sorted_copy = bubble_sort(original, "score")
            >>> original
            [{'score': 3}, {'score': 1}]

    Algorithm:
        1. items = data[:]            # copy the list
        2. Outer loop: for i in range(len(items))
        3. Inner loop: for j in range(len(items) - 1 - i)
        4.     if items[j][key] > items[j+1][key]:
                   items[j], items[j+1] = items[j+1], items[j]
        5. return items
    """
    items = data[:]
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j][key] > items[j + 1][key]:
                pass  # TODO: swap items[j] and items[j+1]
    return items


def insertion_sort(data: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    """Return data sorted ascending by key.

    Examples:
        Three rows sorted by "score" in ascending order:
            >>> data = [{"score": 3}, {"score": 1}, {"score": 2}]
            >>> insertion_sort(data, "score")
            [{'score': 1}, {'score': 2}, {'score': 3}]

        An empty list returns an empty list:
            >>> insertion_sort([], "score")
            []

        Already-sorted data is returned unchanged:
            >>> data = [{"score": 1}, {"score": 2}]
            >>> insertion_sort(data, "score")
            [{'score': 1}, {'score': 2}]

    Hint:
        sorted(data, key=lambda row: row.get(key))
    """
    return None  # TODO: replace None — use sorted() with key=lambda row: row.get(key)


def merge_sort(data: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    """Return data sorted ascending by key.

    Examples:
        Three rows sorted by "score" in ascending order:
            >>> data = [{"score": 3}, {"score": 1}, {"score": 2}]
            >>> merge_sort(data, "score")
            [{'score': 1}, {'score': 2}, {'score': 3}]

        An empty list returns an empty list:
            >>> merge_sort([], "score")
            []

        Already-sorted data is returned unchanged:
            >>> data = [{"score": 1}, {"score": 2}]
            >>> merge_sort(data, "score")
            [{'score': 1}, {'score': 2}]

    Hint:
        sorted(data, key=lambda row: row.get(key))
    """
    return None  # TODO: replace None — use sorted() with key=lambda row: row.get(key)


def quick_sort(data: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    """Return data sorted ascending by key.

    Examples:
        Three rows sorted by "score" in ascending order:
            >>> data = [{"score": 3}, {"score": 1}, {"score": 2}]
            >>> quick_sort(data, "score")
            [{'score': 1}, {'score': 2}, {'score': 3}]

        An empty list returns an empty list:
            >>> quick_sort([], "score")
            []

        Already-sorted data is returned unchanged:
            >>> data = [{"score": 1}, {"score": 2}]
            >>> quick_sort(data, "score")
            [{'score': 1}, {'score': 2}]

    Hint:
        sorted(data, key=lambda row: row.get(key))
    """
    return None  # TODO: replace None — use sorted() with key=lambda row: row.get(key)


def compare_sort_algorithms(data: list[dict[str, Any]], key: str) -> dict[str, list[dict[str, Any]]]:
    """Run all four sorts and return their outputs in a single dict.

    The dict must have keys: "bubble", "insertion", "merge", "quick".

    Examples:
        All four algorithms produce the same sorted output for the same input:
            >>> data = [{"score": 2}, {"score": 1}]
            >>> result = compare_sort_algorithms(data, "score")
            >>> result["bubble"]
            [{'score': 1}, {'score': 2}]
            >>> result["insertion"]
            [{'score': 1}, {'score': 2}]
            >>> result["merge"]
            [{'score': 1}, {'score': 2}]
            >>> result["quick"]
            [{'score': 1}, {'score': 2}]

        All four keys are always present in the returned dict:
            >>> result = compare_sort_algorithms([{"score": 5}], "score")
            >>> sorted(result.keys())
            ['bubble', 'insertion', 'merge', 'quick']

    Hint:
        Call each of the four sorting functions and put the results in a dict.
    """
    return {
        "bubble": bubble_sort(data, key),
        "insertion": None,  # TODO: replace None — call insertion_sort with data and key
        "merge": None,      # TODO: replace None — call merge_sort with data and key
        "quick": None,      # TODO: replace None — call quick_sort with data and key
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

