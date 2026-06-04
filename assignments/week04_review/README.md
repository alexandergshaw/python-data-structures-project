# Week 04: Review and Integration

## Learning Objectives
- Combine two datasets into one.
- Generate a simple summary report from multiple datasets.
- Calculate a percentage growth rate between two numbers.

## What You Need to Do
Open `assignment.py` and implement the three functions below.

---

### Task 1 — `combine_datasets(d1, d2)`
Return a single list that contains all rows from `d1` followed by all rows from `d2`.

```python
d1 = [{"id": 1}]
d2 = [{"id": 2}, {"id": 3}]
combine_datasets(d1, d2)  # → [{"id": 1}, {"id": 2}, {"id": 3}]
```

**Hint:** Use the `+` operator to concatenate two lists.

---

### Task 2 — `generate_report(datasets)`
Given a list of datasets (each dataset is a list of rows), return a dictionary with:
- `"dataset_count"`: how many datasets were passed in.
- `"total_records"`: the total number of rows across all datasets.

```python
datasets = [[{"id": 1}], [{"id": 2}, {"id": 3}]]
generate_report(datasets)
# → {"dataset_count": 2, "total_records": 3}
```

**Hints:**
1. `dataset_count` = `len(datasets)`.
2. `total_records` = sum of `len(ds)` for each dataset in the list.

---

### Task 3 — `calculate_growth_rate(old_val, new_val)`
Return the percentage change from `old_val` to `new_val`.

Formula: `((new_val - old_val) / old_val) * 100`

Return `0.0` if `old_val` is `0` (to avoid division by zero).

```python
calculate_growth_rate(100, 125)  # → 25.0
calculate_growth_rate(200, 150)  # → -25.0
calculate_growth_rate(0, 50)     # → 0.0
```

---

## Run Tests
```bash
pytest assignments/week04_review/tests/
```

All tests should pass once you complete each task.
