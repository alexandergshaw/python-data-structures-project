# Week 06: Big O Notation

## Learning Objectives
- Measure how long a function takes to run.
- Understand how operation counts grow with input size.
- Generate a readable summary of results.

## Background
Big O notation describes how an algorithm's runtime grows as the input gets larger. This week you will write helpers that measure and summarize that behavior.

## What You Need to Do
Open `assignment.py` and implement the three functions below.

---

### Task 1 — `time_function(func, *args)`
Run `func(*args)` and return how long it took in seconds (as a `float`).

```python
import time
elapsed = time_function(sum, [1, 2, 3])
elapsed  # → some small float like 0.000005
```

**Hints:**
1. Record the start time with `time.perf_counter()`.
2. Call `func(*args)`.
3. Record the end time and return `end - start`.

---

### Task 2 — `compare_operations(data_sizes)`
Given a list of input sizes, return a list of dictionaries, one per size.
Each dictionary must have:
- `"size"`: the input size.
- `"operations"`: an estimate of operations — use `size * 2` as a simple placeholder.

```python
compare_operations([10, 20])
# → [{"size": 10, "operations": 20}, {"size": 20, "operations": 40}]
```

**Hint:** Use a list comprehension:
```python
[{"size": s, "operations": s * 2} for s in data_sizes]
```

---

### Task 3 — `generate_complexity_report(results)`
Given the list of dicts returned by `compare_operations`, return a human-readable string that says how many data sizes were analyzed.

```python
results = [{"size": 10, "operations": 20}]
generate_complexity_report(results)  # → "Analyzed 1 data sizes."
```

**Hint:** Use an f-string with `len(results)`.

---

## Run Tests
```bash
pytest assignments/week06_big_o/tests/
```

All tests should pass once you complete each task.
