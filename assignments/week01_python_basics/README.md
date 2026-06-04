# Week 01: Python Basics

## Learning Objectives
- Work with lists of dictionaries (tabular data).
- Write simple functions that inspect and summarize a dataset.
- Format numbers as human-readable strings.

## What You Need to Do
Open `assignment.py` and implement the four functions below. Each function body currently contains `pass`—replace that with your code.

---

### Task 1 — `count_records(data)`
Return the total number of rows in a dataset.

A dataset is a **list of dictionaries**, where each dictionary is one row.

```python
data = [{"id": 1, "name": "Ava"}, {"id": 2, "name": "Liam"}]
count_records(data)  # → 2
```

**Hint:** Use Python's built-in `len()` function.

---

### Task 2 — `count_columns(data)`
Return how many columns (keys) exist in the first row of the dataset.
Return `0` if the dataset is empty.

```python
data = [{"id": 1, "name": "Ava"}]
count_columns(data)  # → 2
```

**Hints:**
- Check whether `data` is empty first.
- Access the first element with `data[0]`, then count its keys.

---

### Task 3 — `get_dataset_summary(data, name)`
Return a dictionary with three keys: `"name"`, `"records"`, and `"columns"`.

```python
data = [{"id": 1}]
get_dataset_summary(data, "sales")
# → {"name": "sales", "records": 1, "columns": 1}
```

**Hint:** Call your `count_records` and `count_columns` functions to fill in the values.

---

### Task 4 — `format_number(n)`
Return a number formatted with commas as a string.

```python
format_number(12000)   # → "12,000"
format_number(1000000) # → "1,000,000"
```

**Hint:** Use an f-string with the `,` format specifier: `f"{n:,}"`.

---

## Run Tests
```bash
pytest assignments/week01_python_basics/tests/
```

All four tests should pass once you complete each task.
