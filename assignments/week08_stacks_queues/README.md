# Week 08: Stacks and Queues

## Learning Objectives
- Implement a stack (Last-In, First-Out).
- Implement a queue (First-In, First-Out).
- Model a simple data pipeline using a list of steps.

## Background
- **Stack**: Items are added and removed from the *same* end (the top). Think of a stack of plates.
- **Queue**: Items are added at one end and removed from the other (like a checkout line).

## What You Need to Do
Open `assignment.py` and implement the three classes below.

---

### Task 1 — `Stack` class

#### `__init__(self)`
Initialize `self.items = []`.

#### `push(self, value)`
Add `value` to the top (end) of the stack.

#### `pop(self)`
Remove and return the top (last) item.

```python
s = Stack()
s.push('a')
s.push('b')
s.pop()  # → 'b'  (last in, first out)
s.pop()  # → 'a'
```

**Hints:**
- `push`: use `self.items.append(value)`.
- `pop`: use `self.items.pop()`.

---

### Task 2 — `Queue` class

Use Python's `collections.deque` for efficiency (already imported).

#### `__init__(self)`
Initialize `self.items = deque()`.

#### `enqueue(self, value)`
Add `value` to the back of the queue.

#### `dequeue(self)`
Remove and return the item from the front of the queue.

```python
q = Queue()
q.enqueue('x')
q.enqueue('y')
q.dequeue()  # → 'x'  (first in, first out)
```

**Hints:**
- `enqueue`: `self.items.append(value)`.
- `dequeue`: `self.items.popleft()`.

---

### Task 3 — `DataPipeline` class

#### `__init__(self)`
Initialize `self.steps = []`.

#### `add_step(self, step)`
Append the step name (a string) to `self.steps`.

#### `run(self)`
Return a **copy** of `self.steps` as a list.

```python
p = DataPipeline()
p.add_step('extract')
p.add_step('transform')
p.run()  # → ['extract', 'transform']
```

**Hint for run:** Return `self.steps[:]` (a copy so callers cannot modify the internal list).

---

## Run Tests
```bash
pytest assignments/week08_stacks_queues/tests/
```

All tests should pass once you complete each class.
