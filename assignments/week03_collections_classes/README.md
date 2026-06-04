# Week 03: Collections and Classes

## Learning Objectives
- Remove duplicates with a `set` and sort a list.
- Count word occurrences with a dictionary.
- Build a simple class with an `__init__` and methods.

## What You Need to Do
Open `assignment.py` and implement the two functions and one class below.

---

### Task 1 — `get_unique_items(items)`
Return a **sorted** list containing each item only once.

```python
get_unique_items([3, 1, 2, 1, 3])  # → [1, 2, 3]
get_unique_items(["b", "a", "b"])  # → ['a', 'b']
```

**Hints:**
1. Convert `items` to a `set` to remove duplicates.
2. Wrap the result in `sorted()` to get a sorted list.

---

### Task 2 — `word_frequency(words)`
Given a list of words, return a dictionary mapping each word to its count.

```python
word_frequency(["hi", "bye", "hi"])  # → {'hi': 2, 'bye': 1}
word_frequency([])                   # → {}
```

**Hints:**
1. Start with `freq = {}`.
2. Loop over `words`.
3. For each word: `freq[word] = freq.get(word, 0) + 1`
4. Return `freq`.

---

### Task 3 — `Counter` class

A `Counter` keeps track of a running integer count.

#### `__init__(self, start=0)`
Store `start` in `self.count`.

#### `increment(self)`
Add `1` to `self.count`.

#### `decrement(self)`
Subtract `1` from `self.count`.

#### `reset(self)`
Set `self.count` back to `0`.

#### `get_value(self) -> int`
Return `self.count`.

```python
c = Counter()
c.increment()
c.increment()
c.get_value()   # → 2

c.decrement()
c.get_value()   # → 1

c.reset()
c.get_value()   # → 0

c2 = Counter(10)
c2.get_value()  # → 10
```

---

## Run Tests
```bash
pytest assignments/week03_collections_classes/tests/
```

All tests should pass once you complete each task.
