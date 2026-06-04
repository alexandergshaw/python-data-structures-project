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
    """Count empty or missing values across all records."""
    return sum(1 for row in data for value in row.values() if value in (None, ""))


def find_duplicates(data: list[dict[str, Any]]) -> int:
    """Count repeated record patterns beyond the first occurrence."""
    markers = [tuple(sorted(row.items())) for row in data]
    return sum(1 for marker in set(markers) if markers.count(marker) > 1)


def validate_positive(value: int | float, field_name: str) -> bool:
    """Return True when a numeric field is zero or greater."""
    if value < 0:
        raise ValueError(f"{field_name} must be non-negative")
    return True


def count_valid_records(data: list[dict[str, Any]]) -> int:
    """Count records that have no empty values."""
    return sum(1 for row in data if all(value not in (None, "") for value in row.values()))


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

