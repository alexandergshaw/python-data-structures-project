"""Week 06 assignment starter for Big O Analysis."""

WEEK_NUMBER = 6
TOPIC = 'Big O Analysis'
FEATURE_NAME = 'Algorithm Analysis Center'

import time
from typing import Any, Callable

LEARNING_OBJECTIVES = [
    "Measure runtime for functions.",
    "Compare performance at multiple input sizes.",
    "Summarize complexity observations.",
]


def time_function(func: Callable[..., Any], *args: Any) -> float:
    """Run func(*args) and return the elapsed time in seconds.

    Example:
        >>> elapsed = time_function(sum, [1, 2, 3])
        >>> elapsed >= 0
        True

    Hints:
        1. start = time.perf_counter()
        2. Call func(*args)
        3. return time.perf_counter() - start
    """
    # TODO: Record start time, call the function, return elapsed time
    pass


def compare_operations(data_sizes: list[int]) -> list[dict[str, int]]:
    """Return a list of dicts showing estimated operation counts per size.

    Each dict has "size" and "operations" (size * 2 as a simple estimate).

    Example:
        >>> compare_operations([10, 20])
        [{'size': 10, 'operations': 20}, {'size': 20, 'operations': 40}]

    Hint:
        [{"size": s, "operations": s * 2} for s in data_sizes]
    """
    # TODO: Build and return the list of size/operations dicts
    pass


def generate_complexity_report(results: list[dict[str, int]]) -> str:
    """Return a summary string for the given operation results.

    Example:
        >>> generate_complexity_report([{"size": 10, "operations": 20}])
        'Analyzed 1 data sizes.'

    Hint:
        f"Analyzed {len(results)} data sizes."
    """
    # TODO: Return a descriptive string using len(results)
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

