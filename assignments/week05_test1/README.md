# Week 05: Test 1 Preparation

## Overview
This assignment reviews and combines everything from Weeks 1–4 to prepare you for Test 1. You will implement four functions that each require you to apply multiple concepts together. Work through each task without referencing previous assignments — that is the best way to prepare.

## Learning Objectives
- Check whether two strings are anagrams.
- Find the maximum value in a list without using `max()`.
- Reverse a string.
- Merge two dictionaries.

## How to Open the Starter File
All your code goes in `assignment.py`.

```
week05_test1/
├── assignment.py   ← edit this file
├── tests/
│   └── test_week05.py
└── README.md       ← you are here
```

---

## Task 1 — `is_anagram(a, b)`

### What it should do
Return `True` if `a` and `b` are anagrams of each other — that is, if they contain the exact same letters in any order. The comparison is case-insensitive.

```
is_anagram("listen", "silent")  →  True
is_anagram("hello",  "world")   →  False
is_anagram("Listen", "Silent")  →  True   (case-insensitive)
```

### Key concept: sorting characters
Two strings are anagrams when their sorted character lists are identical:

```
"listen"  →  lowercase  →  "listen"  →  sorted  →  ['e','i','l','n','s','t']
"silent"  →  lowercase  →  "silent"  →  sorted  →  ['e','i','l','n','s','t']
                                                      ← equal! → True
```

Compare that to:
```
"hello"  →  sorted  →  ['e','h','l','l','o']
"world"  →  sorted  →  ['d','l','o','r','w']
                        ← not equal → False
```

### Implementation hint
```python
def is_anagram(a: str, b: str) -> bool:
    return sorted(a.lower()) == sorted(b.lower())
```

---

## Task 2 — `find_max(numbers)`

### What it should do
Return the largest number in `numbers` **without** using Python's built-in `max()`. Return `None` if the list is empty.

```
find_max([3, 1, 4, 1, 5, 9])  →  9
find_max([-5, -1, -3])         →  -1   (all negative, -1 is the largest)
find_max([42])                 →  42
find_max([])                   →  None
```

### Key concept: tracking a running maximum
Walk through the list and keep track of the largest value seen so far:

```
numbers = [3, 1, 4, 1, 5, 9]

current_max = 3   (start with the first element)
  compare 1 → 1 < 3, no update   →  current_max = 3
  compare 4 → 4 > 3, update      →  current_max = 4
  compare 1 → 1 < 4, no update   →  current_max = 4
  compare 5 → 5 > 4, update      →  current_max = 5
  compare 9 → 9 > 5, update      →  current_max = 9
return 9  ✓
```

### Implementation hint
```python
def find_max(numbers):
    if not numbers:
        return None
    current_max = numbers[0]
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
    return current_max
```

---

## Task 3 — `reverse_string(s)`

### What it should do
Return `s` with its characters in reverse order.

```
reverse_string("hello")   →  "olleh"
reverse_string("Python")  →  "nohtyP"
reverse_string("")         →  ""
```

### Key concept: slice reversal
The slice `s[::-1]` steps through the string backwards, producing a reversed copy:

```
"hello"
  h e l l o
  4 3 2 1 0  ← stepping backwards
→ "olleh"
```

### Implementation hint
```python
def reverse_string(s: str) -> str:
    return s[::-1]
```

---

## Task 4 — `merge_dicts(d1, d2)`

### What it should do
Return a new dictionary containing all key-value pairs from both `d1` and `d2`. When both dictionaries share a key, `d2`'s value wins.

```
merge_dicts({"a": 1, "b": 2}, {"b": 99, "c": 3})
→ {'a': 1, 'b': 99, 'c': 3}
           ^^^^^^^^
           d2 overwrote d1's "b"

merge_dicts({"a": 1}, {"b": 2})
→ {'a': 1, 'b': 2}   (no overlap, both keys kept)

merge_dicts({}, {"x": 10})
→ {'x': 10}
```

### Key concept: dict.update()
`dict.update(other)` copies all key-value pairs from `other` into the dictionary, overwriting any keys that already exist. By starting with a copy of `d1` and then calling `update(d2)`, `d2`'s values take priority for shared keys.

```
result = {"a": 1, "b": 2}    # copy of d1
result.update({"b": 99, "c": 3})   # d2 overrides "b"
result  →  {"a": 1, "b": 99, "c": 3}
```

### Implementation hint
```python
def merge_dicts(d1: dict, d2: dict) -> dict:
    result = dict(d1)
    result.update(d2)
    return result
```

---

## Unit Tests

### What are unit tests and why do they matter?
Unit tests verify that your implementation handles not just the "obvious" cases but also edge cases — empty inputs, all-negative values, overlapping dictionary keys, and case differences. Catching these on test day can be the difference between a pass and a fail.

### How to run the tests

**Run only this week's tests:**
```bash
pytest assignments/week05_test1/tests/ -v
```

**Run all assignments at once:**
```bash
pytest assignments/ -q
```

### What each test checks

| Test name | Input(s) | Expected output |
|-----------|----------|-----------------|
| `test_is_anagram_true` | `"listen"`, `"silent"` | `True` |
| `test_is_anagram_false` | `"hello"`, `"world"` | `False` |
| `test_is_anagram_case_insensitive` | `"Listen"`, `"Silent"` | `True` |
| `test_find_max_basic` | `[3,1,4,1,5,9]` | `9` |
| `test_find_max_negatives` | `[-5,-1,-3]` | `-1` |
| `test_find_max_empty` | `[]` | `None` |
| `test_find_max_single` | `[42]` | `42` |
| `test_reverse_string_basic` | `"hello"` | `"olleh"` |
| `test_reverse_string_mixed_case` | `"Python"` | `"nohtyP"` |
| `test_reverse_string_empty` | `""` | `""` |
| `test_merge_dicts_basic` | `{"a":1,"b":2}`, `{"b":99,"c":3}` | `{"a":1,"b":99,"c":3}` |
| `test_merge_dicts_no_overlap` | `{"a":1}`, `{"b":2}` | `{"a":1,"b":2}` |
| `test_merge_dicts_empty_first` | `{}`, `{"x":10}` | `{"x":10}` |

### Understanding the output
All 13 tests should pass. If `test_find_max_negatives` fails, double-check that you initialize `current_max` to `numbers[0]` and **not** to `0` — starting at `0` would incorrectly return `0` for all-negative lists.
