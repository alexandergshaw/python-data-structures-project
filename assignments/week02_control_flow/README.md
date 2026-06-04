# Week 02: Control Flow

## Learning Objectives
- Use `if`, `elif`, and `else` to branch on conditions.
- Use `for` loops to iterate over lists.
- Return early from a loop when you find what you need.

## What You Need to Do
Open `assignment.py` and implement the four functions below. Each function body currently contains `pass`—replace that with your code.

---

### Task 1 — `classify_number(n)`
Return `"positive"`, `"negative"`, or `"zero"` based on the value of `n`.

```python
classify_number(5)   # → "positive"
classify_number(-3)  # → "negative"
classify_number(0)   # → "zero"
```

**Hint:** Use `if n > 0`, `elif n < 0`, and `else`.

---

### Task 2 — `fizzbuzz(n)`
Return `"FizzBuzz"` if `n` is divisible by both 3 and 5,  
`"Fizz"` if divisible by 3 only,  
`"Buzz"` if divisible by 5 only,  
or the number itself as a string otherwise.

```python
fizzbuzz(15)  # → "FizzBuzz"
fizzbuzz(9)   # → "Fizz"
fizzbuzz(10)  # → "Buzz"
fizzbuzz(7)   # → "7"
```

**Hint:** Check the combined case (`n % 3 == 0 and n % 5 == 0`) **first**, before the individual checks.

---

### Task 3 — `count_positives(numbers)`
Return how many numbers in the list are strictly greater than zero.

```python
count_positives([1, -2, 3, 0, 5])  # → 3
count_positives([-1, -2])           # → 0
count_positives([])                 # → 0
```

**Hints:**
1. Start a counter at `0`.
2. Loop over `numbers` with a `for` loop.
3. Add `1` to the counter whenever `num > 0`.
4. Return the counter.

---

### Task 4 — `find_first_negative(numbers)`
Return the first negative number in the list, or `None` if there are none.

```python
find_first_negative([3, 1, -5, 2])  # → -5
find_first_negative([1, 2, 3])      # → None
find_first_negative([-1, 2, 3])     # → -1
```

**Hints:**
1. Loop over the list.
2. As soon as you find a number `< 0`, `return` it immediately.
3. If the loop finishes without finding one, `return None`.

---

## Run Tests
```bash
pytest assignments/week02_control_flow/tests/
```

All tests should pass once you complete each task.
