# Week 02: Control Flow

## Overview
This week you learn how to make your program *decide* and *repeat*. Decision-making uses `if`/`elif`/`else` blocks; repetition uses `for` loops. These are the two most essential control-flow tools in Python, and they appear in virtually every program you will ever write.

## Learning Objectives
- Use `if`, `elif`, and `else` to branch on conditions.
- Use `for` loops to iterate over lists.
- Return early from a loop when you find what you need.

## How to Open the Starter File
All your code goes in `assignment.py`. Each function body currently contains `pass` — replace that with your implementation.

```
week02_control_flow/
├── assignment.py   ← edit this file
├── tests/
│   └── test_week02.py
└── README.md       ← you are here
```

---

## Task 1 — `classify_number(n)`

### What it should do
Look at a number and return one of three strings describing it.

```
classify_number(5)   →  "positive"
classify_number(-3)  →  "negative"
classify_number(0)   →  "zero"
```

### Key concept: `if` / `elif` / `else`
An `if` block runs only when its condition is `True`. Use `elif` ("else if") for additional conditions, and `else` as the fallback when nothing matched:

```
                ┌─────────────────────────┐
   n > 0?  ─── │  Yes → return "positive" │
                └─────────────────────────┘
                ┌─────────────────────────┐
   n < 0?  ─── │  Yes → return "negative" │
                └─────────────────────────┘
                ┌─────────────────────────┐
   else    ─── │        return "zero"     │
                └─────────────────────────┘
```

### Implementation hint
```python
def classify_number(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"
```

---

## Task 2 — `fizzbuzz(n)`

### What it should do
Apply the classic FizzBuzz rules:

```
fizzbuzz(15)  →  "FizzBuzz"   (divisible by both 3 and 5)
fizzbuzz(9)   →  "Fizz"       (divisible by 3 only)
fizzbuzz(10)  →  "Buzz"       (divisible by 5 only)
fizzbuzz(7)   →  "7"          (not divisible by either)
```

### Key concept: order of conditions matters
Check the *combined* case **first**. If you check "divisible by 3" before "divisible by both 3 and 5", then 15 would incorrectly return `"Fizz"` and never reach `"FizzBuzz"`.

```
  n % 15 == 0?  (or: n%3==0 AND n%5==0)  ──→  "FizzBuzz"
  n %  3 == 0?                            ──→  "Fizz"
  n %  5 == 0?                            ──→  "Buzz"
  otherwise                               ──→  str(n)
```

Notice the last case converts `n` to a string with `str(n)`. Returning the integer `7` would not match the expected string `"7"`.

### Implementation hint
```python
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
```

---

## Task 3 — `count_positives(numbers)`

### What it should do
Count how many numbers in the list are strictly greater than zero.

```
count_positives([1, -2, 3, 0, 5])  →  3   (1, 3, and 5 qualify)
count_positives([-1, -2])           →  0
count_positives([])                 →  0
```

Note: `0` itself is **not** positive. Only values strictly `> 0` count.

### Key concept: accumulator pattern
The most common loop pattern is the **accumulator**: start a counter at zero, loop over every item, and add to the counter whenever a condition is met.

```
counter = 0
for each number in the list:
    if number > 0:
        counter += 1
return counter
```

### Implementation hint
```python
def count_positives(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count
```

---

## Task 4 — `find_first_negative(numbers)`

### What it should do
Scan the list and return the **first** number that is less than zero. If none exist, return `None`.

```
find_first_negative([3, 1, -5, 2])  →  -5   (stops at index 2)
find_first_negative([1, 2, 3])      →  None  (no negatives)
find_first_negative([-1, 2, 3])     →  -1   (first element qualifies)
```

### Key concept: early return inside a loop
Instead of collecting all negatives and picking one later, you can `return` immediately when you find what you need. This stops the loop early and is more efficient.

```
for each number in the list:
    if number < 0:
        return number   ← stops here, never looks at the rest
# only reached if the loop finishes without returning
return None
```

### Implementation hint
```python
def find_first_negative(numbers):
    for num in numbers:
        if num < 0:
            return num
    return None
```

---

## Unit Tests

### What are unit tests and why do they matter?
Each test calls one of your functions with a specific input and checks that you get exactly the right output. If your function returns something unexpected, the test fails and you see a clear error message pointing to the problem. Unit tests give you fast, reliable feedback so you can fix bugs quickly.

### How to run the tests

**Run only this week's tests:**
```bash
pytest assignments/week02_control_flow/tests/ -v
```

**Run all assignments at once:**
```bash
pytest assignments/ -q
```

### What each test checks

| Test name | Input(s) | Expected output |
|-----------|----------|-----------------|
| `test_classify_number_positive` | `5` | `"positive"` |
| `test_classify_number_negative` | `-3` | `"negative"` |
| `test_classify_number_zero` | `0` | `"zero"` |
| `test_fizzbuzz_fizzbuzz` | `15` | `"FizzBuzz"` |
| `test_fizzbuzz_fizz` | `9` | `"Fizz"` |
| `test_fizzbuzz_buzz` | `10` | `"Buzz"` |
| `test_fizzbuzz_other` | `7` | `"7"` |
| `test_count_positives_mixed` | `[1, -2, 3, 0, 5]` | `3` |
| `test_count_positives_all_negative` | `[-1, -2]` | `0` |
| `test_count_positives_empty` | `[]` | `0` |
| `test_find_first_negative_found` | `[3, 1, -5, 2]` | `-5` |
| `test_find_first_negative_none` | `[1, 2, 3]` | `None` |
| `test_find_first_negative_first_element` | `[-1, 2, 3]` | `-1` |

### Understanding the output
All 13 tests should pass when your implementation is complete. If a test fails, read the error message — it will show you the function name, the input, what you returned, and what was expected.
