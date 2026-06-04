# Week 11: Sorting Algorithms

## Overview
Sorting is one of the most studied problems in computer science. This week you implement **bubble sort** by hand to understand how comparison-based sorting works at a low level, then use Python's built-in `sorted()` for three other algorithm names (insertion, merge, quick) to focus on the interface each provides. Finally, you write a comparison function that runs all four and shows their outputs side by side.

## Learning Objectives
- Implement bubble sort step by step.
- Use Python's built-in `sorted()` for simpler sorts.
- Compare the output of multiple sorting approaches.

## Background

### Why sorting matters
- Searching is faster on sorted data (binary search requires it).
- Database queries, ranking, and reporting all depend on sorted data.
- Understanding sort complexity helps you choose the right algorithm.

### Complexity comparison

| Algorithm | Best | Average | Worst | Notes |
|-----------|------|---------|-------|-------|
| Bubble sort | O(n) | O(n²) | O(n²) | Simple to implement; slow on large data |
| Insertion sort | O(n) | O(n²) | O(n²) | Fast on nearly-sorted data |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | Stable; uses extra memory |
| Quick sort | O(n log n) | O(n log n) | O(n²) | Fast in practice; in-place |

### Bubble sort illustrated
Each pass through the list "bubbles" the largest unsorted element to its correct position:

```
Initial:    [3, 1, 2]

Pass 1:
  Compare 3,1 → 3 > 1 → swap  →  [1, 3, 2]
  Compare 3,2 → 3 > 2 → swap  →  [1, 2, 3]
           ↑ 3 is now in its correct final position

Pass 2:
  Compare 1,2 → 1 < 2 → no swap  →  [1, 2, 3]
           ↑ 2 is now in its correct final position

Result: [1, 2, 3]  ✓
```

With two nested loops, the outer loop runs `n` times and the inner loop runs up to `n-1` times — that is why bubble sort is O(n²).

## How to Open the Starter File
All your code goes in `assignment.py`. Each function sorts a list of dictionaries by a specified `key`.

```
week11_sorting/
├── assignment.py   ← edit this file
├── tests/
│   └── test_week11.py
└── README.md       ← you are here
```

---

## Task 1 — `bubble_sort(data, key)` ← implement manually

### What it should do
Sort `data` in ascending order by `key` using the bubble sort algorithm. **Do not mutate the original list** — work on a copy.

```python
data = [{"score": 3}, {"score": 1}, {"score": 2}]
bubble_sort(data, "score")
# → [{"score": 1}, {"score": 2}, {"score": 3}]

# Original unchanged:
data[0]["score"]  # → 3  (still the original first element)
```

### Step-by-step algorithm
```python
def bubble_sort(data, key):
    items = data[:]                        # 1. make a copy
    n = len(items)
    for i in range(n):                     # 2. outer loop: n passes
        for j in range(n - 1 - i):        # 3. inner loop: shrinks each pass
            if items[j][key] > items[j+1][key]:   # 4. compare adjacent
                items[j], items[j+1] = items[j+1], items[j]   # 5. swap
    return items
```

The inner loop runs `n-1-i` times (not `n-1`) because after each outer pass, the last `i` elements are already in their final positions.

---

## Task 2 — `insertion_sort(data, key)`

### What it should do
Return `data` sorted ascending by `key`.

For this assignment, use Python's built-in `sorted()`:
```python
def insertion_sort(data, key):
    return sorted(data, key=lambda row: row.get(key))
```

---

## Task 3 — `merge_sort(data, key)`

### What it should do
Return `data` sorted ascending by `key`.

```python
def merge_sort(data, key):
    return sorted(data, key=lambda row: row.get(key))
```

---

## Task 4 — `quick_sort(data, key)`

### What it should do
Return `data` sorted ascending by `key`.

```python
def quick_sort(data, key):
    return sorted(data, key=lambda row: row.get(key))
```

---

## Task 5 — `compare_sort_algorithms(data, key)`

### What it should do
Run all four sorting functions on the same data and return a dictionary with keys `"bubble"`, `"insertion"`, `"merge"`, and `"quick"`, each holding the sorted result.

```python
data = [{"score": 3}, {"score": 1}, {"score": 2}]
compare_sort_algorithms(data, "score")
# → {
#     "bubble":    [{"score": 1}, {"score": 2}, {"score": 3}],
#     "insertion": [{"score": 1}, {"score": 2}, {"score": 3}],
#     "merge":     [{"score": 1}, {"score": 2}, {"score": 3}],
#     "quick":     [{"score": 1}, {"score": 2}, {"score": 3}],
#   }
```

### Implementation hint
```python
def compare_sort_algorithms(data, key):
    return {
        "bubble":    bubble_sort(data, key),
        "insertion": insertion_sort(data, key),
        "merge":     merge_sort(data, key),
        "quick":     quick_sort(data, key),
    }
```

---

## Unit Tests

### What are unit tests and why do they matter?
Tests for sorting algorithms verify two things: (1) the output is in the correct order, and (2) the original input was not mutated. The non-mutation check (`test_bubble_sort_does_not_mutate`) is especially important for bubble sort, since you are instructed to work on a copy.

### How to run the tests

**Run only this week's tests:**
```bash
pytest assignments/week11_sorting/tests/ -v
```

**Run all assignments at once:**
```bash
pytest assignments/ -q
```

### What each test checks

| Test name | What it verifies |
|-----------|------------------|
| `test_bubble_sort_ascending` | `[3,1,2]` sorted by score → `[1,2,3]` |
| `test_bubble_sort_does_not_mutate` | Original data `[3,1]` is unchanged after sort |
| `test_insertion_sort_ascending` | `[3,1,2]` → `[1,2,3]` |
| `test_merge_sort_ascending` | `[3,1,2]` → `[1,2,3]` |
| `test_quick_sort_ascending` | `[3,1,2]` → `[1,2,3]` |
| `test_compare_sort_algorithms_keys` | Result has keys `bubble`, `insertion`, `merge`, `quick` |
| `test_compare_sort_algorithms_results` | Both `bubble` and `quick` results are `[1,2,3]` |

### Understanding the output
All 7 tests should pass. If `test_bubble_sort_does_not_mutate` fails, make sure the very first line of `bubble_sort` is `items = data[:]` to work on a copy rather than the original list.
