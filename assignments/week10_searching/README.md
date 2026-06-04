# Week 10: Searching Algorithms

## Overview
Searching is the process of finding a specific item in a collection. This week you implement two classic algorithms — **linear search** and **binary search** — and compare them side by side. Understanding when to use each is one of the most practical skills in programming.

## Learning Objectives
- Implement linear search (works on any list).
- Implement binary search (works on a sorted list).
- Use both algorithms and compare their results.

## Background

### Linear Search — O(n)
Scan from the beginning of the list, checking each item one by one, until you find a match or reach the end. It works on *any* list (sorted or not) but can be slow for large inputs.

```
target = 3
data = [1, 4, 2, 3, 5]

Check index 0 → 1 ≠ 3
Check index 1 → 4 ≠ 3
Check index 2 → 2 ≠ 3
Check index 3 → 3 == 3  ✓  return 3
```

In the worst case (item at the end or not found), you scan all *n* items → O(n).

### Binary Search — O(log n)
Jump to the middle of a **sorted** list. If the middle value matches, you're done. If the target is smaller, search the left half. If larger, search the right half. Each step cuts the remaining search space in half.

```
target = 3
sorted_data = [1, 2, 3, 4, 5]
               0  1  2  3  4   ← indices

low=0, high=4 → mid=2 → data[2]=3 == 3  ✓  return 2
(found in one step!)
```

Another example, target = 5:
```
low=0, high=4 → mid=2 → data[2]=3 < 5 → search right half
low=3, high=4 → mid=3 → data[3]=4 < 5 → search right half
low=4, high=4 → mid=4 → data[4]=5 == 5  ✓  return 4
```

| | Linear Search | Binary Search |
|---|---|---|
| Requires sorted input? | No | **Yes** |
| Time complexity | O(n) | O(log n) |
| Best for | Small/unsorted data | Large sorted datasets |

The dataset in this week's assignment is a list of **dictionaries**. You search by a specific key within each dictionary (e.g., `"id"`).

## How to Open the Starter File
All your code goes in `assignment.py`.

```
week10_searching/
├── assignment.py   ← edit this file
├── tests/
│   └── test_week10.py
└── README.md       ← you are here
```

---

## Task 1 — `linear_search(data, target, key)`

### What it should do
Return the index of the first row where `row[key] == target`, or `-1` if not found.

```python
data = [{"id": 1}, {"id": 2}, {"id": 3}]
linear_search(data, 2, "id")  →  1
linear_search(data, 9, "id")  →  -1
linear_search(data, 1, "id")  →  0
```

### Key concept: `enumerate()`
`enumerate(data)` yields `(index, row)` pairs so you can track both the index and the row at the same time:

```python
for index, row in enumerate(data):
    if row.get(key) == target:
        return index
return -1
```

Using `.get(key)` instead of `row[key]` is safer — it returns `None` if the key doesn't exist rather than raising a `KeyError`.

---

## Task 2 — `binary_search(sorted_data, target, key)`

### What it should do
Return the index of the row where `row[key] == target` in a *sorted* list, or `-1` if not found. The list must already be sorted by `key` in ascending order.

```python
data = [{"id": 1}, {"id": 2}, {"id": 3}]
binary_search(data, 3, "id")  →  2
binary_search(data, 1, "id")  →  0
binary_search(data, 9, "id")  →  -1
```

### Step-by-step algorithm

```
low = 0
high = len(sorted_data) - 1

while low <= high:
    mid = (low + high) // 2          # integer division → middle index
    value = sorted_data[mid].get(key)

    if value == target:
        return mid                    # found!
    elif value < target:
        low = mid + 1                 # target is in the right half
    else:
        high = mid - 1               # target is in the left half

return -1  # not found
```

---

## Task 3 — `compare_search_algorithms(data, target, key)`

### What it should do
Run both search algorithms on the same data and return both results in a dictionary.

```python
data = [{"id": 1}, {"id": 2}, {"id": 3}]
compare_search_algorithms(data, 1, "id")
→ {"linear_index": 0, "binary_index": 0}
```

### Important: binary search needs sorted data
The input `data` may not be sorted. Sort it by `key` before passing it to `binary_search`:

```python
sorted_data = sorted(data, key=lambda row: row.get(key))
```

Then call each algorithm and combine the results:
```python
return {
    "linear_index": linear_search(data, target, key),
    "binary_index": binary_search(sorted_data, target, key),
}
```

---

## Unit Tests

### What are unit tests and why do they matter?
Search algorithm tests check three scenarios: finding an item at the beginning, finding one in the middle/end, and failing to find one at all (returning `-1`). If any of these fail, your loop bounds, comparison operators, or index arithmetic likely have a bug.

### How to run the tests

**Run only this week's tests:**
```bash
pytest assignments/week10_searching/tests/ -v
```

**Run all assignments at once:**
```bash
pytest assignments/ -q
```

### What each test checks

| Test name | Input(s) | Expected output |
|-----------|----------|-----------------|
| `test_linear_search_found` | target=2 in `[{id:1},{id:2},{id:3}]` | `1` |
| `test_linear_search_first` | target=1 | `0` |
| `test_linear_search_not_found` | target=9 | `-1` |
| `test_binary_search_found` | target=3 in sorted list | `2` |
| `test_binary_search_first` | target=1 | `0` |
| `test_binary_search_not_found` | target=9 | `-1` |
| `test_compare_search_linear_index` | target=1 | `linear_index == 0` |
| `test_compare_search_binary_index` | target=1 | `binary_index == 0` |

### Understanding the output
All 8 tests should pass. If binary search fails for the first element (`index 0`), double-check your `while low <= high` condition — using `<` instead of `<=` misses the case where `low == high`.
