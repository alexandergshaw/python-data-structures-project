# Week 04: Review and Integration

## Learning Objectives
- Check whether a string is a palindrome.
- Count vowels in a string using a loop.
- Clamp a value between a minimum and maximum.
- Summarize a list of numbers into a single dictionary.

## What You Need to Do
Open `assignment.py` and implement the four functions below.

---

### Task 1 — `is_palindrome(s)`
Return `True` if `s` reads the same forwards and backwards, `False` otherwise.

```python
is_palindrome("racecar")  # → True
is_palindrome("hello")    # → False
is_palindrome("a")        # → True
```

**Hint:** A string is a palindrome when `s == s[::-1]`. The `[::-1]` slice reverses a string.

---

### Task 2 — `count_vowels(text)`
Return the number of vowels (`a, e, i, o, u`) in `text`. The check is case-insensitive.

```python
count_vowels("hello")  # → 2
count_vowels("AEIOU")  # → 5
count_vowels("gym")    # → 0
```

**Hints:**
1. Convert to lowercase first: `text.lower()`
2. Loop over each character.
3. Check if the character is in `"aeiou"`.
4. Count matches and return the total.

---

### Task 3 — `clamp(value, lo, hi)`
Return `value` kept within the range `[lo, hi]`.

- If `value < lo`, return `lo`.
- If `value > hi`, return `hi`.
- Otherwise return `value`.

```python
clamp(5, 1, 10)    # → 5
clamp(-3, 0, 100)  # → 0
clamp(200, 0, 100) # → 100
```

---

### Task 4 — `summarize(numbers)`
Return a dictionary describing the list of numbers.

| Key | Value |
|-----|-------|
| `"count"` | how many numbers |
| `"total"` | their sum |
| `"minimum"` | the smallest |
| `"maximum"` | the largest |

Return all zeros when `numbers` is empty.

```python
summarize([3, 1, 4, 1, 5])
# → {'count': 5, 'total': 14, 'minimum': 1, 'maximum': 5}

summarize([])
# → {'count': 0, 'total': 0, 'minimum': 0, 'maximum': 0}
```

**Hint:** Use `len()`, `sum()`, `min()`, and `max()`.

---

## Run Tests
```bash
pytest assignments/week04_review/tests/
```

All tests should pass once you complete each task.
