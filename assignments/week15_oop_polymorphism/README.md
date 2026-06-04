# Week 15: OOP and Polymorphism

## Learning Objectives
- Use class inheritance to share behavior.
- Override a method in a subclass (polymorphism).
- Produce different output from objects of different types.

## Background
**Inheritance** lets a child class reuse and extend a parent class.  
**Polymorphism** means you can call the same method (e.g., `render()`) on different objects and get different results.

## What You Need to Do
Open `assignment.py` and implement the four classes below.

---

### Task 1 — `AnalyticsReport` (base class)

#### `__init__(self, title)`
Store `title` as `self.title`.

#### `render(self) -> str`
Return `f"Analytics Report: {self.title}"`.

```python
AnalyticsReport("Overview").render()
# → "Analytics Report: Overview"
```

---

### Task 2 — `KPIReport(AnalyticsReport)` (subclass)
Inherit from `AnalyticsReport`.

Override `render(self)` to return `f"KPI Report: {self.title}"`.

```python
KPIReport("Revenue").render()
# → "KPI Report: Revenue"
```

**Hint:** You do **not** need to re-implement `__init__` — you get it for free from `AnalyticsReport`.

---

### Task 3 — `VisualizationReport(AnalyticsReport)` (subclass)
Override `render(self)` to return `f"Visualization Report: {self.title}"`.

---

### Task 4 — `RecommendationReport(AnalyticsReport)` (subclass)
Override `render(self)` to return `f"Recommendation Report: {self.title}"`.

---

## Run Tests
```bash
pytest assignments/week15_oop_polymorphism/tests/
```

All tests should pass once you complete each class.
