# Week 16: Final Portfolio Build

## Overview
This is the capstone assignment. You will implement a `Student` class and four standalone functions that together showcase every major skill from the course: OOP, sorting, searching, recursion, and working with collections. Completing this assignment demonstrates that you can apply these concepts in a realistic, integrated scenario.

## Learning Objectives
- Build a class with instance methods and control flow.
- Sort a list of objects by a computed attribute.
- Search a list using a linear scan.
- Write a recursive function with a base case.
- Summarize a collection of objects into a dictionary.

## How to Open the Starter File
All your code goes in `assignment.py`.

```
week16_final/
├── assignment.py   ← edit this file
├── tests/
│   └── test_week16.py
└── README.md       ← you are here
```

---

## Task 1 — `Student` class (OOP)

### What it should do
A `Student` stores a name and a list of test scores. It can compute its own average grade and convert that average to a letter grade.

```python
s = Student("Alice", [80, 100])
s.get_average()       # → 90.0
s.get_letter_grade()  # → 'A'

s2 = Student("Bob")       # no scores to start
s2.add_score(55)
s2.get_letter_grade()     # → 'F'
```

### Methods to implement

#### `__init__(self, name, scores=None)`
Store `name` as `self.name`. Store a **copy** of `scores` as `self.scores` (use `[]` when `scores` is `None`):

```python
self.name = name
self.scores = list(scores) if scores is not None else []
```

Storing a copy (not the original list) prevents the caller from accidentally mutating the student's scores.

#### `add_score(self, score)`
Append a new score to `self.scores`:
```python
self.scores.append(score)
```

#### `get_average(self) -> float`
Return the mean of all scores, or `0.0` for an empty list:
```python
return sum(self.scores) / len(self.scores) if self.scores else 0.0
```

#### `get_letter_grade(self) -> str`
Convert the average to a letter grade:

```
Average ≥ 90  →  'A'
Average ≥ 80  →  'B'
Average ≥ 70  →  'C'
Average ≥ 60  →  'D'
Average < 60  →  'F'
```

```
90 ─────────────────────────── A
80 ─────────────────────────── B
70 ─────────────────────────── C
60 ─────────────────────────── D
 0 ─────────────────────────── F
```

Check boundaries from highest to lowest:
```python
avg = self.get_average()
if avg >= 90: return 'A'
if avg >= 80: return 'B'
if avg >= 70: return 'C'
if avg >= 60: return 'D'
return 'F'
```

---

## Task 2 — `sort_students(students)` (Sorting)

### What it should do
Return the list of students sorted from **highest average to lowest average**.

```python
a = Student("Alice", [90])
b = Student("Bob",   [70])
c = Student("Carol", [80])

sorted_names = [s.name for s in sort_students([a, b, c])]
# → ['Alice', 'Carol', 'Bob']   (90 > 80 > 70)
```

### Implementation hint
`sorted()` with `reverse=True` gives descending order:
```python
def sort_students(students):
    return sorted(students, key=lambda s: s.get_average(), reverse=True)
```

---

## Task 3 — `find_student(students, name)` (Searching)

### What it should do
Perform a linear scan and return the first `Student` whose `name` matches, or `None` if not found.

```python
find_student([a, b, c], "Bob").name   # → 'Bob'
find_student([a, b, c], "Zara")       # → None
```

### Implementation hint
```python
def find_student(students, name):
    for student in students:
        if student.name == name:
            return student
    return None
```

---

## Task 4 — `sum_recursive(numbers)` (Recursion)

### What it should do
Return the sum of `numbers` using recursion. Do **not** use Python's built-in `sum()`.

```
sum_recursive([1, 2, 3, 4])
= 1 + sum_recursive([2, 3, 4])
        = 2 + sum_recursive([3, 4])
                = 3 + sum_recursive([4])
                        = 4 + sum_recursive([])
                                  = 0  ← base case
                        = 4 + 0 = 4
                = 3 + 4 = 7
        = 2 + 7 = 9
= 1 + 9 = 10  ✓
```

### Implementation hint
```python
def sum_recursive(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])
```

---

## Task 5 — `grade_distribution(students)` (Collections)

### What it should do
Return a dictionary counting how many students earned each letter grade. Only include grades that appear at least once.

```python
a = Student("Alice", [95])   # 'A'
b = Student("Bob",   [85])   # 'B'
c = Student("Carol", [92])   # 'A'

grade_distribution([a, b, c])
# → {'A': 2, 'B': 1}
```

### Implementation hint
Use the frequency-counting pattern from Week 3:
```python
def grade_distribution(students):
    dist = {}
    for student in students:
        grade = student.get_letter_grade()
        dist[grade] = dist.get(grade, 0) + 1
    return dist
```

---

## Unit Tests

### What are unit tests and why do they matter?
The final assignment has the most tests of any week — 23 in total — because it combines all previous concepts. Tests verify each `Student` method individually, then each standalone function with multiple inputs including edge cases (empty list, student not found, all same grade). Running the full test suite tells you at a glance which parts of your implementation are correct and which still need work.

### How to run the tests

**Run only this week's tests:**
```bash
pytest assignments/week16_final/tests/ -v
```

**Run all assignments at once** (great for a final check):
```bash
pytest assignments/ -q
```

**Run with detailed output on failures:**
```bash
pytest assignments/week16_final/tests/ -v --tb=short
```

### What each test checks

| Test name | What it verifies |
|-----------|------------------|
| `test_student_name_stored` | `Student("Alice").name == "Alice"` |
| `test_student_scores_default_empty` | No scores → `self.scores == []` |
| `test_student_scores_stored` | `Student("Alice", [80,90]).scores == [80,90]` |
| `test_student_add_score` | `add_score(95)` → `scores == [95]` |
| `test_student_get_average_basic` | `[80,100]` → average `90.0` |
| `test_student_get_average_empty` | No scores → average `0.0` |
| `test_student_get_letter_grade_a` | Average 95 → `'A'` |
| `test_student_get_letter_grade_b` | Average 85 → `'B'` |
| `test_student_get_letter_grade_c` | Average 75 → `'C'` |
| `test_student_get_letter_grade_d` | Average 65 → `'D'` |
| `test_student_get_letter_grade_f` | Average 50 → `'F'` |
| `test_sort_students_order` | Alice(90) > Carol(80) > Bob(70) |
| `test_sort_students_length` | Sorted list has same length as input |
| `test_find_student_found` | Finds Bob by name; returns same object |
| `test_find_student_not_found` | Unknown name → `None` |
| `test_sum_recursive_basic` | `[1,2,3,4]` → `10` |
| `test_sum_recursive_empty` | `[]` → `0` |
| `test_sum_recursive_single` | `[5]` → `5` |
| `test_grade_distribution_basic` | 2 A's + 1 B → `{'A':2,'B':1}` |
| `test_grade_distribution_empty` | No students → `{}` |
| `test_grade_distribution_all_same` | 3 A students → `{'A':3}` |

### Understanding the output
All 21 tests above plus the 2 infrastructure tests (`test_is_complete_returns_boolean`, `test_get_week_summary_type`) should pass — 23 total. Use the verbose `-v` flag to see each test name as it passes or fails, which makes debugging much easier.

**Common pitfalls to watch for:**
- `test_student_scores_default_empty`: if you write `self.scores = scores or []`, then passing `[]` explicitly would also trigger the fallback. Use `if scores is not None` instead.
- `test_sort_students_order`: make sure you sort by `get_average()` descending (`reverse=True`), not ascending.
- `test_sum_recursive_empty`: don't forget the base case or Python will raise a `RecursionError`.

---

## Congratulations!
Completing this final assignment means you have implemented: variables, control flow, collections, classes, Big O analysis, arrays, linked lists, stacks, queues, recursion, searching, sorting, trees, inheritance, and polymorphism. That is the full data structures and algorithms curriculum — well done!
