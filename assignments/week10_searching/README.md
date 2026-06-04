# Week 10: Searching Algorithms

## Learning Objectives
- Implement linear search (works on any list).
- Implement binary search (works on a sorted list).
- Use both algorithms and compare their results.

## Background
- **Linear search**: Scan from the beginning until you find a match. Works on *any* list. O(n).
- **Binary search**: Jump to the middle, decide which half to continue searching. Only works on a *sorted* list. O(log n).

## What You Need to Do
Open `assignment.py` and implement the three functions below. The dataset is a list of dictionaries, and you search on a specific key within each dictionary.

---

### Task 1 — `linear_search(data, target, key)`
Return the index of the first row where `row[key] == target`, or `-1` if not found.

```python
data = [{"id": 1}, {"id": 2}, {"id": 3}]
linear_search(data, 2, "id")  # → 1
linear_search(data, 9, "id")  # → -1
```

**Hints:**
1. Use `enumerate(data)` to loop with both index and row.
2. Return `index` when `row.get(key) == target`.
3. Return `-1` after the loop ends without a match.

---

### Task 2 — `binary_search(sorted_data, target, key)`
Return the index of the row where `row[key] == target` in a *sorted* list, or `-1` if not found.

```python
data = [{"id": 1}, {"id": 2}, {"id": 3}]
binary_search(data, 3, "id")  # → 2
```

**Hints (classic binary search):**
1. Start with `low = 0`, `high = len(sorted_data) - 1`.
2. While `low <= high`:
   - `mid = (low + high) // 2`
   - `value = sorted_data[mid].get(key)`
   - If `value == target`: return `mid`.
   - If `value < target`: `low = mid + 1`.
   - Else: `high = mid - 1`.
3. Return `-1`.

---

### Task 3 — `compare_search_algorithms(data, target, key)`
Run both searches and return a dict showing each result index.

```python
data = [{"id": 1}, {"id": 2}, {"id": 3}]
compare_search_algorithms(data, 1, "id")
# → {"linear_index": 0, "binary_index": 0}
```

**Hints:**
1. Sort `data` by `key` for binary search: `sorted_data = sorted(data, key=lambda r: r.get(key))`.
2. Call `linear_search(data, target, key)` for the linear result.
3. Call `binary_search(sorted_data, target, key)` for the binary result.
4. Return both in a dict.

---

## Run Tests
```bash
pytest assignments/week10_searching/tests/
```

All tests should pass once you complete each function.
