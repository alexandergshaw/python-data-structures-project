# Week 12: Algorithms and Data Structures Review

## Overview
You are halfway through the course. This week's assignment is short and intentional: it asks you to list the core topics you have covered and calculate a readiness score. The goal is not to challenge you algorithmically but to prompt self-reflection — what do you know well, and what needs more review before Test 2?

## Learning Objectives
- List the core topics covered so far.
- Calculate a readiness score based on how many topics you have reviewed.

## How to Open the Starter File
All your code goes in `assignment.py`.

```
week12_review/
├── assignment.py   ← edit this file
├── tests/
│   └── test_week12.py
└── README.md       ← you are here
```

---

## Topics covered so far

Before you start coding, take a moment to rate your comfort with each topic:

| # | Topic | Core idea | Confident? |
|---|-------|-----------|-----------|
| 1 | **Arrays** | Contiguous memory; O(1) index access | ☐ |
| 2 | **Linked Lists** | Nodes with pointers; O(1) front insert | ☐ |
| 3 | **Stacks** | LIFO — last in, first out | ☐ |
| 4 | **Queues** | FIFO — first in, first out | ☐ |
| 5 | **Searching** | Linear O(n) vs. Binary O(log n) | ☐ |
| 6 | **Sorting** | Bubble O(n²) vs. Merge/Quick O(n log n) | ☐ |

Any topic where you feel unsure deserves extra study time before Test 2.

---

## Task 1 — `review_checklist()`

### What it should do
Return a list containing all six topic strings. The order does not matter, but the strings must match exactly:

```python
review_checklist()
# → ['arrays', 'linked lists', 'stacks', 'queues', 'searching', 'sorting']
```

Required strings (case-sensitive):
- `'arrays'`
- `'linked lists'`
- `'stacks'`
- `'queues'`
- `'searching'`
- `'sorting'`

### Implementation hint
```python
def review_checklist():
    return ['arrays', 'linked lists', 'stacks', 'queues', 'searching', 'sorting']
```

---

## Task 2 — `score_readiness(completed_topics, total_topics=6)`

### What it should do
Calculate what percentage of the total topics you have completed.

```
score_readiness(3, 6)  →  50.0    (3/6 = 50%)
score_readiness(6, 6)  →  100.0   (all done)
score_readiness(0, 6)  →  0.0     (none done)
score_readiness(0, 0)  →  0.0     (edge case: no topics defined)
```

**Formula:** `(completed_topics / total_topics) * 100`

Return `0.0` if `total_topics` is `0` to avoid a `ZeroDivisionError`.

### Implementation hint
```python
def score_readiness(completed_topics, total_topics=6):
    if total_topics == 0:
        return 0.0
    return (completed_topics / total_topics) * 100
```

---

## Unit Tests

### What are unit tests and why do they matter?
Even for simple review assignments, tests ensure the exact strings and numeric outputs are correct. This week's tests specifically check that all six required topic strings are present and that the percentage formula handles the zero-total edge case without crashing.

### How to run the tests

**Run only this week's tests:**
```bash
pytest assignments/week12_review/tests/ -v
```

**Run all assignments at once:**
```bash
pytest assignments/ -q
```

### What each test checks

| Test name | What it verifies |
|-----------|------------------|
| `test_review_checklist_contains_arrays` | `'arrays'` is in the returned list |
| `test_review_checklist_contains_sorting` | `'sorting'` is in the returned list |
| `test_review_checklist_contains_all_six` | All six required strings are present |
| `test_score_readiness_half` | `score_readiness(3, 6)` → `50.0` |
| `test_score_readiness_full` | `score_readiness(6, 6)` → `100.0` |
| `test_score_readiness_zero_completed` | `score_readiness(0, 6)` → `0.0` |
| `test_score_readiness_zero_total` | `score_readiness(0, 0)` → `0.0` (no crash) |

### Understanding the output
All 7 tests should pass. Tip: if you misspell any topic string (e.g., `'linked_lists'` instead of `'linked lists'`), the checklist tests will fail. Copy the strings exactly from the specification above.
