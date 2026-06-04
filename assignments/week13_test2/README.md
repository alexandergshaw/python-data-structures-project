# Week 13: Test 2 Preparation

## Overview
Test 2 covers everything from Week 6 onwards: Big O, arrays, linked lists, stacks, queues, searching, sorting, and recursion. This assignment focuses on two targeted practice tasks — summarizing a list of scores and identifying which topic needs the most attention — skills you will need both on the test and when analyzing real data.

## Learning Objectives
- Summarize a list of scores with totals and averages.
- Identify the weakest area from a dictionary of scores.

## How to Open the Starter File
All your code goes in `assignment.py`.

```
week13_test2/
├── assignment.py   ← edit this file
├── tests/
│   └── test_week13.py
└── README.md       ← you are here
```

---

## Quick review: concepts for Test 2

Before coding, briefly recall these concepts. If any feel shaky, revisit the corresponding week's assignment.

| Week | Concept | Key fact |
|------|---------|---------|
| 6 | Big O | O(1) < O(log n) < O(n) < O(n²) |
| 7 | Arrays & Linked Lists | Array: O(1) access; LL: O(1) front insert |
| 8 | Stacks & Queues | Stack: LIFO; Queue: FIFO |
| 9 | Recursion | Always need a base case |
| 10 | Searching | Linear: any list; Binary: sorted list only |
| 11 | Sorting | Bubble O(n²); Merge/Quick O(n log n) |

---

## Task 1 — `evaluate_skills(scores)`

### What it should do
Given a list of numeric scores, return a dictionary summarizing them.

```python
evaluate_skills([80, 90])
# → {"total": 170, "average": 85.0}

evaluate_skills([100])
# → {"total": 100, "average": 100.0}

evaluate_skills([])
# → {"total": 0, "average": 0.0}   ← guard against empty list
```

| Key | Formula |
|-----|---------|
| `"total"` | `sum(scores)` |
| `"average"` | `sum(scores) / len(scores)`, or `0.0` if the list is empty |

### Edge case: empty list
`sum([])` is `0` (safe), but `0 / 0` raises a `ZeroDivisionError`. Guard against it:

```python
average = total / len(scores) if scores else 0.0
```

### Implementation hint
```python
def evaluate_skills(scores):
    total = sum(scores)
    average = total / len(scores) if scores else 0.0
    return {"total": total, "average": average}
```

---

## Task 2 — `next_study_topic(scores)`

### What it should do
Given a dictionary mapping topic names to integer scores, return the topic name with the **lowest** score. Return `'review'` if the dictionary is empty.

```python
next_study_topic({"trees": 70, "sorting": 60})  →  "sorting"
next_study_topic({"recursion": 50})              →  "recursion"
next_study_topic({})                              →  "review"
```

### Key concept: `min()` with a key function
`min(dictionary)` returns the key with the lowest value when you pass `key=dictionary.get`:

```python
scores = {"trees": 70, "sorting": 60}
min(scores, key=scores.get)
# → "sorting"  (because scores.get("sorting") = 60 is the minimum)
```

This is equivalent to asking: "which topic has the smallest score value?"

### Implementation hint
```python
def next_study_topic(scores):
    if not scores:
        return 'review'
    return min(scores, key=scores.get)
```

---

## Unit Tests

### What are unit tests and why do they matter?
These tests double as practice problems for the test. They check that `evaluate_skills` handles both the normal case and the empty-list edge case, and that `next_study_topic` correctly identifies the minimum-score topic and handles an empty input safely.

### How to run the tests

**Run only this week's tests:**
```bash
pytest assignments/week13_test2/tests/ -v
```

**Run all assignments at once:**
```bash
pytest assignments/ -q
```

### What each test checks

| Test name | Input(s) | Expected output |
|-----------|----------|-----------------|
| `test_evaluate_skills_average` | `[80, 90]` | `average == 85.0` |
| `test_evaluate_skills_total` | `[80, 90]` | `total == 170` |
| `test_evaluate_skills_empty` | `[]` | `total == 0`, `average == 0.0` |
| `test_next_study_topic_lowest` | `{"trees":70,"sorting":60}` | `"sorting"` |
| `test_next_study_topic_single` | `{"recursion":50}` | `"recursion"` |
| `test_next_study_topic_empty` | `{}` | `"review"` |

### Understanding the output
All 6 tests should pass. If `test_evaluate_skills_empty` raises a `ZeroDivisionError`, add the `if scores else 0.0` guard. If `test_next_study_topic_empty` fails, make sure you check `if not scores` before calling `min()`.
