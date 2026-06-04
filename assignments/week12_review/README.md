# Week 12: Algorithms and Data Structures Review

## Learning Objectives
- List the core topics covered so far.
- Calculate a readiness score based on how many topics you have reviewed.

## What You Need to Do
Open `assignment.py` and implement the two functions below.

---

### Task 1 — `review_checklist()`
Return a list of topic strings that represent the key subjects covered this semester.

The list must contain these six strings (in any order):
`'arrays'`, `'linked lists'`, `'stacks'`, `'queues'`, `'searching'`, `'sorting'`

```python
review_checklist()
# → ['arrays', 'linked lists', 'stacks', 'queues', 'searching', 'sorting']
```

**Hint:** Just return a list literal with the six strings.

---

### Task 2 — `score_readiness(completed_topics, total_topics=6)`
Return the percentage of topics completed as a float.

Formula: `(completed_topics / total_topics) * 100`

Return `0.0` if `total_topics` is `0`.

```python
score_readiness(3, 6)  # → 50.0
score_readiness(6, 6)  # → 100.0
score_readiness(0, 6)  # → 0.0
```

**Hint:** Divide and multiply, but guard against `total_topics == 0`.

---

## Run Tests
```bash
pytest assignments/week12_review/tests/
```

All tests should pass once you complete each function.
