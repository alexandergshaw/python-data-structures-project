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
    """Return the row count and column count for a dataset.

    Example:
        >>> describe_dataset([{"score": 10}, {"score": 20}])
        {'records': 2, 'columns': 1}
        >>> describe_dataset([])
        {'records': 0, 'columns': 0}

    Hints:
        - "records" = len(data)
        - "columns" = len(data[0]) if data else 0
    """
    # TODO: Return a dict with "records" and "columns"
    pass


def filter_by_value(data: list[dict[str, Any]], column: str, threshold: float) -> list[dict[str, Any]]:
    """Return rows where the column value is >= threshold.

    Example:
        >>> data = [{"score": 10}, {"score": 20}, {"score": 15}]
        >>> filter_by_value(data, "score", 15)
        [{'score': 20}, {'score': 15}]

    Hints:
        - Loop over rows (or use a list comprehension).
        - Keep a row if float(row.get(column, 0) or 0) >= threshold.
    """
    # TODO: Return only the rows that meet the threshold
    pass


def rank_items(data: list[dict[str, Any]], column: str) -> list[dict[str, Any]]:
    """Return the rows sorted from highest to lowest by column.

    Example:
        >>> data = [{"score": 10}, {"score": 20}, {"score": 15}]
        >>> rank_items(data, "score")
        [{'score': 20}, {'score': 15}, {'score': 10}]

    Hint:
        sorted(data, key=lambda row: row.get(column, 0), reverse=True)
    """
    # TODO: Sort and return data in descending order by column
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

