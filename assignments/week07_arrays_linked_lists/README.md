# Week 07: Arrays and Linked Lists

## Overview
This week you implement two fundamental data structures from scratch: a **dynamic array** (a thin wrapper around Python's list) and a **singly linked list**. Understanding these structures is the foundation for everything else in the course — stacks, queues, trees, and more all build on these concepts.

## Learning Objectives
- Build a simple wrapper around Python's list (dynamic array).
- Implement a singly linked list with nodes.
- Traverse a linked list and convert it to a plain list.

## Background

### Arrays vs. Linked Lists

```
Array (contiguous memory):
┌────┬────┬────┬────┬────┐
│ 10 │ 20 │ 30 │ 40 │ 50 │
└────┴────┴────┴────┴────┘
  [0]  [1]  [2]  [3]  [4]
 → Access by index in O(1): arr[2] → 30

Linked List (nodes with pointers):
┌──────────┐    ┌──────────┐    ┌──────────┐
│ val: 10  │───▶│ val: 20  │───▶│ val: 30  │───▶ None
│ next: ───┘    │ next: ───┘    │ next: None│
└──────────┘    └──────────┘    └──────────┘
  (head)
 → No index access; must traverse from head
 → But inserting at the front is O(1)
```

| Operation | Array | Linked List |
|-----------|-------|-------------|
| Access by index | O(1) | O(n) |
| Insert at end | O(1) amortized | O(n) — must walk to end |
| Insert at front | O(n) — must shift | O(1) |
| Memory layout | Contiguous | Scattered (via pointers) |

## How to Open the Starter File
All your code goes in `assignment.py`. A `Node` dataclass is already provided — do not modify it.

```
week07_arrays_linked_lists/
├── assignment.py   ← edit this file
├── tests/
│   └── test_week07.py
└── README.md       ← you are here
```

---

## Task 1 — `DynamicArray` class

### What it should do
Wrap Python's built-in list so it behaves like a simple dynamic array with append and length operations.

```python
arr = DynamicArray()
len(arr)      # → 0

arr.append(10)
arr.append(20)
len(arr)      # → 2
arr.items[0]  # → 10
```

### Methods to implement

#### `__init__(self)`
Initialize `self.items` as an empty Python list:
```python
self.items = []
```

#### `append(self, value)`
Add `value` to the end of `self.items`:
```python
self.items.append(value)
```

#### `__len__(self)`
Return the number of items stored. Python calls `__len__` automatically when you write `len(arr)`:
```python
return len(self.items)
```

---

## Task 2 — `Node` dataclass (already provided)

A `Node` holds a single value and an optional reference to the next node:

```python
@dataclass
class Node:
    value: any
    next: 'Node' = None   # pointer to the next node, or None at the tail
```

You do **not** need to change this. Just use `Node(value)` to create new nodes.

---

## Task 3 — `LinkedList` class

### What it should do
A singly linked list where you can append items and read them back as a plain list.

```python
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.to_list()  # → [1, 2, 3]
ll.head.value # → 1
```

### Methods to implement

#### `__init__(self)`
Initialize `self.head = None`. An empty list has no head node.

#### `append(self, value)`
Create a new `Node(value)` and attach it at the **end** of the chain:

```
Before append(4):   1 → 2 → 3 → None
After  append(4):   1 → 2 → 3 → 4 → None
                                 ↑
                           new node goes here
```

Steps:
1. If `self.head is None`, this is the first node: `self.head = Node(value)` and return.
2. Otherwise, walk the chain until you find the node where `current.next is None`.
3. Set `current.next = Node(value)`.

```python
def append(self, value):
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
        return
    current = self.head
    while current.next is not None:
        current = current.next
    current.next = new_node
```

#### `to_list(self)`
Traverse the chain from `head` to tail, collecting each value into a Python list:

```
Walk:  head → node(1) → node(2) → node(3) → None
              ↓          ↓          ↓
result:      [1,         2,         3]
```

```python
def to_list(self):
    result = []
    current = self.head
    while current is not None:
        result.append(current.value)
        current = current.next
    return result
```

---

## Unit Tests

### What are unit tests and why do they matter?
Tests for data structures check both the *interface* (do the right methods exist?) and the *behavior* (do they produce the correct output?). For linked lists, tests also verify internal structure — for example, that `head.value` is set correctly after the first append.

### How to run the tests

**Run only this week's tests:**
```bash
pytest assignments/week07_arrays_linked_lists/tests/ -v
```

**Run all assignments at once:**
```bash
pytest assignments/ -q
```

### What each test checks

| Test name | What it verifies |
|-----------|------------------|
| `test_dynamic_array_starts_empty` | `len(DynamicArray())` is `0` |
| `test_dynamic_array_append_one` | After one append, `len` is `1` |
| `test_dynamic_array_append_multiple` | After three appends, `len` is `3` |
| `test_dynamic_array_items_stored` | `arr.items[0]` holds the appended value |
| `test_linked_list_starts_empty` | `LinkedList().to_list()` is `[]` |
| `test_linked_list_append_one` | `to_list()` returns `[1]` after appending `1` |
| `test_linked_list_append_multiple` | `to_list()` returns `[1,2,3]` in order |
| `test_linked_list_head_value` | `head.value` is `99` after appending `99` |

### Understanding the output
All 8 tests should pass. A common mistake is forgetting the empty-list case in `append` — if `self.head is None` and you try to walk the chain, you will get an `AttributeError`. Always check for `None` first.
