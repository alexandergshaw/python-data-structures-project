# Week 15: OOP and Polymorphism

## Learning Objectives
- Use inheritance for multiple report types.
- Override summary behavior polymorphically.
- Model analytics outputs with classes.

## Assignment Instructions
Implement the starter functions and classes in `assignment.py`. Keep your changes inside this file only so the InsightHub platform can auto-detect completion safely.

## Functions to Implement
- `class AnalyticsReport`
- `def __init__(self, title`
- `def render(self) -> str`
- `class KPIReport(AnalyticsReport)`
- `def render(self) -> str`
- `class VisualizationReport(AnalyticsReport)`
- `def render(self) -> str`
- `class RecommendationReport(AnalyticsReport)`
- `def render(self) -> str`

## Run Tests
```bash
pytest assignments/week15_oop_polymorphism/tests/
```

## Check Completion
```bash
python -c "from assignments.week15_oop_polymorphism.assignment import is_complete; print(is_complete())"
```
