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
    """A named collection of records (rows as dictionaries)."""

    def __init__(self, name: str, records: list[dict[str, Any]] | None = None) -> None:
        """Store the dataset name and an initial list of records.

        Example:
            >>> ds = Dataset("sales", [{"id": 1}])
            >>> ds.name
            'sales'

        Hints:
            - Save name to self.name.
            - Save a COPY of records to self.records (or [] if records is None).
              Use records[:] to copy, or just [] when None.
        """
        self.name = None   # TODO: replace None — store the name parameter
        self.records = None  # TODO: replace None — use records[:] if records is not None, else []

    def add_record(self, record: dict[str, Any]) -> None:
        """Append a new record (dict) to self.records.

        Example:
            >>> ds = Dataset("sales")
            >>> ds.add_record({"id": 1})
            >>> len(ds.records)
            1

        Hint:
            Use self.records.append(record).
        """
        pass  # TODO: append record to self.records

    def get_summary(self) -> dict[str, Any]:
        """Return a dict with keys "name", "records", and "columns".

        "records" is the row count.
        "columns" is the number of keys in the first row (0 if empty).

        Example:
            >>> ds = Dataset("sales")
            >>> ds.add_record({"id": 1, "amount": 50})
            >>> ds.get_summary()
            {'name': 'sales', 'records': 1, 'columns': 2}

        Hints:
            - columns = len(self.records[0]) if self.records else 0
        """
        columns = None  # TODO: replace None — use len(self.records[0]) if self.records else 0
        return {
            "name": self.name,
            "records": len(self.records),
            "columns": columns,
        }


class KPI:
    """A named key performance indicator with a numeric value."""

    def __init__(self, name: str, value: float = 0.0) -> None:
        """Store the KPI name and initial value.

        Example:
            >>> kpi = KPI("Revenue")
            >>> kpi.name
            'Revenue'

        Hint:
            Set self.name = name and self.value = value.
        """
        self.name = None   # TODO: replace None — store the name parameter
        self.value = None  # TODO: replace None — store the value parameter

    def calculate(self, values: list[int | float]) -> float:
        """Compute the average of values, store it in self.value, and return it.

        Return 0.0 when values is empty.

        Example:
            >>> kpi = KPI("Revenue")
            >>> kpi.calculate([10, 20, 30])
            20.0

        Hints:
            - Average = sum(values) / len(values)
            - Guard against empty list: return 0.0 if not values
        """
        if not values:
            return 0.0
        self.value = None  # TODO: replace None — compute sum(values) / len(values)
        return self.value

    def format_value(self) -> str:
        """Return self.value formatted to 2 decimal places with commas.

        Example:
            >>> kpi = KPI("Revenue", 20.0)
            >>> kpi.format_value()
            '20.00'

        Hint:
            Use f"{self.value:,.2f}"
        """
        return None  # TODO: replace None — use an f-string: f"{self.value:,.2f}"


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

