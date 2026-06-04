"""Week 03 assignment starter for Collections and Classes."""

WEEK_NUMBER = 3
TOPIC = 'Collections and Classes'
FEATURE_NAME = 'KPI Dashboard'

LEARNING_OBJECTIVES = [
    "Remove duplicates with a set and sort a list.",
    "Count word occurrences with a dictionary.",
    "Build a simple class with an __init__ and methods.",
]


def get_unique_items(items: list) -> list:
    """Return a sorted list of unique items from the input list.

    Examples:
        Duplicates are removed and the remaining items are sorted in ascending order:
            >>> get_unique_items([3, 1, 2, 1, 3])
            [1, 2, 3]

        Works with strings — alphabetical sorting is applied:
            >>> get_unique_items(["b", "a", "b"])
            ['a', 'b']

        A list with no duplicates is simply returned sorted:
            >>> get_unique_items([1, 2, 3])
            [1, 2, 3]

        An empty list returns an empty list:
            >>> get_unique_items([])
            []

        A list where every element is identical keeps only one copy:
            >>> get_unique_items([7, 7, 7])
            [7]

    Hints:
        1. Convert items to a set to remove duplicates: set(items)
        2. Sort and return as a list: sorted(set(items))
    """
    return None  # TODO: replace None — return sorted(set(items))


def word_frequency(words: list[str]) -> dict[str, int]:
    """Return a dict mapping each word to how many times it appears.

    Examples:
        'hi' appears twice and 'bye' appears once:
            >>> word_frequency(["hi", "bye", "hi"])
            {'hi': 2, 'bye': 1}

        An empty list produces an empty dictionary:
            >>> word_frequency([])
            {}

        Every word appears exactly once when there are no duplicates:
            >>> word_frequency(["apple", "banana", "cherry"])
            {'apple': 1, 'banana': 1, 'cherry': 1}

        A list with a single repeated word counts all occurrences:
            >>> word_frequency(["yes", "yes", "yes"])
            {'yes': 3}

    Hints:
        1. Start with an empty dict: freq = {}
        2. Loop over words.
        3. Use freq[word] = freq.get(word, 0) + 1
        4. Return freq.
    """
    freq = {}
    for word in words:
        pass  # TODO: freq[word] = freq.get(word, 0) + 1
    return freq


class Counter:
    """A simple integer counter that can be incremented, decremented, and reset."""

    def __init__(self, start: int = 0) -> None:
        """Store the starting value in self.count.

        Examples:
            With no argument, the counter starts at zero by default:
                >>> c = Counter()
                >>> c.count
                0

            A custom starting value can be provided:
                >>> c = Counter(10)
                >>> c.count
                10

            Negative starting values are also valid:
                >>> c = Counter(-5)
                >>> c.count
                -5

        Hint:
            self.count = start
        """
        self.count = None  # TODO: replace None — store start in self.count

    def increment(self) -> None:
        """Add 1 to self.count.

        Examples:
            Starting from the default of 0, one increment gives 1:
                >>> c = Counter()
                >>> c.increment()
                >>> c.count
                1

            Multiple increments accumulate:
                >>> c = Counter()
                >>> c.increment()
                >>> c.increment()
                >>> c.increment()
                >>> c.count
                3

            Incrementing from a non-zero start also works:
                >>> c = Counter(5)
                >>> c.increment()
                >>> c.count
                6

        Hint:
            self.count += 1
        """
        pass  # TODO: self.count += 1

    def decrement(self) -> None:
        """Subtract 1 from self.count.

        Examples:
            Starting at 5, one decrement gives 4:
                >>> c = Counter(5)
                >>> c.decrement()
                >>> c.count
                4

            Decrementing from 0 goes into negative territory:
                >>> c = Counter()
                >>> c.decrement()
                >>> c.count
                -1

            Multiple decrements accumulate:
                >>> c = Counter(3)
                >>> c.decrement()
                >>> c.decrement()
                >>> c.count
                1

        Hint:
            self.count -= 1
        """
        pass  # TODO: self.count -= 1

    def reset(self) -> None:
        """Set self.count back to 0.

        Examples:
            After incrementing several times, reset brings the counter back to zero:
                >>> c = Counter(5)
                >>> c.reset()
                >>> c.count
                0

            Even a counter that already holds 0 can be reset without error:
                >>> c = Counter()
                >>> c.reset()
                >>> c.count
                0

            Reset after a series of operations:
                >>> c = Counter(10)
                >>> c.increment()
                >>> c.decrement()
                >>> c.reset()
                >>> c.count
                0

        Hint:
            self.count = 0
        """
        pass  # TODO: self.count = 0

    def get_value(self) -> int:
        """Return the current count.

        Examples:
            get_value on a fresh counter returns the start value:
                >>> c = Counter(7)
                >>> c.get_value()
                7

            get_value reflects changes made by increment and decrement:
                >>> c = Counter()
                >>> c.increment()
                >>> c.increment()
                >>> c.get_value()
                2

            get_value does not change the counter — calling it twice returns the same number:
                >>> c = Counter(42)
                >>> c.get_value()
                42
                >>> c.get_value()
                42

        Hint:
            return self.count
        """
        return None  # TODO: replace None — return self.count


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
