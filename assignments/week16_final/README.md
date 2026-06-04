# Week 16: Final Portfolio Build

## Learning Objectives
- Summarize completion progress across all weeks.
- Generate resume-style bullet points from a skill list.
- Calculate a final letter grade from completed work.

## What You Need to Do
Open `assignment.py` and implement the three functions below.

---

### Task 1 — `generate_final_summary(progress)`
`progress` is a dictionary where keys are week numbers (integers) and values are dicts with a `"complete"` key (boolean).

Return a dictionary with:
- `"completed"`: how many weeks have `"complete"` equal to `True`.
- `"total"`: the total number of weeks in `progress`.

```python
progress = {1: {"complete": True}, 2: {"complete": False}, 3: {"complete": True}}
generate_final_summary(progress)
# → {"completed": 2, "total": 3}
```

**Hints:**
- Use a loop or `sum()` to count weeks where `item.get("complete")` is `True`.
- `"total"` = `len(progress)`.

---

### Task 2 — `create_resume_bullets(skills)`
Convert a list of skill names into resume-ready bullet strings.

Each bullet should follow this format:  
`"Applied {skill} in InsightHub portfolio work."`

```python
create_resume_bullets(["Python", "Sorting"])
# → ["Applied Python in InsightHub portfolio work.",
#    "Applied Sorting in InsightHub portfolio work."]
```

**Hint:** Use a list comprehension with an f-string.

---

### Task 3 — `calculate_final_grade(weeks_completed)`
Return a letter grade based on the percentage of 16 weeks completed.

| Percentage | Grade |
|------------|-------|
| ≥ 90%      | 'A'   |
| ≥ 80%      | 'B'   |
| ≥ 70%      | 'C'   |
| ≥ 60%      | 'D'   |
| < 60%      | 'F'   |

```python
calculate_final_grade(16)  # → 'A'  (100%)
calculate_final_grade(13)  # → 'B'  (81.25%)
calculate_final_grade(0)   # → 'F'
```

**Hints:**
- `percentage = (weeks_completed / 16) * 100`
- Use `if / elif / else` to return the right grade.

---

## Run Tests
```bash
pytest assignments/week16_final/tests/
```

All tests should pass once you complete each function.
