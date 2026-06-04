"""Week 05 assignment starter for Test 1 Preparation."""

WEEK_NUMBER = 5
TOPIC = 'Test 1 Preparation'
FEATURE_NAME = 'Python Fundamentals Badge'

from typing import Any

LEARNING_OBJECTIVES = [
    "Describe datasets clearly.",
    "Filter records based on thresholds.",
    "Rank analytics items by a field.",
]


def describe_dataset(data: list[dict[str, Any]]) -> dict[str, int]:
    """Describe dataset size and column count."""
    return {"records": len(data), "columns": len(data[0]) if data else 0}


def filter_by_value(data: list[dict[str, Any]], column: str, threshold: float) -> list[dict[str, Any]]:
    """Return records where the column value is at least the threshold."""
    return [row for row in data if float(row.get(column, 0) or 0) >= threshold]


def rank_items(data: list[dict[str, Any]], column: str) -> list[dict[str, Any]]:
    """Return data sorted descending by a chosen column."""
    return sorted(data, key=lambda row: row.get(column, 0), reverse=True)


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

