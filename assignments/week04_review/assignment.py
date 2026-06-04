"""Week 04 assignment starter for Review and Integration."""

WEEK_NUMBER = 4
TOPIC = 'Review and Integration'
FEATURE_NAME = 'Analytics Progress Dashboard'

from typing import Any

LEARNING_OBJECTIVES = [
    "Integrate multiple dataset helpers.",
    "Generate multi-dataset reports.",
    "Calculate business growth rates.",
]


def combine_datasets(d1: list[dict[str, Any]], d2: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return a single list containing all rows from d1 followed by all rows from d2.

    Example:
        >>> combine_datasets([{"id": 1}], [{"id": 2}, {"id": 3}])
        [{'id': 1}, {'id': 2}, {'id': 3}]

    Hint:
        Use the + operator: list(d1) + list(d2)
    """
    # TODO: Combine and return both lists
    pass


def generate_report(datasets: list[list[dict[str, Any]]]) -> dict[str, int]:
    """Return a summary report for a list of datasets.

    The returned dict must have:
        "dataset_count" - how many datasets were provided
        "total_records" - total number of rows across all datasets

    Example:
        >>> generate_report([[{"id": 1}], [{"id": 2}, {"id": 3}]])
        {'dataset_count': 2, 'total_records': 3}

    Hints:
        - dataset_count = len(datasets)
        - total_records = sum(len(ds) for ds in datasets)
    """
    # TODO: Build and return the report dict
    pass


def calculate_growth_rate(old_val: float, new_val: float) -> float:
    """Return the percentage change from old_val to new_val.

    Return 0.0 when old_val is 0 (avoids division by zero).

    Formula: ((new_val - old_val) / old_val) * 100

    Example:
        >>> calculate_growth_rate(100, 125)
        25.0
        >>> calculate_growth_rate(200, 150)
        -25.0
        >>> calculate_growth_rate(0, 50)
        0.0

    Hint:
        Check if old_val == 0 first and return 0.0.
    """
    # TODO: Compute and return the growth rate percentage
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

