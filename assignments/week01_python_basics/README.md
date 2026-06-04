# Week 01: Python Basics

## Learning Objectives
- Work with variables and data types.
- Write functions that use arithmetic and f-strings.
- Use the modulo operator to check divisibility.

## What You Need to Do
Open `assignment.py` and implement the four functions below. Each function body contains `return None`—replace that with your code.

---

### Task 1 — `greet(name)`
Return a personalised greeting string.

```python
greet("Alice")  # → "Hello, Alice!"
greet("World")  # → "Hello, World!"
```

**Hint:** Use an f-string: `f"Hello, {name}!"`

---

### Task 2 — `add(a, b)`
Return the sum of two numbers.

```python
add(3, 4)     # → 7
add(1.5, 2.5) # → 4.0
add(-1, 1)    # → 0
```

**Hint:** Use the `+` operator.

---

### Task 3 — `is_even(n)`
Return `True` if `n` is even, `False` otherwise.

```python
is_even(4)  # → True
is_even(7)  # → False
is_even(0)  # → True
```

**Hint:** A number is even when `n % 2 == 0`. The `%` operator gives the remainder after division.

---

### Task 4 — `celsius_to_fahrenheit(c)`
Convert a Celsius temperature to Fahrenheit.

**Formula:** `(c × 9 / 5) + 32`

```python
celsius_to_fahrenheit(0)    # → 32.0
celsius_to_fahrenheit(100)  # → 212.0
celsius_to_fahrenheit(-40)  # → -40.0
```

**Hint:** Apply the formula directly: `(c * 9 / 5) + 32`

---

## Run Tests
```bash
pytest assignments/week01_python_basics/tests/
```

All four tests should pass once you complete each task.
