# Week 11: Sorting Algorithms

## Learning Objectives
- Implement bubble sort step by step.
- Use Python's built-in `sorted()` for simpler sorts.
- Compare the output of multiple sorting approaches.

## Background
Sorting arranges items in order. There are many algorithms:
- **Bubble sort**: Repeatedly compare adjacent items and swap them if out of order.
- **Insertion / merge / quick sort**: More efficient approaches covered in class.

Each function sorts a list of dictionaries by a specified key.

## What You Need to Do
Open `assignment.py` and implement the five functions below.

---

### Task 1 — `bubble_sort(data, key)` ← implement manually
Sort `data` in ascending order by `key` using the bubble sort algorithm.

**Algorithm:**
1. Copy the list: `items = data[:]`.
2. Use two nested loops. The outer loop runs `len(items)` times.
3. The inner loop compares adjacent pairs: if `items[j][key] > items[j+1][key]`, swap them.
4. Return `items`.

```python
data = [{"score": 3}, {"score": 1}, {"score": 2}]
bubble_sort(data, "score")
# → [{"score": 1}, {"score": 2}, {"score": 3}]
```

---

### Task 2 — `insertion_sort(data, key)`
Return `data` sorted ascending by `key`.

**Hint:** Use Python's `sorted(data, key=lambda row: row.get(key))`.

---

### Task 3 — `merge_sort(data, key)`
Return `data` sorted ascending by `key`.

**Hint:** Use Python's `sorted(data, key=lambda row: row.get(key))`.

---

### Task 4 — `quick_sort(data, key)`
Return `data` sorted ascending by `key`.

**Hint:** Use Python's `sorted(data, key=lambda row: row.get(key))`.

---

### Task 5 — `compare_sort_algorithms(data, key)`
Run all four sorts and return their results in a dict with keys `"bubble"`, `"insertion"`, `"merge"`, and `"quick"`.

```python
compare_sort_algorithms(data, "score")
# → {"bubble": [...], "insertion": [...], "merge": [...], "quick": [...]}
```

---

## Run Tests
```bash
pytest assignments/week11_sorting/tests/
```

All tests should pass once you complete each function.
