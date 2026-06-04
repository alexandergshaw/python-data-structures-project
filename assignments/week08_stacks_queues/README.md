# Week 08: Stacks and Queues

## Overview
Stacks and queues are two of the most widely used data structures in computing. They differ in exactly one way: the order in which items are removed. This week you build both from scratch and then model a simple data pipeline as a sequence of processing steps.

## Learning Objectives
- Implement a stack (Last-In, First-Out).
- Implement a queue (First-In, First-Out) using `collections.deque`.
- Model a simple data pipeline using a list of steps.

## Background

### Stack — LIFO (Last-In, First-Out)
Think of a stack of plates. You can only add or remove from the **top**. The last plate placed on top is the first one taken off.

```
push('a')   push('b')   push('c')   pop()    pop()
    ┌───┐       ┌───┐       ┌───┐             ┌───┐
    │ a │       │ b │  ┌───►│ c │◄── top      │ b │◄── top
    └───┘       │ a │  │    │ b │             │ a │
                └───┘  │    │ a │             └───┘
                       │    └───┘
                       └── removed 'c' first
```

Real-world uses: browser back button, undo/redo, function call stack.

### Queue — FIFO (First-In, First-Out)
Think of a checkout line. The first person to join is the first to be served.

```
enqueue('x')   enqueue('y')   enqueue('z')   dequeue()
  front                                        front
  ┌───┐          ┌───┬───┐      ┌───┬───┬───┐  ┌───┬───┐
  │ x │          │ x │ y │      │ x │ y │ z │  │ y │ z │
  └───┘          └───┴───┘      └───┴───┴───┘  └───┴───┘
                                                removed 'x' first
```

Real-world uses: print queues, task scheduling, breadth-first graph traversal.

## How to Open the Starter File
All your code goes in `assignment.py`. `collections.deque` is already imported.

```
week08_stacks_queues/
├── assignment.py   ← edit this file
├── tests/
│   └── test_week08.py
└── README.md       ← you are here
```

---

## Task 1 — `Stack` class

### What it should do

```python
s = Stack()
s.push('a')
s.push('b')
s.push('c')
s.pop()   # → 'c'   (last in, first out)
s.pop()   # → 'b'
s.pop()   # → 'a'
```

### Methods to implement

#### `__init__(self)`
Initialize `self.items = []`. The end of the list is the top of the stack.

#### `push(self, value)`
Add `value` to the top (end of the list):
```python
self.items.append(value)
```

#### `pop(self)`
Remove and return the top (last) item:
```python
return self.items.pop()
```

Python's `list.pop()` with no arguments removes and returns the **last** element, which is exactly the LIFO behavior we want.

---

## Task 2 — `Queue` class

### Why `collections.deque`?
A regular Python list can act as a queue, but removing from the front (`list.pop(0)`) requires shifting every remaining element — that is O(n). `deque` (double-ended queue) is optimized for fast appends and pops from **both** ends, making `popleft()` O(1).

### What it should do

```python
q = Queue()
q.enqueue('x')
q.enqueue('y')
q.dequeue()   # → 'x'   (first in, first out)
q.dequeue()   # → 'y'
```

### Methods to implement

#### `__init__(self)`
Initialize `self.items = deque()`.

#### `enqueue(self, value)`
Add `value` to the **back** of the queue:
```python
self.items.append(value)
```

#### `dequeue(self)`
Remove and return the item from the **front** of the queue:
```python
return self.items.popleft()
```

---

## Task 3 — `DataPipeline` class

### What it should do
A pipeline is a sequence of named processing steps that run in order. This class records those steps and returns them when the pipeline is "run".

```python
p = DataPipeline()
p.add_step('extract')
p.add_step('transform')
p.add_step('load')
p.run()   # → ['extract', 'transform', 'load']
```

An ETL (Extract → Transform → Load) pipeline is a classic pattern in data engineering.

### Methods to implement

#### `__init__(self)`
Initialize `self.steps = []`.

#### `add_step(self, step)`
Append the step name to `self.steps`:
```python
self.steps.append(step)
```

#### `run(self)`
Return a **copy** of `self.steps`. Returning a copy prevents callers from accidentally mutating the pipeline's internal list:
```python
return self.steps[:]   # slice with no bounds = full copy
```

---

## Unit Tests

### What are unit tests and why do they matter?
For LIFO/FIFO structures, the most important thing to test is **ordering**. The tests here verify that your stack pops in reverse insertion order and your queue dequeues in original insertion order. There is also a test that confirms `run()` returns a *copy* — modifying the returned list should not affect future `run()` calls.

### How to run the tests

**Run only this week's tests:**
```bash
pytest assignments/week08_stacks_queues/tests/ -v
```

**Run all assignments at once:**
```bash
pytest assignments/ -q
```

### What each test checks

| Test name | What it verifies |
|-----------|------------------|
| `test_stack_push_and_pop` | Push `'a'`, pop → `'a'` |
| `test_stack_lifo_order` | Push `'first'` then `'second'`; pop → `'second'` |
| `test_stack_push_multiple` | Push `1,2,3`; pop → `3` |
| `test_queue_enqueue_and_dequeue` | Enqueue `'x'`; dequeue → `'x'` |
| `test_queue_fifo_order` | Enqueue `'first'` then `'second'`; dequeue → `'first'` |
| `test_pipeline_add_and_run` | Add `'extract'`; `run()` → `['extract']` |
| `test_pipeline_multiple_steps` | Three steps; `run()` returns them all in order |
| `test_pipeline_run_returns_copy` | Mutating `run()`'s result doesn't affect the pipeline |

### Understanding the output
All 8 tests should pass. If `test_stack_lifo_order` fails, check that your `pop` calls `self.items.pop()` (removes from the end) and not `self.items.pop(0)` (which would make it a queue). If `test_pipeline_run_returns_copy` fails, return `self.steps[:]` instead of `self.steps`.
