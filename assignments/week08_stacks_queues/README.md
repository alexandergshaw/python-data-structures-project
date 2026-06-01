# Week 08: Stacks and Queues

## Learning Objectives
- Implement stack behavior.
- Implement queue behavior.
- Model a simple data pipeline.

## Assignment Instructions
Implement the starter functions and classes in `assignment.py`. Keep your changes inside this file only so the InsightHub platform can auto-detect completion safely.

## Functions to Implement
- `class Stack`
- `def __init__(self) -> None`
- `def push(self, value`
- `def pop(self) -> Any`
- `class Queue`
- `def __init__(self) -> None`
- `def enqueue(self, value`
- `def dequeue(self) -> Any`
- `class DataPipeline`
- `def __init__(self) -> None`
- `def add_step(self, step`
- `def run(self) -> list[str]`

## Run Tests
```bash
pytest assignments/week08_stacks_queues/tests/
```

## Check Completion
```bash
python -c "from assignments.week08_stacks_queues.assignment import is_complete; print(is_complete())"
```
