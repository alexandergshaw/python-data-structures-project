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
    """Combine two datasets into one list."""
    return list(d1) + list(d2)


def generate_report(datasets: list[list[dict[str, Any]]]) -> dict[str, int]:
    """Generate a simple report about datasets provided."""
    total_records = sum(len(dataset) for dataset in datasets)
    return {"dataset_count": len(datasets), "total_records": total_records}


def calculate_growth_rate(old_val: float, new_val: float) -> float:
    """Calculate percentage growth between two values."""
    if old_val == 0:
        return 0.0
    return ((new_val - old_val) / old_val) * 100


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

