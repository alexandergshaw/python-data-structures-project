# Week 05: Test 1 Preparation

## Learning Objectives
- Check whether two strings are anagrams.
- Find the maximum value in a list without using `max()`.
- Reverse a string.
- Merge two dictionaries.

## What You Need to Do
Open `assignment.py` and implement the four functions below. These tasks combine concepts from Weeks 1–4.

---

### Task 1 — `is_anagram(a, b)`
Return `True` if `a` and `b` are anagrams of each other (same letters, any order).
The comparison is case-insensitive.

```python
is_anagram("listen", "silent")  # → True
is_anagram("hello", "world")    # → False
```

**Hint:** Sort the lowercase characters of each string and compare:
```python
sorted(a.lower()) == sorted(b.lower())
```

---

### Task 2 — `find_max(numbers)`
Return the largest number in `numbers` **without** using the built-in `max()`.
Return `None` if the list is empty.

```python
find_max([3, 1, 4, 1, 5, 9])  # → 9
find_max([-5, -1, -3])         # → -1
find_max([])                   # → None
```

**Hints:**
1. Return `None` immediately if `numbers` is empty.
2. Start with `current_max = numbers[0]`.
3. Loop over the rest; update `current_max` whenever you find a larger value.

---

### Task 3 — `reverse_string(s)`
Return `s` reversed.

```python
reverse_string("hello")   # → "olleh"
reverse_string("Python")  # → "nohtyP"
reverse_string("")         # → ""
```

**Hint:** Use slice notation: `s[::-1]`

---

### Task 4 — `merge_dicts(d1, d2)`
Return a new dictionary with all entries from both `d1` and `d2`.
When both share a key, `d2`'s value wins.

```python
merge_dicts({"a": 1, "b": 2}, {"b": 99, "c": 3})
# → {'a': 1, 'b': 99, 'c': 3}
```

**Hint:**
```python
result = dict(d1)
result.update(d2)
return result
```

---

## Run Tests
```bash
pytest assignments/week05_test1/tests/
```

All tests should pass once you complete each task.
