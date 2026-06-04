# Week 05: Test 1 Preparation

## Learning Objectives
- Describe the shape of a dataset (rows and columns).
- Filter rows using a threshold value.
- Sort rows in descending order by a chosen column.

## What You Need to Do
Open `assignment.py` and implement the three functions below.

---

### Task 1 — `describe_dataset(data)`
Return a dictionary with keys `"records"` and `"columns"` describing the dataset's size.

```python
data = [{"score": 10}, {"score": 20}]
describe_dataset(data)  # → {"records": 2, "columns": 1}
```

**Hints:**
- `"records"` = `len(data)`.
- `"columns"` = `len(data[0])` if data is not empty, else `0`.

---

### Task 2 — `filter_by_value(data, column, threshold)`
Return only the rows where the value in `column` is **greater than or equal to** `threshold`.

```python
data = [{"score": 10}, {"score": 20}, {"score": 15}]
filter_by_value(data, "score", 15)
# → [{"score": 20}, {"score": 15}]
```

**Hints:**
1. Loop over the rows (or use a list comprehension).
2. Keep a row if `float(row.get(column, 0) or 0) >= threshold`.

---

### Task 3 — `rank_items(data, column)`
Return the rows sorted from highest to lowest by the values in `column`.

```python
data = [{"score": 10}, {"score": 20}, {"score": 15}]
rank_items(data, "score")
# → [{"score": 20}, {"score": 15}, {"score": 10}]
```

**Hint:** Use Python's `sorted()` with `reverse=True` and a `key` function:
```python
sorted(data, key=lambda row: row.get(column, 0), reverse=True)
```

---

## Run Tests
```bash
pytest assignments/week05_test1/tests/
```

All tests should pass once you complete each task.
