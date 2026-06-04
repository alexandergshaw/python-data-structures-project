# Week 09: Recursion

## Overview
Recursion is a technique where a function calls itself to solve a smaller version of the same problem. It can feel unintuitive at first, but once you see the pattern — *base case* + *recursive case* — it becomes a powerful and elegant tool. This week you write four recursive functions to build that intuition.

## Learning Objectives
- Understand the base case and recursive case pattern.
- Write recursive functions that process lists.
- Flatten a nested list structure recursively.

## Background

### The recursion pattern
Every recursive function needs two parts:

```
def recursive_func(data):
    # 1. BASE CASE — the simplest possible input; return directly
    if data is empty (or size 1):
        return <base value>

    # 2. RECURSIVE CASE — reduce the problem and call self
    return <something> + recursive_func(<smaller input>)
```

The recursive call must always move *closer* to the base case. If it doesn't, the function will recurse forever and Python will raise a `RecursionError`.

### Visualizing the call stack
When you call `recursive_sum([1, 2, 3])`, Python builds a **call stack**:

```
recursive_sum([1, 2, 3])
  = 1 + recursive_sum([2, 3])
            = 2 + recursive_sum([3])
                      = 3 + recursive_sum([])
                                  = 0          ← base case
                      = 3 + 0 = 3
            = 2 + 3 = 5
  = 1 + 5 = 6
```

Each call waits for the next one to return, then adds its own contribution.

## How to Open the Starter File
All your code goes in `assignment.py`.

```
week09_recursion/
├── assignment.py   ← edit this file
├── tests/
│   └── test_week09.py
└── README.md       ← you are here
```

---

## Task 1 — `recursive_sum(data)`

### What it should do
Return the sum of all integers in `data` without using Python's built-in `sum()`.

```
recursive_sum([1, 2, 3])  →  6
recursive_sum([])          →  0
recursive_sum([5])         →  5
```

### Implementation hint
```python
def recursive_sum(data):
    if not data:          # base case: empty list → 0
        return 0
    return data[0] + recursive_sum(data[1:])
                          # ↑ first element   ↑ sum of the rest
```

`data[1:]` is a slice containing everything *except* the first element. Each recursive call shortens the list by one item until it's empty.

---

## Task 2 — `recursive_search(data, target, index=0)`

### What it should do
Return the index of the first occurrence of `target` in `data`, or `-1` if not found. The `index` parameter tracks your current position — start it at `0` (the default).

```
recursive_search(['a', 'b', 'c'], 'b')   →  1
recursive_search(['a', 'b', 'c'], 'z')   →  -1
recursive_search([10, 20, 30],    10)    →  0
```

### How the index advances
```
Call 1: index=0, data[0]='a' ≠ 'b'  →  recurse with index=1
Call 2: index=1, data[1]='b' == 'b' →  return 1  ✓
```

### Implementation hint
```python
def recursive_search(data, target, index=0):
    if index >= len(data):         # base case: ran off the end
        return -1
    if data[index] == target:      # found it
        return index
    return recursive_search(data, target, index + 1)
```

---

## Task 3 — `flatten_nested(data)`

### What it should do
Take a list that may contain other lists (nested to any depth) and return a single flat list.

```
flatten_nested([1, [2, [3]]])  →  [1, 2, 3]
flatten_nested([1, 2, 3])      →  [1, 2, 3]   (already flat)
flatten_nested([])             →  []
```

### How the recursion unfolds
```
flatten_nested([1, [2, [3]]])
  item=1 → not a list → append 1
  item=[2, [3]] → it IS a list → recurse:
      flatten_nested([2, [3]])
        item=2 → append 2
        item=[3] → recurse:
            flatten_nested([3])
              item=3 → append 3
            → [3]
          extend with [3]
      → [2, 3]
    extend with [2, 3]
→ [1, 2, 3]  ✓
```

### Implementation hint
```python
def flatten_nested(data):
    flat = []
    for item in data:
        if isinstance(item, list):
            flat.extend(flatten_nested(item))   # recurse into sub-list
        else:
            flat.append(item)
    return flat
```

---

## Task 4 — `recursive_count(data)`

### What it should do
Return the total number of non-list items in a (possibly nested) list.

```
recursive_count([1, [2, [3]]])  →  3
recursive_count([1, 2, 3, 4])   →  4
```

### Implementation hint
`flatten_nested` already gives you all the leaf values as a flat list — just count them:

```python
def recursive_count(data):
    return len(flatten_nested(data))
```

---

## Unit Tests

### What are unit tests and why do they matter?
Recursive functions fail in specific, predictable ways: forgetting the base case causes infinite recursion; off-by-one errors cause wrong answers. The tests cover both normal cases and edge cases (empty lists, single-element lists, deeply nested lists) to catch these mistakes quickly.

### How to run the tests

**Run only this week's tests:**
```bash
pytest assignments/week09_recursion/tests/ -v
```

**Run all assignments at once:**
```bash
pytest assignments/ -q
```

### What each test checks

| Test name | Input(s) | Expected output |
|-----------|----------|-----------------|
| `test_recursive_sum_basic` | `[1, 2, 3]` | `6` |
| `test_recursive_sum_empty` | `[]` | `0` |
| `test_recursive_sum_single` | `[5]` | `5` |
| `test_recursive_search_found` | `['a','b','c']`, `'b'` | `1` |
| `test_recursive_search_not_found` | `['a','b','c']`, `'z'` | `-1` |
| `test_recursive_search_first_element` | `[10,20,30]`, `10` | `0` |
| `test_flatten_nested_basic` | `[1,[2,[3]]]` | `[1,2,3]` |
| `test_flatten_nested_already_flat` | `[1,2,3]` | `[1,2,3]` |
| `test_flatten_nested_empty` | `[]` | `[]` |
| `test_recursive_count_nested` | `[1,[2,[3]]]` | `3` |
| `test_recursive_count_flat` | `[1,2,3,4]` | `4` |

### Understanding the output
All 11 tests should pass. If you see a `RecursionError`, check that your base case is correct and that each recursive call makes the problem strictly smaller (shorter list, larger index, etc.).
