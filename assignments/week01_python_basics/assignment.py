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

    Examples:
        Greeting a person by first name:
            >>> greet("Alice")
            'Hello, Alice!'

        Greeting with any string — the function just wraps whatever name is given:
            >>> greet("World")
            'Hello, World!'

        A single-character name works the same way:
            >>> greet("Z")
            'Hello, Z!'

    Hint:
        Use an f-string: f"Hello, {name}!"
    """
    return None  # TODO: replace None — return f"Hello, {name}!"


def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of a and b.

    Examples:
        Adding two positive integers:
            >>> add(3, 4)
            7

        Adding two floats — the result is also a float:
            >>> add(1.5, 2.5)
            4.0

        Adding a negative and a positive number:
            >>> add(-10, 4)
            -6

        Adding zero to a number leaves it unchanged:
            >>> add(0, 99)
            99

    Hint:
        Use the + operator: a + b
    """
    return None  # TODO: replace None — return a + b


def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise.

    Examples:
        A typical even number:
            >>> is_even(4)
            True

        An odd number returns False:
            >>> is_even(7)
            False

        Zero is considered even (0 % 2 == 0):
            >>> is_even(0)
            True

        Negative even numbers also return True:
            >>> is_even(-6)
            True

        Negative odd numbers return False:
            >>> is_even(-3)
            False

    Hint:
        A number is even when n % 2 == 0.
        The % operator gives the remainder after division.
    """
    return None  # TODO: replace None — return n % 2 == 0


def celsius_to_fahrenheit(c: float) -> float:
    """Convert a Celsius temperature to Fahrenheit.

    Formula: (c * 9 / 5) + 32

    Examples:
        The freezing point of water (0 °C) converts to 32 °F:
            >>> celsius_to_fahrenheit(0)
            32.0

        The boiling point of water (100 °C) converts to 212 °F:
            >>> celsius_to_fahrenheit(100)
            212.0

        -40 °C and -40 °F are the same — the scales intersect here:
            >>> celsius_to_fahrenheit(-40)
            -40.0

        Normal body temperature (37 °C) converts to approximately 98.6 °F:
            >>> celsius_to_fahrenheit(37)
            98.60000000000001

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

