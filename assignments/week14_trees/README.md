# Week 14: Trees

## Learning Objectives
- Insert values into a Binary Search Tree (BST).
- Traverse a BST in inorder, preorder, and postorder.
- Measure the height of a tree.

## Background
A **Binary Search Tree** is a tree where:
- Every node has a value, a left child, and a right child.
- Values *smaller* than the current node go to the **left**.
- Values *larger* than the current node go to the **right**.

A `TreeNode` dataclass is already provided — do not modify it.

## What You Need to Do
Open `assignment.py` and implement the `BinarySearchTree` methods below.

---

### Task 1 — `insert(self, value)`
Insert `value` into the BST.

**Hints:**
1. Define a helper `_insert(node, new_value)`:
   - If `node is None`, return `TreeNode(new_value)`.
   - If `new_value < node.value`, set `node.left = _insert(node.left, new_value)`.
   - If `new_value > node.value`, set `node.right = _insert(node.right, new_value)`.
   - Return `node`.
2. Call `self.root = _insert(self.root, value)`.

---

### Task 2 — `search(self, value)` → bool
Return `True` if `value` exists in the tree, `False` otherwise.

**Hints:**
1. Start at `current = self.root`.
2. While `current` is not `None`:
   - If `current.value == value`: return `True`.
   - If `value < current.value`: go left (`current = current.left`).
   - Else: go right (`current = current.right`).
3. Return `False`.

---

### Task 3 — `inorder(self)` → list[int]
Return all values **in ascending order** (left → node → right).

```python
tree.insert(10); tree.insert(5); tree.insert(15)
tree.inorder()  # → [5, 10, 15]
```

**Hint:** Use a recursive helper `_walk(node)`:
- Return `[]` if `node is None`.
- Return `_walk(node.left) + [node.value] + _walk(node.right)`.

---

### Task 4 — `preorder(self)` → list[int]
Return values in preorder (node → left → right).

**Hint:** `[node.value] + _walk(node.left) + _walk(node.right)`.

---

### Task 5 — `postorder(self)` → list[int]
Return values in postorder (left → right → node).

**Hint:** `_walk(node.left) + _walk(node.right) + [node.value]`.

---

### Task 6 — `get_height(self)` → int
Return the height of the tree (0 for an empty tree).

**Hint:** Use a recursive helper `_height(node)`:
- Return `0` if `node is None`.
- Return `1 + max(_height(node.left), _height(node.right))`.

---

## Run Tests
```bash
pytest assignments/week14_trees/tests/
```

All tests should pass once you complete the class.
