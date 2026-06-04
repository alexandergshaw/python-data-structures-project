"""Week 03 assignment starter for Collections and Classes."""

WEEK_NUMBER = 3
TOPIC = 'Collections and Classes'
FEATURE_NAME = 'KPI Dashboard'

from typing import Any

LEARNING_OBJECTIVES = [
    "Build reusable classes for datasets and KPIs.",
    "Store records in object-oriented structures.",
    "Compute formatted KPI values.",
]


class Dataset:
    """Represent a named collection of records."""

    def __init__(self, name: str, records: list[dict[str, Any]] | None = None) -> None:
        self.name = name
        self.records = records[:] if records else []

    def add_record(self, record: dict[str, Any]) -> None:
        """Add a record to the dataset."""
        self.records.append(record)

    def get_summary(self) -> dict[str, Any]:
        """Return a summary of the dataset."""
        columns = len(self.records[0]) if self.records else 0
        return {"name": self.name, "records": len(self.records), "columns": columns}


class KPI:
    """Represent a KPI metric with a numeric value."""

    def __init__(self, name: str, value: float = 0.0) -> None:
        self.name = name
        self.value = value

    def calculate(self, values: list[int | float]) -> float:
        """Calculate the average from a sequence of values."""
        self.value = sum(values) / len(values) if values else 0.0
        return self.value

    def format_value(self) -> str:
        """Format the KPI value for display."""
        return f"{self.value:,.2f}"


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

