# Week 04: Review and Integration

## Overview
This week consolidates everything from Weeks 1–3. You will write four functions that each combine multiple concepts: string manipulation, loops, conditionals, and built-in functions. Think of this as a self-check — if you can complete these independently, you are ready for the first test.

## Learning Objectives
- Check whether a string is a palindrome.
- Count vowels in a string using a loop.
- Clamp a value between a minimum and maximum.
- Summarize a list of numbers into a single dictionary.

## How to Open the Starter File
All your code goes in `assignment.py`.

```
week04_review/
├── assignment.py   ← edit this file
├── tests/
│   └── test_week04.py
└── README.md       ← you are here
```

---

## Task 1 — `is_palindrome(s)`

### What it should do
Return `True` if the string reads the same forwards and backwards, `False` otherwise.

```
is_palindrome("racecar")  →  True
is_palindrome("hello")    →  False
is_palindrome("a")        →  True
is_palindrome("")         →  True   (empty string is a palindrome)
```

### Key concept: string slicing and reversal
Python's slice notation `s[start:stop:step]` lets you extract parts of a string. The shorthand `s[::-1]` reverses the entire string by stepping backwards:

```
s = "racecar"

Forward:   r  a  c  e  c  a  r
           0  1  2  3  4  5  6

Reversed:  r  a  c  e  c  a  r   ← same! it's a palindrome
([::-1])   6  5  4  3  2  1  0

s = "hello"

Forward:   h  e  l  l  o
Reversed:  o  l  l  e  h   ← different → not a palindrome
```

A string is a palindrome when `s == s[::-1]`.

### Implementation hint
```python
def is_palindrome(s: str) -> bool:
    return s == s[::-1]
```

---

## Task 2 — `count_vowels(text)`

### What it should do
Count how many vowels (`a, e, i, o, u`) appear in `text`. The check is case-insensitive.

```
count_vowels("hello")  →  2   ('e' and 'o')
count_vowels("AEIOU")  →  5   (all uppercase, still counts)
count_vowels("gym")    →  0   (no vowels)
```

### Key concept: membership check with `in`
The `in` operator checks whether a value exists inside another collection:

```python
'e' in "aeiou"  # → True
'z' in "aeiou"  # → False
```

Loop over every character, convert to lowercase (so 'A' matches 'a'), and count each vowel.

### Implementation hint
```python
def count_vowels(text: str) -> int:
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count
```

---

## Task 3 — `clamp(value, lo, hi)`

### What it should do
Keep `value` within the range `[lo, hi]`. If it falls below `lo`, snap it up to `lo`. If it exceeds `hi`, snap it down to `hi`. Otherwise, leave it unchanged.

```
clamp(5,   1, 10)   →   5   (already inside range)
clamp(-3,  0, 100)  →   0   (below lo → snap to 0)
clamp(200, 0, 100)  →  100  (above hi → snap to 100)
```

Visually:
```
   lo=0 ──────────────────────── hi=100
    │                                │
    │    5 is here → return 5        │
    │                                │
   ─3 is here → return 0    200 is here → return 100
```

### Implementation hint
```python
def clamp(value, lo, hi):
    if value < lo:
        return lo
    if value > hi:
        return hi
    return value
```

---

## Task 4 — `summarize(numbers)`

### What it should do
Return a dictionary that describes the list of numbers using four keys.

| Key | Value |
|-----|-------|
| `"count"` | how many numbers are in the list |
| `"total"` | their sum |
| `"minimum"` | the smallest number |
| `"maximum"` | the largest number |

When `numbers` is empty, return all zeros.

```
summarize([3, 1, 4, 1, 5])
→ {'count': 5, 'total': 14, 'minimum': 1, 'maximum': 5}

summarize([7])
→ {'count': 1, 'total': 7, 'minimum': 7, 'maximum': 7}

summarize([])
→ {'count': 0, 'total': 0, 'minimum': 0, 'maximum': 0}
```

### Key concept: Python's built-in aggregate functions
- `len(numbers)` → count of items
- `sum(numbers)` → total
- `min(numbers)` → smallest
- `max(numbers)` → largest

None of these work on an empty list (except `len` and `sum`), so you must check for the empty case separately.

### Implementation hint
```python
def summarize(numbers):
    if not numbers:
        return {"count": 0, "total": 0, "minimum": 0, "maximum": 0}
    return {
        "count":   len(numbers),
        "total":   sum(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers),
    }
```

---

## Unit Tests

### What are unit tests and why do they matter?
Unit tests automatically verify that each function behaves correctly across a variety of inputs — including edge cases like empty strings, empty lists, and boundary values. Running the tests is much faster than manually trying inputs in the Python shell.

### How to run the tests

**Run only this week's tests:**
```bash
pytest assignments/week04_review/tests/ -v
```

**Run all assignments at once:**
```bash
pytest assignments/ -q
```

### What each test checks

| Test name | Input(s) | Expected output |
|-----------|----------|-----------------|
| `test_is_palindrome_true` | `"racecar"` | `True` |
| `test_is_palindrome_false` | `"hello"` | `False` |
| `test_is_palindrome_single_char` | `"a"` | `True` |
| `test_is_palindrome_empty` | `""` | `True` |
| `test_count_vowels_basic` | `"hello"` | `2` |
| `test_count_vowels_uppercase` | `"AEIOU"` | `5` |
| `test_count_vowels_no_vowels` | `"gym"` | `0` |
| `test_clamp_within_range` | `5, 1, 10` | `5` |
| `test_clamp_below_lo` | `-3, 0, 100` | `0` |
| `test_clamp_above_hi` | `200, 0, 100` | `100` |
| `test_summarize_basic` | `[3,1,4,1,5]` | `{count:5, total:14, minimum:1, maximum:5}` |
| `test_summarize_empty` | `[]` | `{count:0, total:0, minimum:0, maximum:0}` |
| `test_summarize_single` | `[7]` | count=1, min=7, max=7 |

### Understanding the output
All 13 tests should pass. Pay special attention to the empty-list case in `summarize` — it is a common source of `ValueError` if you forget to check `if not numbers` before calling `min()` or `max()`.
