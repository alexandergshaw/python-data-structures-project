# Week 06: Big O Notation

## Overview
Big O notation is the language computer scientists use to describe how an algorithm's runtime or memory usage grows as the input gets larger. This week you will write functions that *measure* elapsed time and *model* how operation counts scale — giving you a hands-on feel for why algorithm efficiency matters.

## Learning Objectives
- Measure how long a function takes to run using `time.perf_counter()`.
- Understand how operation counts grow with input size.
- Generate a human-readable summary of complexity results.

## Background: What is Big O?

Big O describes the **worst-case growth rate** of an algorithm, ignoring constant factors:

```
O(1)        Constant   — runtime doesn't change with input size
             Example: looking up a value by key in a dict

O(log n)    Logarithmic — very slow growth; doubles input → +1 step
             Example: binary search

O(n)        Linear     — proportional to input size
             Example: linear search, counting items in a list

O(n²)       Quadratic  — grows fast; 10× input → 100× slower
             Example: nested loops (bubble sort)
```

Visualized for n = 1, 2, 4, 8, 16:
```
Steps
  ↑
  │                         ●  n²
  │                    ●
  │               ●
  │    ●     ●
  │  ● ●  ●
  │● ● ●  ●  ●              n
  │● ● ●  ●  ●  ●  ●  ●  ● log n
  └─────────────────────────────→ input size (n)
```

## How to Open the Starter File
All your code goes in `assignment.py`.

```
week06_big_o/
├── assignment.py   ← edit this file
├── tests/
│   └── test_week06.py
└── README.md       ← you are here
```

---

## Task 1 — `time_function(func, *args)`

### What it should do
Run `func(*args)` once and return how long it took, in seconds, as a `float`.

```python
elapsed = time_function(sum, [1, 2, 3])
elapsed  # → some small positive float, e.g. 0.000003
```

### Key concept: high-resolution timer
`time.perf_counter()` returns the current time as a high-resolution float (in seconds since some reference point). Subtract the start time from the end time to get elapsed duration:

```
start = time.perf_counter()
func(*args)                      ← run the function
end   = time.perf_counter()
elapsed = end - start            ← always >= 0
```

The `*args` syntax passes all extra arguments directly to `func`, so `time_function(sum, [1,2,3])` calls `sum([1,2,3])`.

### Implementation hint
```python
import time

def time_function(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start
```

---

## Task 2 — `compare_operations(data_sizes)`

### What it should do
Given a list of input sizes, return a list of dictionaries — one per size — each with a `"size"` field and an `"operations"` estimate.

```python
compare_operations([10, 20])
→ [{"size": 10, "operations": 20},
   {"size": 20, "operations": 40}]

compare_operations([5, 10, 15])
→ [{"size": 5, "operations": 10},
   {"size": 10, "operations": 20},
   {"size": 15, "operations": 30}]
```

The `"operations"` field uses `size * 2` as a simple linear model (O(n) with a factor of 2). In a real analysis you would replace this with actual measurements or a more sophisticated model.

### Key concept: list comprehension
A list comprehension builds a new list by transforming each item in an existing iterable:

```python
[{"size": s, "operations": s * 2} for s in data_sizes]
```

This is equivalent to:
```python
result = []
for s in data_sizes:
    result.append({"size": s, "operations": s * 2})
```

### Implementation hint
```python
def compare_operations(data_sizes):
    return [{"size": s, "operations": s * 2} for s in data_sizes]
```

---

## Task 3 — `generate_complexity_report(results)`

### What it should do
Given the list of dictionaries returned by `compare_operations`, return a single human-readable string describing how many data sizes were analyzed.

```python
results = [{"size": 10, "operations": 20}]
generate_complexity_report(results)
# → "Analyzed 1 data sizes."

results = [{"size": 10, "operations": 20}, {"size": 20, "operations": 40}]
generate_complexity_report(results)
# → "Analyzed 2 data sizes."
```

### Key concept: f-string with `len()`
`len(results)` gives the count of items in the list; embed it in an f-string to produce the report.

### Implementation hint
```python
def generate_complexity_report(results):
    return f"Analyzed {len(results)} data sizes."
```

---

## Unit Tests

### What are unit tests and why do they matter?
Unit tests verify functional correctness of each component. For this week they confirm that `time_function` returns a non-negative float (timing cannot be negative), that `compare_operations` produces the right structure and values, and that `generate_complexity_report` formats the output correctly.

### How to run the tests

**Run only this week's tests:**
```bash
pytest assignments/week06_big_o/tests/ -v
```

**Run all assignments at once:**
```bash
pytest assignments/ -q
```

### What each test checks

| Test name | What it verifies |
|-----------|------------------|
| `test_time_function_returns_float` | `time_function(sum, [1,2,3])` returns a `float` |
| `test_time_function_non_negative` | The elapsed time is `>= 0` |
| `test_compare_operations_size_field` | `results[0]['size'] == 10`, `results[1]['size'] == 20` |
| `test_compare_operations_operations_field` | `results[0]['operations'] == 20`, `results[1]['operations'] == 40` |
| `test_compare_operations_length` | Three sizes → three result dicts |
| `test_generate_complexity_report_contains_analyzed` | Report string contains the word `"Analyzed"` |
| `test_generate_complexity_report_contains_count` | Report string contains the count (`"2"`) |

### Understanding the output
All 7 tests should pass. The timing tests (`non_negative`, `returns_float`) are especially simple — if your function correctly uses `perf_counter` and subtracts start from end, these will always pass.
