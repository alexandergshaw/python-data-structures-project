# Week 09: Recursion

## Learning Objectives
- Understand the base case and recursive case pattern.
- Write recursive functions that process lists.
- Flatten a nested list structure recursively.

## Background
A recursive function calls *itself* with a smaller input until it reaches the **base case** (when the input is small enough to return directly).

General pattern:
```python
def recursive_func(data):
    if <base case>:      # list is empty or problem is trivial
        return <base value>
    return <something> + recursive_func(<smaller input>)
```

## What You Need to Do
Open `assignment.py` and implement the four functions below.

---

### Task 1 — `recursive_sum(data)`
Return the sum of all integers in `data` without using Python's built-in `sum()`.

```python
recursive_sum([1, 2, 3])  # → 6
recursive_sum([])          # → 0
```

**Hints:**
- Base case: if `data` is empty, return `0`.
- Recursive case: `data[0] + recursive_sum(data[1:])`.

---

### Task 2 — `recursive_search(data, target, index=0)`
Return the index of the first occurrence of `target` in `data`, or `-1` if not found.

```python
recursive_search(['a', 'b', 'c'], 'b')  # → 1
recursive_search(['a', 'b', 'c'], 'z')  # → -1
```

**Hints:**
- Base case: if `index >= len(data)`, return `-1`.
- If `data[index] == target`, return `index`.
- Otherwise, return `recursive_search(data, target, index + 1)`.

---

### Task 3 — `flatten_nested(data)`
Return a flat (one-level) list from a potentially nested list.

```python
flatten_nested([1, [2, [3]]])  # → [1, 2, 3]
flatten_nested([1, 2, 3])      # → [1, 2, 3]
```

**Hints:**
1. Start with `flat = []`.
2. Loop over each `item` in `data`.
3. If `item` is a `list`, extend `flat` with `flatten_nested(item)`.
4. Otherwise, append `item` to `flat`.
5. Return `flat`.

---

### Task 4 — `recursive_count(data)`
Return the total number of non-list items in a (possibly nested) list.

```python
recursive_count([1, [2, [3]]])  # → 3
```

**Hint:** Call `flatten_nested(data)` and return `len(...)` of the result.

---

## Run Tests
```bash
pytest assignments/week09_recursion/tests/
```

All tests should pass once you complete each function.
