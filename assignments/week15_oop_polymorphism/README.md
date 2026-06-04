# Week 15: OOP and Polymorphism

## Overview
Object-Oriented Programming (OOP) is a paradigm that organizes code around objects — data and the methods that operate on it bundled together. This week you explore two of OOP's most powerful features: **inheritance** (sharing behavior between classes) and **polymorphism** (calling the same method on different objects and getting different results).

## Learning Objectives
- Use class inheritance to share behavior.
- Override a method in a subclass (polymorphism).
- Produce different output from objects of different types.

## Background

### Inheritance
A **child class** (subclass) inherits all attributes and methods from its **parent class** (superclass). It can then add new behavior or override existing behavior.

```
AnalyticsReport (parent)
│  __init__(title)
│  render() → "Analytics Report: {title}"
│
├── KPIReport (child)
│     render() → "KPI Report: {title}"     ← overrides parent
│
├── VisualizationReport (child)
│     render() → "Visualization Report: {title}"
│
└── RecommendationReport (child)
      render() → "Recommendation Report: {title}"
```

All four classes share the same `__init__` (inherited from `AnalyticsReport`) but each calls `render()` differently. That is polymorphism.

### Polymorphism in action
```python
reports = [
    AnalyticsReport("Q1"),
    KPIReport("Revenue"),
    VisualizationReport("Trend"),
    RecommendationReport("Next Steps"),
]

for report in reports:
    print(report.render())   # ← same method call, different output!

# Analytics Report: Q1
# KPI Report: Revenue
# Visualization Report: Trend
# Recommendation Report: Next Steps
```

This is the power of polymorphism: you can process a collection of different object types through a common interface.

## How to Open the Starter File
All your code goes in `assignment.py`.

```
week15_oop_polymorphism/
├── assignment.py   ← edit this file
├── tests/
│   └── test_week15.py
└── README.md       ← you are here
```

---

## Task 1 — `AnalyticsReport` (base class)

### What it should do
The base class stores a title and knows how to render itself as a string.

```python
AnalyticsReport("Overview").render()
# → "Analytics Report: Overview"
```

### Methods to implement

#### `__init__(self, title)`
Store `title` as `self.title`:
```python
def __init__(self, title):
    self.title = title
```

#### `render(self) -> str`
Return the formatted report string:
```python
def render(self) -> str:
    return f"Analytics Report: {self.title}"
```

---

## Task 2 — `KPIReport(AnalyticsReport)` (subclass)

### What it should do
Inherit from `AnalyticsReport`. Override only `render()` — you do **not** need to re-write `__init__`, because Python automatically uses the parent's `__init__`.

```python
KPIReport("Revenue").render()
# → "KPI Report: Revenue"
KPIReport("Revenue").title
# → "Revenue"   ← inherited from AnalyticsReport.__init__
```

### How to inherit
```python
class KPIReport(AnalyticsReport):      # ← specify parent in parentheses
    def render(self) -> str:
        return f"KPI Report: {self.title}"
```

---

## Task 3 — `VisualizationReport(AnalyticsReport)` (subclass)

Override `render()` to return `f"Visualization Report: {self.title}"`.

```python
VisualizationReport("Trend").render()
# → "Visualization Report: Trend"
```

---

## Task 4 — `RecommendationReport(AnalyticsReport)` (subclass)

Override `render()` to return `f"Recommendation Report: {self.title}"`.

```python
RecommendationReport("Next Steps").render()
# → "Recommendation Report: Next Steps"
```

---

## Unit Tests

### What are unit tests and why do they matter?
These tests verify both individual class behavior *and* the polymorphism contract. `test_polymorphism_different_outputs` specifically checks that all four `render()` calls produce distinct strings — if two classes accidentally produce the same output, that test fails and highlights the mistake.

### How to run the tests

**Run only this week's tests:**
```bash
pytest assignments/week15_oop_polymorphism/tests/ -v
```

**Run all assignments at once:**
```bash
pytest assignments/ -q
```

### What each test checks

| Test name | What it verifies |
|-----------|------------------|
| `test_analytics_report_title_stored` | `AnalyticsReport('Overview').title == 'Overview'` |
| `test_analytics_report_render` | Returns `'Analytics Report: Overview'` |
| `test_kpi_report_render` | Returns `'KPI Report: Revenue'` |
| `test_kpi_report_has_title` | `KPIReport('Revenue').title == 'Revenue'` (inherited `__init__`) |
| `test_visualization_report_render` | Returns `'Visualization Report: Trend'` |
| `test_recommendation_report_render` | Returns `'Recommendation Report: Next Steps'` |
| `test_polymorphism_different_outputs` | All four `render()` calls produce different strings |

### Understanding the output
All 7 tests should pass. The most common mistake is forgetting to specify the parent class: `class KPIReport:` (no parent) means the class won't inherit `__init__`, and `KPIReport("Revenue").title` will raise an `AttributeError`. Always write `class KPIReport(AnalyticsReport):`.
