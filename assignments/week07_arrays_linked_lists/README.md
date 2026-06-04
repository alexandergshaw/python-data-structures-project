# Week 07: Arrays and Linked Lists

## Learning Objectives
- Build a simple wrapper around Python's list (dynamic array).
- Implement a singly linked list with nodes.
- Traverse a linked list and convert it to a plain list.

## Background
Arrays store items in contiguous memory. Linked lists store items in *nodes*, where each node holds a value and a reference (pointer) to the next node. This week you implement both.

## What You Need to Do
Open `assignment.py` and implement the two data structures below.

---

### Task 1 — `DynamicArray` class

#### `__init__(self)`
Initialize `self.items` as an empty Python list (`[]`).

#### `append(self, value)`
Add `value` to the end of `self.items`.

#### `__len__(self)`
Return the number of items stored.

```python
arr = DynamicArray()
arr.append(10)
arr.append(20)
len(arr)  # → 2
```

---

### Task 2 — `Node` dataclass (already provided)
A `Node` has a `value` and an optional `next` pointer. **No changes needed here.**

---

### Task 3 — `LinkedList` class

#### `__init__(self)`
Initialize `self.head` to `None` (the list starts empty).

#### `append(self, value)`
Create a new `Node(value)` and add it at the **end** of the list.

**Hints for append:**
1. If `self.head is None`, set `self.head = Node(value)` and return.
2. Otherwise, walk the list until you find the node where `current.next is None`.
3. Set `current.next = Node(value)`.

#### `to_list(self)`
Return a plain Python list of all values in order from head to tail.

**Hints for to_list:**
1. Start at `self.head`.
2. While `current` is not `None`, add `current.value` to your result list and advance `current = current.next`.
3. Return the result list.

```python
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.to_list()  # → [1, 2, 3]
```

---

## Run Tests
```bash
pytest assignments/week07_arrays_linked_lists/tests/
```

All tests should pass once you complete each data structure.
