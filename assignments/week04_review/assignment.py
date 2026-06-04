"""Week 04 assignment starter for Review and Integration."""

WEEK_NUMBER = 4
TOPIC = 'Review and Integration'
FEATURE_NAME = 'Analytics Progress Dashboard'

LEARNING_OBJECTIVES = [
    "Check whether a string is a palindrome.",
    "Count vowels in a string using a loop.",
    "Clamp a value between a minimum and maximum.",
    "Summarize a list of numbers into a single dictionary.",
]


def is_palindrome(s: str) -> bool:
    """Return True if s reads the same forwards and backwards, False otherwise.

    Comparison is case-sensitive.

    Example:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("a")
        True

    Hint:
        A string is a palindrome when it equals its reverse.
        Reverse a string with slicing: s[::-1]
    """
    return None  # TODO: replace None — return s == s[::-1]


def count_vowels(text: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in text.

    Case-insensitive: 'A' and 'a' both count.

    Example:
        >>> count_vowels("hello")
        2
        >>> count_vowels("AEIOU")
        5
        >>> count_vowels("gym")
        0

    Hints:
        1. Convert text to lowercase: text.lower()
        2. Loop over each character.
        3. Check if the character is in the string "aeiou".
        4. Count matches and return the total.
    """
    count = 0
    for char in text.lower():
        if char in "aeiou":
            pass  # TODO: add 1 to count
    return count


def clamp(value: int | float, lo: int | float, hi: int | float) -> int | float:
    """Return value clamped to the range [lo, hi].

    If value < lo, return lo.
    If value > hi, return hi.
    Otherwise return value.

    Example:
        >>> clamp(5, 1, 10)
        5
        >>> clamp(-3, 0, 100)
        0
        >>> clamp(200, 0, 100)
        100

    Hints:
        1. if value < lo: return lo
        2. if value > hi: return hi
        3. return value
    """
    if value < lo:
        pass  # TODO: return lo
    if value > hi:
        pass  # TODO: return hi
    return value


def summarize(numbers: list[int | float]) -> dict[str, int | float]:
    """Return a summary dictionary for a list of numbers.

    The returned dict must have these keys:
        "count" — how many numbers are in the list
        "total" — the sum of all numbers
        "minimum" — the smallest number
        "maximum" — the largest number

    Return all zeros when the list is empty.

    Example:
        >>> summarize([3, 1, 4, 1, 5])
        {'count': 5, 'total': 14, 'minimum': 1, 'maximum': 5}
        >>> summarize([])
        {'count': 0, 'total': 0, 'minimum': 0, 'maximum': 0}

    Hints:
        - Guard against an empty list: if not numbers, return the zero dict.
        - Use len(), sum(), min(), max() for the values.
    """
    if not numbers:
        return {"count": 0, "total": 0, "minimum": 0, "maximum": 0}
    return {
        "count": None,    # TODO: replace None — use len(numbers)
        "total": None,    # TODO: replace None — use sum(numbers)
        "minimum": None,  # TODO: replace None — use min(numbers)
        "maximum": None,  # TODO: replace None — use max(numbers)
    }


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
