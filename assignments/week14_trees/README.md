# Week 14: Trees

## Learning Objectives
- Implement binary search tree insertion.
- Traverse trees in multiple orders.
- Measure tree height.

## Assignment Instructions
Implement the starter functions and classes in `assignment.py`. Keep your changes inside this file only so the InsightHub platform can auto-detect completion safely.

## Functions to Implement
- `class TreeNode`
- `class BinarySearchTree`
- `def __init__(self) -> None`
- `def insert(self, value`
- `def _insert(node`
- `def search(self, value`
- `def inorder(self) -> list[int]`
- `def _walk(node`
- `def preorder(self) -> list[int]`
- `def _walk(node`
- `def postorder(self) -> list[int]`
- `def _walk(node`
- `def get_height(self) -> int`
- `def _height(node`

## Run Tests
```bash
pytest assignments/week14_trees/tests/
```

## Check Completion
```bash
python -c "from assignments.week14_trees.assignment import is_complete; print(is_complete())"
```
