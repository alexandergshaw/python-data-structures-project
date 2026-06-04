# Week 13: Test 2 Preparation

## Learning Objectives
- Summarize a list of scores with totals and averages.
- Identify the weakest area from a dictionary of scores.

## What You Need to Do
Open `assignment.py` and implement the two functions below.

---

### Task 1 — `evaluate_skills(scores)`
Given a list of numeric scores, return a dictionary with:
- `"total"`: the sum of all scores.
- `"average"`: the mean score (sum / count). Return `0.0` if the list is empty.

```python
evaluate_skills([80, 90])
# → {"total": 170, "average": 85.0}

evaluate_skills([])
# → {"total": 0, "average": 0.0}
```

**Hints:**
- `total = sum(scores)`.
- `average = total / len(scores) if scores else 0.0`.

---

### Task 2 — `next_study_topic(scores)`
Given a dictionary mapping topic names to integer scores, return the topic with the **lowest** score.

Return `'review'` if the dictionary is empty.

```python
next_study_topic({"trees": 70, "sorting": 60})  # → "sorting"
next_study_topic({})                              # → "review"
```

**Hints:**
- Use `min(scores, key=scores.get)` to find the key with the smallest value.
- Check if `scores` is empty first.

---

## Run Tests
```bash
pytest assignments/week13_test2/tests/
```

All tests should pass once you complete each function.
