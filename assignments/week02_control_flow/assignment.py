"""Week 02 assignment starter for Control Flow."""

WEEK_NUMBER = 2
TOPIC = 'Control Flow'
FEATURE_NAME = 'Data Cleaning Center'

LEARNING_OBJECTIVES = [
    "Use if/elif/else to branch on conditions.",
    "Use for loops to iterate over lists.",
    "Return early from a loop when you find what you need.",
]


def classify_number(n: int | float) -> str:
    """Return 'positive', 'negative', or 'zero' based on n.

    Examples:
        Any number greater than zero is positive:
            >>> classify_number(5)
            'positive'

        Any number less than zero is negative:
            >>> classify_number(-3)
            'negative'

        Zero is its own special category — not positive or negative:
            >>> classify_number(0)
            'zero'

        Floats work too — 0.1 is still positive:
            >>> classify_number(0.1)
            'positive'

        Large negative floats are still negative:
            >>> classify_number(-999.9)
            'negative'

    Hint:
        Use if n > 0, elif n < 0, else.
    """
    if n > 0:
        pass  # TODO: return "positive"
    elif n < 0:
        pass  # TODO: return "negative"
    else:
        pass  # TODO: return "zero"


def fizzbuzz(n: int) -> str:
    """Return "FizzBuzz", "Fizz", "Buzz", or the number as a string.

    Rules:
        - Divisible by both 3 and 5 → "FizzBuzz"
        - Divisible by 3 only        → "Fizz"
        - Divisible by 5 only        → "Buzz"
        - Otherwise                  → str(n)

    Examples:
        15 is divisible by both 3 and 5, so it gets the combined label:
            >>> fizzbuzz(15)
            'FizzBuzz'

        9 is only divisible by 3:
            >>> fizzbuzz(9)
            'Fizz'

        10 is only divisible by 5:
            >>> fizzbuzz(10)
            'Buzz'

        7 is divisible by neither, so its string form is returned:
            >>> fizzbuzz(7)
            '7'

        1 is also not divisible by 3 or 5:
            >>> fizzbuzz(1)
            '1'

        30 is divisible by both 3 and 5 — another FizzBuzz:
            >>> fizzbuzz(30)
            'FizzBuzz'

    Hint:
        Check n % 3 == 0 and n % 5 == 0 FIRST (the combined case).
    """
    if n % 3 == 0 and n % 5 == 0:
        pass  # TODO: return "FizzBuzz"
    elif n % 3 == 0:
        pass  # TODO: return "Fizz"
    elif n % 5 == 0:
        pass  # TODO: return "Buzz"
    else:
        pass  # TODO: return str(n)


def count_positives(numbers: list[int | float]) -> int:
    """Return how many numbers in the list are greater than zero.

    Examples:
        Three of the five values are greater than zero (0 itself is not positive):
            >>> count_positives([1, -2, 3, 0, 5])
            3

        A list of all negative values contributes zero positives:
            >>> count_positives([-1, -2])
            0

        An empty list has no elements at all, so the count is zero:
            >>> count_positives([])
            0

        A list of all positives counts every element:
            >>> count_positives([10, 20, 30])
            3

        Zero is not considered positive — it is excluded from the count:
            >>> count_positives([0, 0, 0])
            0

    Hints:
        1. Start count = 0.
        2. Loop over numbers with a for loop.
        3. If num > 0, add 1 to count.
        4. Return count.
    """
    count = 0
    for num in numbers:
        if num > 0:
            pass  # TODO: add 1 to count
    return count


def find_first_negative(numbers: list[int | float]) -> int | float | None:
    """Return the first negative number in the list, or None if there are none.

    Examples:
        The first negative encountered (scanning left to right) is returned immediately:
            >>> find_first_negative([3, 1, -5, 2])
            -5

        When no negatives exist, None is returned after scanning the whole list:
            >>> find_first_negative([1, 2, 3])

        The very first element can be the first negative:
            >>> find_first_negative([-1, 2, 3])
            -1

        An empty list has no negatives, so None is returned:
            >>> find_first_negative([])

        Later negatives are ignored once the first is found:
            >>> find_first_negative([5, -3, -7, -1])
            -3

    Hints:
        1. Loop over the list with a for loop.
        2. If num < 0, return num immediately (return early).
        3. After the loop ends, return None.
    """
    for num in numbers:
        if num < 0:
            pass  # TODO: return num here (return early — don't wait for the loop to finish)
    return None


def is_complete() -> bool:
    """Return completion status for this week's assignment starter."""
    return False


def get_unlocked_feature() -> str:
    """Return the dashboard feature unlocked by this week."""
    return FEATURE_NAME


def get_week_summary() -> dict[str, object]:
    """Return a dashboard-friendly summary for this week."""
    return {
        'week': WEEK_NUMBER,
        'topic': TOPIC,
        'feature': FEATURE_NAME,
        'objectives': LEARNING_OBJECTIVES,
        'complete': is_complete(),
    }
