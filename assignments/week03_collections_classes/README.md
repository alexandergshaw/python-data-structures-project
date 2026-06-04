# Week 03: Collections and Classes

## Overview
This week introduces two of Python's most useful built-in data structures — `set` and `dict` — and shows you how to create your own objects with a `class`. Collections let you group related data; classes let you bundle data *and* behavior together into a single, reusable unit.

## Learning Objectives
- Remove duplicates with a `set` and sort a list.
- Count word occurrences with a dictionary.
- Build a simple class with an `__init__` and methods.

## How to Open the Starter File
All your code goes in `assignment.py`. Implement the two functions and one class described below.

```
week03_collections_classes/
├── assignment.py   ← edit this file
├── tests/
│   └── test_week03.py
└── README.md       ← you are here
```

---

## Task 1 — `get_unique_items(items)`

### What it should do
Accept a list that may contain duplicates. Return a **sorted** list with each item appearing only once.

```
get_unique_items([3, 1, 2, 1, 3])   →  [1, 2, 3]
get_unique_items(["b", "a", "b"])   →  ['a', 'b']
get_unique_items([1, 2, 3])         →  [1, 2, 3]   (already unique, just sorted)
```

### Key concept: sets
A **set** is an unordered collection that automatically eliminates duplicates:

```
list   →  [3, 1, 2, 1, 3]   duplicates allowed, ordered
             ↓  set(...)
set    →  {1, 2, 3}          no duplicates, but unordered
             ↓  sorted(...)
list   →  [1, 2, 3]          no duplicates, sorted
```

`sorted()` takes any iterable (including a set) and returns a new sorted list.

### Implementation hint
```python
def get_unique_items(items):
    return sorted(set(items))
```

---

## Task 2 — `word_frequency(words)`

### What it should do
Count how many times each word appears in the list and return a dictionary mapping word → count.

```
word_frequency(["hi", "bye", "hi"])  →  {'hi': 2, 'bye': 1}
word_frequency([])                   →  {}
word_frequency(["a", "a", "a"])      →  {'a': 3}
```

### Key concept: building a frequency dictionary
Dictionaries map keys to values. The pattern for counting is:

```
freq = {}                           # start empty
for each word in words:
    freq[word] = freq.get(word, 0) + 1
                 ^^^^^^^^^^^^^^^^^^^^^
                 look up current count (default 0) and add 1
return freq
```

`dict.get(key, default)` returns the value for `key` if it exists, otherwise returns `default`. This avoids a `KeyError` on the first occurrence of a new word.

### Implementation hint
```python
def word_frequency(words):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
```

---

## Task 3 — `Counter` class

### What it should do
A `Counter` is a simple object that keeps track of a running integer count. It supports incrementing, decrementing, resetting, and reading the current value.

```python
c = Counter()       # default start: 0
c.increment()
c.increment()
c.get_value()       # → 2

c.decrement()
c.get_value()       # → 1

c.reset()
c.get_value()       # → 0

c2 = Counter(10)    # custom start
c2.get_value()      # → 10
```

### Key concept: classes and instance variables
A **class** is a blueprint for creating objects. The `__init__` method runs automatically when you create an object (`Counter()`). Instance variables like `self.count` store data that belongs to each specific object:

```
class Counter:
    def __init__(self, start=0):    ← runs on Counter()
        self.count = start          ← each object has its own .count

    def increment(self):
        self.count += 1             ← modifies THIS object's count
```

### Methods to implement

#### `__init__(self, start=0)`
Store `start` in `self.count`.

#### `increment(self)`
Add `1` to `self.count`.

#### `decrement(self)`
Subtract `1` from `self.count`.

#### `reset(self)`
Set `self.count` back to `0`.

#### `get_value(self) -> int`
Return the current value of `self.count`.

---

## Unit Tests

### What are unit tests and why do they matter?
Tests are small automated checks — each one calls your function or method and verifies the result. When you run the test suite, Python automatically runs every check and reports which ones pass or fail. This is far faster and more reliable than testing by hand.

### How to run the tests

**Run only this week's tests:**
```bash
pytest assignments/week03_collections_classes/tests/ -v
```

**Run all assignments at once:**
```bash
pytest assignments/ -q
```

### What each test checks

| Test name | What it verifies |
|-----------|------------------|
| `test_get_unique_items_numbers` | `[3,1,2,1,3]` → `[1,2,3]` |
| `test_get_unique_items_strings` | `["b","a","b"]` → `["a","b"]` |
| `test_get_unique_items_already_unique` | `[1,2,3]` → `[1,2,3]` |
| `test_word_frequency_basic` | `["hi","bye","hi"]` → `{'hi':2,'bye':1}` |
| `test_word_frequency_empty` | `[]` → `{}` |
| `test_word_frequency_all_same` | `["a","a","a"]` → `{'a':3}` |
| `test_counter_default_start` | `Counter().count` is `0` |
| `test_counter_custom_start` | `Counter(10).count` is `10` |
| `test_counter_increment` | After one `increment()`, count is `1` |
| `test_counter_increment_twice` | After two `increment()` calls, count is `2` |
| `test_counter_decrement` | `Counter(5)` then `decrement()` → count `4` |
| `test_counter_reset` | `Counter(5)` then `reset()` → count `0` |
| `test_counter_get_value` | `Counter(7).get_value()` → `7` |

### Understanding the output
All 13 tests should pass when your implementation is correct. A `FAILED` line means a specific method returned the wrong result — check the assertion error to see what was expected versus what your code returned.
