"""Week 01 assignment starter for Python Basics."""

WEEK_NUMBER = 1
TOPIC = 'Python Basics'
FEATURE_NAME = 'Dataset Explorer'

from typing import Any

LEARNING_OBJECTIVES = [
    "Practice working with lists and dictionaries.",
    "Summarize tabular datasets using Python basics.",
    "Format numeric analytics results clearly.",
]


def count_records(data: list[dict[str, Any]]) -> int:
    """Return the number of records in a dataset.

    Example:
        >>> count_records([{"id": 1}, {"id": 2}])
        2
    """
    return len(data)


def count_columns(data: list[dict[str, Any]]) -> int:
    """Return the number of columns in the first record.

    Example:
        >>> count_columns([{"id": 1, "name": "Ava"}])
        2
    """
    if not data:
        return 0
    return len(data[0])


def get_dataset_summary(data: list[dict[str, Any]], name: str) -> dict[str, Any]:
    """Return a summary dictionary for a dataset.

    Example:
        >>> get_dataset_summary([{"id": 1}], "sales")
        {'name': 'sales', 'records': 1, 'columns': 1}
    """
    return {"name": name, "records": count_records(data), "columns": count_columns(data)}


def format_number(n: int | float) -> str:
    """Format a number with commas for dashboard display.

    Example:
        >>> format_number(12000)
        '12,000'
    """
    return f"{n:,}"


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

