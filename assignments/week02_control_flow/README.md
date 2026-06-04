# Week 02: Control Flow

## Learning Objectives
- Use `if` statements and loops to inspect data.
- Detect missing values and duplicate rows in a dataset.
- Count only the records that pass a validation rule.

## What You Need to Do
Open `assignment.py` and implement the four functions below. Each function body currently contains `pass`—replace that with your code.

---

### Task 1 — `find_missing_values(data)`
Return the total count of empty or `None` values across every row and every column.

```python
data = [{"id": 1, "name": "Ava"}, {"id": 2, "name": None}]
find_missing_values(data)  # → 1  (only name in row 2 is missing)
```

**Hints:**
1. Use a nested loop: outer loop over rows, inner loop over `row.values()`.
2. A value is "missing" when it equals `None` or `""` (empty string).
3. Count each missing value you find and return the total.

---

### Task 2 — `find_duplicates(data)`
Return the number of **distinct** row patterns that appear more than once.

```python
data = [{"x": 1}, {"x": 2}, {"x": 1}]
find_duplicates(data)  # → 1  (the pattern {"x": 1} is duplicated)
```

**Hints:**
1. Convert each row to a `tuple` of sorted `(key, value)` pairs so you can compare rows.
2. For each unique pattern, check whether it appears more than once in the full list.
3. Count how many unique patterns are duplicated.

---

### Task 3 — `validate_positive(value, field_name)`
Return `True` when `value` is zero or greater.  
Raise a `ValueError` when `value` is negative.

```python
validate_positive(10, "price")   # → True
validate_positive(-1, "price")   # raises ValueError
```

**Hint:** Use an `if` statement: if `value < 0` raise the error, otherwise return `True`.

---

### Task 4 — `count_valid_records(data)`
Return the number of rows that have **no** empty or `None` values.

```python
data = [{"id": 1, "name": "Ava"}, {"id": 2, "name": ""}]
count_valid_records(data)  # → 1  (row 2 has an empty name)
```

**Hints:**
1. Loop over the rows.
2. For each row, check whether any value equals `None` or `""`.
3. If none are missing, count that row.

---

## Run Tests
```bash
pytest assignments/week02_control_flow/tests/
```

All tests should pass once you complete each task.
