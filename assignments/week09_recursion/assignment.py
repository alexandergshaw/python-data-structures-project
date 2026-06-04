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
    """Return the recursive sum of a list of integers."""
    if not data:
        return 0
    return data[0] + recursive_sum(data[1:])


def recursive_search(data: list[Any], target: Any, index: int = 0) -> int:
    """Return the index of target or -1 when missing."""
    if index >= len(data):
        return -1
    if data[index] == target:
        return index
    return recursive_search(data, target, index + 1)


def flatten_nested(data: list[Any]) -> list[Any]:
    """Flatten nested lists recursively."""
    flat: list[Any] = []
    for item in data:
        if isinstance(item, list):
            flat.extend(flatten_nested(item))
        else:
            flat.append(item)
    return flat


def recursive_count(data: list[Any]) -> int:
    """Count items recursively, flattening nested lists."""
    return len(flatten_nested(data))


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

