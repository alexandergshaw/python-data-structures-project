# Week 03: Collections and Classes

## Learning Objectives
- Build reusable classes for datasets and KPIs.
- Store records in object-oriented structures.
- Compute formatted KPI values.

## Assignment Instructions
Implement the starter functions and classes in `assignment.py`. Keep your changes inside this file only so the InsightHub platform can auto-detect completion safely.

## Functions to Implement
- `class Dataset`
- `def __init__(self, name`
- `def add_record(self, record`
- `def get_summary(self) -> dict[str, Any]`
- `class KPI`
- `def __init__(self, name`
- `def calculate(self, values`
- `def format_value(self) -> str`

## Run Tests
```bash
pytest assignments/week03_collections_classes/tests/
```

## Check Completion
```bash
python -c "from assignments.week03_collections_classes.assignment import is_complete; print(is_complete())"
```
