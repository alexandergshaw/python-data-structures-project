# Week 16: Final Portfolio Build

## Learning Objectives
- Build a class with instance methods and control flow.
- Sort a list of objects by a computed attribute.
- Search a list using a linear scan.
- Write a recursive function with a base case.
- Summarize a collection of objects into a dictionary.

## What You Need to Do
Open `assignment.py` and implement the `Student` class and the four functions below. Each task draws on a different skill from the course.

---

### Task 1 — `Student` class (OOP)

A `Student` holds a name and a list of test scores.

#### `__init__(self, name, scores=None)`
- Store `name` as `self.name`.
- Store a **copy** of `scores` as `self.scores` (or `[]` when `scores` is `None`).

#### `add_score(self, score)`
- Append `score` to `self.scores`.

#### `get_average(self) -> float`
- Return the average of `self.scores`, or `0.0` if the list is empty.

#### `get_letter_grade(self) -> str`
Return a grade based on the average:

| Average | Grade |
|---------|-------|
| ≥ 90    | 'A'   |
| ≥ 80    | 'B'   |
| ≥ 70    | 'C'   |
| ≥ 60    | 'D'   |
| < 60    | 'F'   |

```python
s = Student("Alice", [80, 100])
s.get_average()       # → 90.0
s.get_letter_grade()  # → 'A'

s2 = Student("Bob")
s2.add_score(55)
s2.get_letter_grade() # → 'F'
```

---

### Task 2 — `sort_students(students)` (Sorting)
Return `students` sorted from **highest to lowest** average.

```python
a = Student("Alice", [90])
b = Student("Bob", [70])
c = Student("Carol", [80])
[s.name for s in sort_students([a, b, c])]
# → ['Alice', 'Carol', 'Bob']
```

**Hint:** Use `sorted()` with `key=lambda s: s.get_average()` and `reverse=True`.

---

### Task 3 — `find_student(students, name)` (Searching)
Return the first `Student` whose name matches `name`, or `None` if not found.

```python
find_student([a, b, c], "Bob").name  # → 'Bob'
find_student([a, b, c], "Zara")      # → None
```

**Hints:**
1. Loop over `students`.
2. If `student.name == name`, return that student immediately.
3. After the loop, `return None`.

---

### Task 4 — `sum_recursive(numbers)` (Recursion)
Return the sum of `numbers` using recursion. Do **not** use `sum()`.

```python
sum_recursive([1, 2, 3, 4])  # → 10
sum_recursive([])             # → 0
```

**Hints:**
- **Base case:** if `numbers` is empty, return `0`.
- **Recursive case:** `return numbers[0] + sum_recursive(numbers[1:])`

---

### Task 5 — `grade_distribution(students)` (Collections)
Return a dictionary counting how many students earned each letter grade.
Only include grades that appear at least once.

```python
a = Student("Alice", [95])   # 'A'
b = Student("Bob",   [85])   # 'B'
c = Student("Carol", [92])   # 'A'
grade_distribution([a, b, c])
# → {'A': 2, 'B': 1}
```

**Hints:**
1. Start with `dist = {}`.
2. Loop over students.
3. `dist[grade] = dist.get(grade, 0) + 1`

---

## Run Tests
```bash
pytest assignments/week16_final/tests/
```

All tests should pass once you complete each task.
