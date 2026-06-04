"""Week 05 assignment starter for Test 1 Preparation."""

WEEK_NUMBER = 5
TOPIC = 'Test 1 Preparation'
FEATURE_NAME = 'Python Fundamentals Badge'

LEARNING_OBJECTIVES = [
    "Check whether two strings are anagrams.",
    "Find the maximum value in a list without using max().",
    "Reverse a string.",
    "Merge two dictionaries.",
]


def is_anagram(a: str, b: str) -> bool:
    """Return True if a and b are anagrams of each other, False otherwise.

    Two strings are anagrams if they contain the same letters in any order.
    The comparison is case-insensitive.

    Examples:
        "listen" and "silent" contain exactly the same letters rearranged:
            >>> is_anagram("listen", "silent")
            True

        "hello" and "world" do not share the same letter set:
            >>> is_anagram("hello", "world")
            False

        Case is ignored — uppercase and lowercase are treated the same:
            >>> is_anagram("Listen", "Silent")
            True

        Different lengths can never be anagrams:
            >>> is_anagram("abc", "ab")
            False

        A word is always an anagram of itself:
            >>> is_anagram("python", "python")
            True

    Hint:
        Sort the lowercase characters of each string and compare:
        sorted(a.lower()) == sorted(b.lower())
    """
    return None  # TODO: replace None — return sorted(a.lower()) == sorted(b.lower())


def find_max(numbers: list[int | float]) -> int | float | None:
    """Return the largest number in the list without using the built-in max().

    Return None if the list is empty.

    Examples:
        The largest value in the list is returned:
            >>> find_max([3, 1, 4, 1, 5, 9])
            9

        Works correctly with all-negative lists:
            >>> find_max([-5, -1, -3])
            -1

        An empty list has no maximum, so None is returned:
            >>> find_max([])

        A single-element list returns that element:
            >>> find_max([42])
            42

        The maximum can appear anywhere in the list, including the start:
            >>> find_max([100, 50, 75])
            100

    Hints:
        1. Return None immediately if numbers is empty.
        2. Start with current_max = numbers[0].
        3. Loop over the rest; if a number is larger, update current_max.
        4. Return current_max.
    """
    if not numbers:
        return None
    current_max = numbers[0]
    for num in numbers[1:]:
        if num > current_max:
            pass  # TODO: update current_max to num
    return current_max


def reverse_string(s: str) -> str:
    """Return the string s reversed.

    Examples:
        A common word reversed character by character:
            >>> reverse_string("hello")
            'olleh'

        Mixed case is preserved exactly:
            >>> reverse_string("Python")
            'nohtyP'

        An empty string reversed is still an empty string:
            >>> reverse_string("")
            ''

        A single character reversed is itself:
            >>> reverse_string("x")
            'x'

        A palindrome reversed equals itself:
            >>> reverse_string("racecar")
            'racecar'

    Hint:
        Use string slicing: s[::-1]
    """
    return None  # TODO: replace None — return s[::-1]


def merge_dicts(d1: dict, d2: dict) -> dict:
    """Return a new dictionary containing all key-value pairs from d1 and d2.

    When both dicts share a key, the value from d2 wins.

    Examples:
        Keys from both dicts are combined; 'b' from d2 overwrites 'b' from d1:
            >>> merge_dicts({"a": 1, "b": 2}, {"b": 99, "c": 3})
            {'a': 1, 'b': 99, 'c': 3}

        Merging with an empty first dict just returns the second dict's contents:
            >>> merge_dicts({}, {"x": 10})
            {'x': 10}

        Merging with an empty second dict just returns the first dict's contents:
            >>> merge_dicts({"x": 10}, {})
            {'x': 10}

        Both dicts empty results in an empty dict:
            >>> merge_dicts({}, {})
            {}

        No shared keys — all entries appear in the result:
            >>> merge_dicts({"a": 1}, {"b": 2})
            {'a': 1, 'b': 2}

    Hint:
        Build a copy of d1 first, then update it with d2:
            result = dict(d1)
            result.update(d2)
            return result
    """
    result = dict(d1)
    result.update(d2)
    return None  # TODO: replace None — return result


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
