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

    Example:
        >>> classify_number(5)
        'positive'
        >>> classify_number(-3)
        'negative'
        >>> classify_number(0)
        'zero'

    """
    if n > 0:
        pass  # TODO
    elif n < 0:
        pass  # TODO
    else:
        pass  # TODO


def fizzbuzz(n: int) -> str:
    """Return "FizzBuzz", "Fizz", "Buzz", or the number as a string.

    Rules:
        - Divisible by both 3 and 5 → "FizzBuzz"
        - Divisible by 3 only        → "Fizz"
        - Divisible by 5 only        → "Buzz"
        - Otherwise                  → str(n)

    Example:
        >>> fizzbuzz(15)
        'FizzBuzz'
        >>> fizzbuzz(9)
        'Fizz'
        >>> fizzbuzz(10)
        'Buzz'
        >>> fizzbuzz(7)
        '7'

    """
    if n % 3 == 0 and n % 5 == 0:
        pass  # TODO
    elif n % 3 == 0:
        pass  # TODO
    elif n % 5 == 0:
        pass  # TODO
    else:
        pass  # TODO


def count_positives(numbers: list[int | float]) -> int:
    """Return how many numbers in the list are greater than zero.

    Example:
        >>> count_positives([1, -2, 3, 0, 5])
        3
        >>> count_positives([-1, -2])
        0
        >>> count_positives([])
        0

    """
    count = 0
    for num in numbers:
        if num > 0:
            pass  # TODO
    return count


def find_first_negative(numbers: list[int | float]) -> int | float | None:
    """Return the first negative number in the list, or None if there are none.

    Example:
        >>> find_first_negative([3, 1, -5, 2])
        -5
        >>> find_first_negative([1, 2, 3])
        None
        >>> find_first_negative([-1, 2, 3])
        -1

    """
    for num in numbers:
        if num < 0:
            pass  # TODO
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
