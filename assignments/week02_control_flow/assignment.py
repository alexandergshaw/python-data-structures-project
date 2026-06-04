"""Week 02 assignment starter for Control Flow."""

WEEK_NUMBER = 2
TOPIC = 'Control Flow'
FEATURE_NAME = 'Data Cleaning Center'

from typing import Any

LEARNING_OBJECTIVES = [
    "Use conditionals to validate records.",
    "Identify missing values and duplicates.",
    "Count records that pass validation rules.",
]


def find_missing_values(data: list[dict[str, Any]]) -> int:
    """Count empty or None values across all rows and columns.

    Example:
        >>> find_missing_values([{"id": 1, "name": "Ava"}, {"id": 2, "name": None}])
        1

    Hints:
        1. Use a nested loop: outer over rows, inner over row.values().
        2. A value is missing when it is None or "" (empty string).
        3. Keep a running count and return it.
    """
    # TODO: Count every value that is None or "" across all rows
    pass


def find_duplicates(data: list[dict[str, Any]]) -> int:
    """Return the number of distinct row patterns that appear more than once.

    Example:
        >>> find_duplicates([{"x": 1}, {"x": 2}, {"x": 1}])
        1

    Hints:
        1. Convert each row to a comparable form:
               marker = tuple(sorted(row.items()))
        2. Build a list of all markers.
        3. For each unique marker, check if it appears more than once.
        4. Count how many unique markers are duplicated.
    """
    # TODO: Count distinct row patterns that appear more than once
    pass


def validate_positive(value: int | float, field_name: str) -> bool:
    """Return True when value >= 0, raise ValueError when value < 0.

    Example:
        >>> validate_positive(10, "price")
        True
        >>> validate_positive(-1, "price")   # raises ValueError
        ...

    Hint:
        if value < 0:
            raise ValueError(f"{field_name} must be non-negative")
        return True
    """
    # TODO: Raise ValueError if value is negative, otherwise return True
    pass


def count_valid_records(data: list[dict[str, Any]]) -> int:
    """Return the number of rows that have no empty or None values.

    Example:
        >>> count_valid_records([{"id": 1, "name": "Ava"}, {"id": 2, "name": ""}])
        1

    Hints:
        1. Loop over each row.
        2. Check whether all values in the row are neither None nor "".
        3. Count and return the rows that pass.
    """
    # TODO: Count rows where every value is non-empty and non-None
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

