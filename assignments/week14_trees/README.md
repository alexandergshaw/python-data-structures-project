# Week 14: Trees

## Overview
Trees are hierarchical data structures where each element (node) can have children. The **Binary Search Tree (BST)** is the most fundamental: it keeps values organized so that searching, inserting, and in many cases sorting are all efficient. This week you build a full BST from scratch, including three traversal orders and a height calculation.

## Learning Objectives
- Insert values into a Binary Search Tree (BST).
- Traverse a BST in inorder, preorder, and postorder.
- Measure the height of a tree.

## Background

### BST structure
Every node satisfies one invariant:
- **Left child** holds a value **smaller** than the current node.
- **Right child** holds a value **larger** than the current node.

```
         Insert: 10, 5, 15, 12, 3

                  10          ← root
                 /  \
                5    15
               /    /
              3    12

 Values left of 10:  3, 5  (all < 10)  ✓
 Values right of 10: 12, 15 (all > 10) ✓
```

### Traversal orders
The order in which you visit nodes is called a **traversal**:

```
Tree:          10
              /  \
             5    15
            /    /
           3    12

Inorder   (left → node → right):  3, 5, 10, 12, 15   ← always ascending!
Preorder  (node → left → right): 10, 5, 3, 15, 12    ← root first
Postorder (left → right → node):  3, 5, 12, 15, 10   ← root last
```

Inorder traversal of a BST always produces values in ascending sorted order — that is a useful property.

### Tree height
Height = the number of edges on the longest path from root to a leaf. In this implementation we count nodes rather than edges, so an empty tree has height 0 and a single-node tree has height 1.

```
         10          height = 3 (10 → 5 → 3)
        /  \
       5    15
      /
     3
```

## How to Open the Starter File
All your code goes in `assignment.py`. A `TreeNode` dataclass is already provided — do not modify it.

```
week14_trees/
├── assignment.py   ← edit this file
├── tests/
│   └── test_week14.py
└── README.md       ← you are here
```

---

## Task 1 — `insert(self, value)`

### What it should do
Add `value` to the correct position in the BST.

### Algorithm
Use a recursive helper `_insert(node, value)`:

```
_insert(node, value):
  if node is None:
      return TreeNode(value)        ← create a new leaf
  if value < node.value:
      node.left = _insert(node.left, value)   ← go left
  elif value > node.value:
      node.right = _insert(node.right, value) ← go right
  return node                                  ← return unchanged node

self.root = _insert(self.root, value)
```

Duplicate values are ignored (neither `<` nor `>` branches are taken).

---

## Task 2 — `search(self, value) → bool`

### What it should do
Return `True` if `value` exists in the tree, `False` otherwise.

```python
tree.insert(10); tree.insert(5); tree.insert(15); tree.insert(12)
tree.search(12)   # → True
tree.search(99)   # → False
```

### Algorithm
Walk the tree iteratively. At each node, compare `value` to `current.value`:

```
Start at root (10)
  12 > 10 → go right to 15
  12 < 15 → go left to 12
  12 == 12 → return True  ✓
```

```python
def search(self, value):
    current = self.root
    while current is not None:
        if current.value == value:
            return True
        elif value < current.value:
            current = current.left
        else:
            current = current.right
    return False
```

---

## Task 3 — `inorder(self) → list[int]`

### What it should do
Return all values in ascending order (left → node → right).

```python
tree.inorder()  # → [5, 10, 12, 15]  (given tree above)
```

### Recursive helper pattern
```python
def inorder(self):
    def _walk(node):
        if node is None:
            return []
        return _walk(node.left) + [node.value] + _walk(node.right)
    return _walk(self.root)
```

---

## Task 4 — `preorder(self) → list[int]`
Return values in preorder: node → left → right.

```python
def _walk(node):
    if node is None:
        return []
    return [node.value] + _walk(node.left) + _walk(node.right)
```

---

## Task 5 — `postorder(self) → list[int]`
Return values in postorder: left → right → node.

```python
def _walk(node):
    if node is None:
        return []
    return _walk(node.left) + _walk(node.right) + [node.value]
```

---

## Task 6 — `get_height(self) → int`

### What it should do
Return the height of the tree. An empty tree has height `0`; a single-node tree has height `1`.

```python
tree = BinarySearchTree()
tree.get_height()    # → 0

tree.insert(10)
tree.get_height()    # → 1

tree.insert(5); tree.insert(15); tree.insert(12)
tree.get_height()    # → 3  (10 → 15 → 12)
```

### Recursive helper
```python
def get_height(self):
    def _height(node):
        if node is None:
            return 0
        return 1 + max(_height(node.left), _height(node.right))
    return _height(self.root)
```

---

## Unit Tests

### What are unit tests and why do they matter?
BST tests verify both the structure (does `root.value` equal the first inserted value?) and behavior (does `inorder` produce sorted output? does `postorder` always end with the root?). Testing traversals separately ensures each one visits nodes in the correct sequence.

### How to run the tests

**Run only this week's tests:**
```bash
pytest assignments/week14_trees/tests/ -v
```

**Run all assignments at once:**
```bash
pytest assignments/ -q
```

### What each test checks

| Test name | What it verifies |
|-----------|------------------|
| `test_insert_root` | After inserting `10`, `tree.root.value == 10` |
| `test_search_found` | `search(12)` returns `True` for `[10,5,15,12]` |
| `test_search_not_found` | `search(99)` returns `False` |
| `test_inorder_sorted` | `inorder()` → `[5,10,12,15]` (ascending) |
| `test_preorder_root_first` | `preorder()[0]` is the root value (`10`) |
| `test_postorder_root_last` | `postorder()[-1]` is the root value (`10`) |
| `test_get_height_empty` | Empty tree → height `0` |
| `test_get_height_single` | Single node → height `1` |
| `test_get_height_multi` | `[10,5,15,12]` → height `>= 2` |

### Understanding the output
All 9 tests should pass. If `test_inorder_sorted` fails, check that your inorder helper uses the pattern `left + [node] + right` (not `right + [node] + left`, which would give descending order).
