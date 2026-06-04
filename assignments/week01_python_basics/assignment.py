"""Week 01 assignment starter for Python Basics."""

WEEK_NUMBER = 1
TOPIC = 'Python Basics'
FEATURE_NAME = 'Dataset Explorer'

LEARNING_OBJECTIVES = [
    "Work with variables and data types.",
    "Write functions that use arithmetic and f-strings.",
    "Use the modulo operator to check divisibility.",
]


def greet(name: str) -> str:
    """Return a greeting string for the given name.

    Example:
        >>> greet("Alice")
        'Hello, Alice!'
        >>> greet("World")
        'Hello, World!'

    Hint:
        Use an f-string: f"Hello, {name}!"
    """
    return None  # TODO: replace None — return f"Hello, {name}!"


def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of a and b.

    Example:
        >>> add(3, 4)
        7
        >>> add(1.5, 2.5)
        4.0

    Hint:
        Use the + operator: a + b
    """
    return None  # TODO: replace None — return a + b


def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise.

    Example:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
        >>> is_even(0)
        True

    Hint:
        A number is even when n % 2 == 0.
        The % operator gives the remainder after division.
    """
    return None  # TODO: replace None — return n % 2 == 0


def celsius_to_fahrenheit(c: float) -> float:
    """Convert a Celsius temperature to Fahrenheit.

    Formula: (c * 9 / 5) + 32

    Example:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
        >>> celsius_to_fahrenheit(-40)
        -40.0

    Hint:
        Apply the formula: (c * 9 / 5) + 32
    """
    return None  # TODO: replace None — apply the formula (c * 9 / 5) + 32


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

