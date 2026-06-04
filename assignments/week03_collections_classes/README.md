# Week 03: Collections and Classes

## Learning Objectives
- Create Python classes with `__init__`, instance variables, and methods.
- Store and inspect data inside a class.
- Compute a numeric result and format it as a string.

## What You Need to Do
Open `assignment.py` and implement the two classes below.

---

### Task 1 — `Dataset` class

A `Dataset` holds a collection of named records.

#### `__init__(self, name, records=None)`
- Store `name` as `self.name`.
- Store a **copy** of `records` (or an empty list when `records` is `None`) as `self.records`.

#### `add_record(self, record)`
- Append `record` (a dictionary) to `self.records`.

#### `get_summary(self) -> dict`
- Return a dictionary with three keys: `"name"`, `"records"`, and `"columns"`.
- `"records"` = number of rows in `self.records`.
- `"columns"` = number of keys in the first row (or `0` if empty).

```python
ds = Dataset("sales")
ds.add_record({"id": 1, "amount": 50})
ds.get_summary()
# → {"name": "sales", "records": 1, "columns": 2}
```

---

### Task 2 — `KPI` class

A `KPI` stores a named metric value.

#### `__init__(self, name, value=0.0)`
- Store `name` as `self.name` and `value` as `self.value`.

#### `calculate(self, values) -> float`
- Compute the **average** of the numbers in `values`.
- Save the result to `self.value` and return it.
- Return `0.0` when `values` is empty.

#### `format_value(self) -> str`
- Return `self.value` formatted to two decimal places with commas.

```python
kpi = KPI("Revenue")
kpi.calculate([10, 20, 30])  # → 20.0
kpi.format_value()            # → "20.00"
```

**Hints for `calculate`:**
- Use `sum(values) / len(values)` for the average.
- Guard against an empty list with an `if` check.

**Hint for `format_value`:**
- Use `f"{self.value:,.2f}"`.

---

## Run Tests
```bash
pytest assignments/week03_collections_classes/tests/
```

All tests should pass once you complete each class.
