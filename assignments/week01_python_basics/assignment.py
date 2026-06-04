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
    """Return the total number of rows in a dataset.

    A dataset is a list of dictionaries. Each dictionary is one row.

    Example:
        >>> count_records([{"id": 1}, {"id": 2}])
        2
        >>> count_records([])
        0

    Hint:
        Use the built-in len() function on the list.
    """
    return None  # TODO: replace None — use len() to count the rows in data


def count_columns(data: list[dict[str, Any]]) -> int:
    """Return the number of columns in the first row of the dataset.

    Return 0 if the dataset is empty.

    Example:
        >>> count_columns([{"id": 1, "name": "Ava"}])
        2
        >>> count_columns([])
        0

    Hints:
        1. First check whether data is empty. If so, return 0.
        2. Access the first row with data[0].
        3. Count the keys in that row with len().
    """
    if not data:
        return 0
    first_row = data[0]
    return None  # TODO: replace None — use len() to count the keys in first_row


def get_dataset_summary(data: list[dict[str, Any]], name: str) -> dict[str, Any]:
    """Return a summary dictionary for a named dataset.

    The dictionary must have exactly these keys: "name", "records", "columns".

    Example:
        >>> get_dataset_summary([{"id": 1}], "sales")
        {'name': 'sales', 'records': 1, 'columns': 1}

    Hint:
        Call count_records() and count_columns() to fill in the values.
    """
    return {
        "name": None,     # TODO: replace None with the dataset name
        "records": None,  # TODO: replace None — call count_records(data)
        "columns": None,  # TODO: replace None — call count_columns(data)
    }


def format_number(n: int | float) -> str:
    """Return a number formatted with commas as a string.

    Example:
        >>> format_number(12000)
        '12,000'
        >>> format_number(1000000)
        '1,000,000'

    Hint:
        Use an f-string with the comma format specifier: f"{n:,}"
    """
    return None  # TODO: replace None — use an f-string with the :, format specifier on n


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

