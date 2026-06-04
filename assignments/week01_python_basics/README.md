# Week 01: Python Basics

## Overview
This is your first assignment. You will write four small functions that cover the most fundamental building blocks of Python: variables, arithmetic, f-strings, and boolean expressions. Every concept here reappears in later weeks, so make sure you understand *why* each solution works, not just *what* to type.

## Learning Objectives
- Work with variables and basic data types (`int`, `float`, `str`, `bool`).
- Write functions that use arithmetic operators and f-strings.
- Use the modulo operator (`%`) to check divisibility.

## How to Open the Starter File
All your code goes in `assignment.py` inside this folder. Open it and find the four functions. Each one currently has `return None` as a placeholder — replace that line with your implementation.

```
week01_python_basics/
├── assignment.py   ← edit this file
├── tests/
│   └── test_week01.py
└── README.md       ← you are here
```

---

## Task 1 — `greet(name)`

### What it should do
Accept a person's name as a string and return a friendly greeting.

```
greet("Alice")  →  "Hello, Alice!"
greet("World")  →  "Hello, World!"
greet("X")      →  "Hello, X!"
```

### Key concept: f-strings
An **f-string** (formatted string literal) lets you embed variable values directly inside a string. You prefix the string with `f` and wrap variable names in `{}`:

```
f"Hello, {name}!"
         ^^^^^^
         Python replaces this with the value of `name`
```

So if `name = "Alice"`, then `f"Hello, {name}!"` produces `"Hello, Alice!"`.

### Implementation hint
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

---

## Task 2 — `add(a, b)`

### What it should do
Accept two numbers and return their sum. Works for integers, floats, and mixed combinations.

```
add(3, 4)       →  7
add(1.5, 2.5)   →  4.0
add(-1, 1)      →  0
```

### Key concept: the `+` operator
In Python, `+` adds two numbers together. When either operand is a float, the result is also a float (`3 + 4 = 7` but `1.5 + 2.5 = 4.0`).

### Implementation hint
```python
def add(a, b):
    return a + b
```

---

## Task 3 — `is_even(n)`

### What it should do
Return `True` if `n` is an even number, `False` if it is odd.

```
is_even(4)   →  True    (4 ÷ 2 = 2, remainder 0)
is_even(7)   →  False   (7 ÷ 2 = 3, remainder 1)
is_even(0)   →  True    (0 ÷ 2 = 0, remainder 0)
```

### Key concept: the modulo operator `%`
The `%` operator returns the **remainder** after integer division:

```
8 % 2  →  0   (8 divides evenly by 2)
9 % 2  →  1   (9 divided by 2 is 4 remainder 1)
7 % 3  →  1   (7 divided by 3 is 2 remainder 1)
```

A number is even when dividing by 2 leaves no remainder, i.e. `n % 2 == 0`.

### Implementation hint
```python
def is_even(n: int) -> bool:
    return n % 2 == 0
```

---

## Task 4 — `celsius_to_fahrenheit(c)`

### What it should do
Convert a temperature in Celsius to its equivalent in Fahrenheit.

```
celsius_to_fahrenheit(0)     →  32.0    (freezing point of water)
celsius_to_fahrenheit(100)   →  212.0   (boiling point of water)
celsius_to_fahrenheit(-40)   →  -40.0   (the two scales meet here)
```

### Key concept: arithmetic formula
The conversion formula is:

```
°F = (°C × 9 / 5) + 32
```

Step by step for `c = 100`:
```
100 × 9  =  900
900 / 5  =  180
180 + 32 =  212.0  ✓
```

### Implementation hint
```python
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
```

---

## Unit Tests

### What are unit tests and why do they matter?
A **unit test** is a small automated check that calls one of your functions with a specific input and verifies you get the expected output. Instead of manually running your code and eyeballing the results, tests let you press one button and instantly know whether everything works.

Benefits:
- **Instant feedback** — you know within seconds whether your code is correct.
- **Safety net** — if you change one function and break another, the tests will catch it.
- **Self-documenting** — each test is an executable example of how a function should behave.

### How to run the tests

**Run only this week's tests** (recommended while you are working on Week 01):
```bash
pytest assignments/week01_python_basics/tests/ -v
```

The `-v` flag ("verbose") prints each individual test name so you can see exactly which ones pass or fail.

**Run all assignment tests at once** (useful for a final check):
```bash
pytest assignments/ -q
```

The `-q` flag ("quiet") gives a compact summary.

### What each test checks

| Test name | Input(s) | Expected output |
|-----------|----------|-----------------|
| `test_greet_basic` | `"Alice"` | `"Hello, Alice!"` |
| `test_greet_different_name` | `"World"` | `"Hello, World!"` |
| `test_greet_single_char` | `"X"` | `"Hello, X!"` |
| `test_add_integers` | `3, 4` | `7` |
| `test_add_floats` | `1.5, 2.5` | `4.0` |
| `test_add_negative` | `-1, 1` | `0` |
| `test_is_even_even` | `4` | `True` |
| `test_is_even_odd` | `7` | `False` |
| `test_is_even_zero` | `0` | `True` |
| `test_celsius_to_fahrenheit_zero` | `0` | `32.0` |
| `test_celsius_to_fahrenheit_hundred` | `100` | `212.0` |
| `test_celsius_to_fahrenheit_negative_forty` | `-40` | `-40.0` |

### Understanding the output
When every test passes you will see something like:
```
12 passed in 0.05s
```

If a test fails you will see a detailed report showing which test failed, the input used, what your function returned, and what was expected:
```
FAILED tests/test_week01.py::test_greet_basic
AssertionError: assert 'Hi, Alice!' == 'Hello, Alice!'
```
Read the assertion error carefully — it tells you exactly what went wrong. Fix the function and re-run.
