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

    Examples:
        The elapsed time is always a non-negative float:
            >>> elapsed = time_function(sum, [1, 2, 3])
            >>> elapsed >= 0
            True

        Works with any callable — here we time a sort operation:
            >>> elapsed = time_function(sorted, [3, 1, 2])
            >>> elapsed >= 0
            True

        Works with functions that take multiple arguments:
            >>> elapsed = time_function(max, [5, 3, 9])
            >>> elapsed >= 0
            True

    Hints:
        1. start = time.perf_counter()
        2. Call func(*args)
        3. return time.perf_counter() - start
    """
    start = time.perf_counter()
    func(*args)
    return None  # TODO: replace None — return the elapsed time (current time minus start)


def compare_operations(data_sizes: list[int]) -> list[dict[str, int]]:
    """Return a list of dicts showing estimated operation counts per size.

    Each dict has "size" and "operations" (size * 2 as a simple estimate).

    Examples:
        Two sizes are each paired with their estimated operation count:
            >>> compare_operations([10, 20])
            [{'size': 10, 'operations': 20}, {'size': 20, 'operations': 40}]

        A single size produces a single-element list:
            >>> compare_operations([5])
            [{'size': 5, 'operations': 10}]

        An empty input produces an empty list:
            >>> compare_operations([])
            []

        Larger sizes scale proportionally — operations is always size * 2:
            >>> compare_operations([100, 200, 300])
            [{'size': 100, 'operations': 200}, {'size': 200, 'operations': 400}, {'size': 300, 'operations': 600}]

    Hint:
        [{"size": s, "operations": s * 2} for s in data_sizes]
    """
    result = []
    for s in data_sizes:
        result.append({"size": s, "operations": None})  # TODO: replace None — operations is s * 2
    return result


def generate_complexity_report(results: list[dict[str, int]]) -> str:
    """Return a summary string for the given operation results.

    Examples:
        A single-item result set is reported as "1 data sizes":
            >>> generate_complexity_report([{"size": 10, "operations": 20}])
            'Analyzed 1 data sizes.'

        Multiple results are counted and reported:
            >>> generate_complexity_report([{"size": 10, "operations": 20}, {"size": 20, "operations": 40}])
            'Analyzed 2 data sizes.'

        An empty results list reports zero:
            >>> generate_complexity_report([])
            'Analyzed 0 data sizes.'

    Hint:
        f"Analyzed {len(results)} data sizes."
    """
    return None  # TODO: replace None — return f"Analyzed {len(results)} data sizes."


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

