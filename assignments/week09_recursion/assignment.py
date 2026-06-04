"""Week 09 assignment starter for Recursion."""

WEEK_NUMBER = 9
TOPIC = 'Recursion'
FEATURE_NAME = 'Nested Data Explorer'

from typing import Any

LEARNING_OBJECTIVES = [
    "Sum data recursively.",
    "Search recursively.",
    "Flatten nested structures.",
]


def recursive_sum(data: list[int]) -> int:
    """Return the sum of all integers in data using recursion (no sum()).

    Examples:
        Three positive integers add up to 6:
            >>> recursive_sum([1, 2, 3])
            6

        The base case: an empty list has a sum of zero:
            >>> recursive_sum([])
            0

        A single-element list returns that element:
            >>> recursive_sum([42])
            42

        Negative numbers are included in the sum:
            >>> recursive_sum([-1, -2, -3])
            -6

        Mixed positive and negative values:
            >>> recursive_sum([10, -3, 7])
            14

    Hints:
        Base case:     if not data: return 0
        Recursive case: data[0] + recursive_sum(data[1:])
    """
    if not data:
        return 0
    return None  # TODO: replace None — add data[0] to the recursive sum of data[1:]


def recursive_search(data: list[Any], target: Any, index: int = 0) -> int:
    """Return the index of the first occurrence of target, or -1 if not found.

    Examples:
        'b' is at index 1 in the list:
            >>> recursive_search(['a', 'b', 'c'], 'b')
            1

        A value that doesn't exist returns -1:
            >>> recursive_search(['a', 'b', 'c'], 'z')
            -1

        The first element is found at index 0:
            >>> recursive_search(['x', 'y', 'z'], 'x')
            0

        An empty list always returns -1:
            >>> recursive_search([], 'a')
            -1

        Only the first occurrence is returned — later duplicates are ignored:
            >>> recursive_search([1, 2, 1, 3], 1)
            0

    Hints:
        Base case 1:   if index >= len(data): return -1
        Base case 2:   if data[index] == target: return index
        Recursive case: return recursive_search(data, target, index + 1)
    """
    if index >= len(data):
        return -1
    if data[index] == target:
        return index
    return None  # TODO: replace None — recurse with index + 1


def flatten_nested(data: list[Any]) -> list[Any]:
    """Return a flat list from a nested list structure.

    Examples:
        A deeply nested list is fully flattened to a single level:
            >>> flatten_nested([1, [2, [3]]])
            [1, 2, 3]

        A list with no nesting is returned unchanged:
            >>> flatten_nested([1, 2, 3])
            [1, 2, 3]

        An empty list flattens to an empty list:
            >>> flatten_nested([])
            []

        Mixed nesting depth — all elements end up in one flat list:
            >>> flatten_nested([[1, 2], [3, [4, 5]]])
            [1, 2, 3, 4, 5]

        Works with strings and other non-list types as leaf values:
            >>> flatten_nested(["a", ["b", ["c"]]])
            ['a', 'b', 'c']

    Hints:
        1. Start with flat = []
        2. For each item in data:
               if isinstance(item, list): flat.extend(flatten_nested(item))
               else:                      flat.append(item)
        3. Return flat
    """
    flat = []
    for item in data:
        if isinstance(item, list):
            pass  # TODO: extend flat with the result of recursively flattening item
        else:
            pass  # TODO: append item to flat
    return flat


def recursive_count(data: list[Any]) -> int:
    """Return the total number of non-list items in a nested list.

    Examples:
        Three leaf values across three nesting levels:
            >>> recursive_count([1, [2, [3]]])
            3

        A flat list counts every element directly:
            >>> recursive_count([1, 2, 3, 4])
            4

        An empty list contains zero non-list items:
            >>> recursive_count([])
            0

        Nested empty lists count as zero because they contain no leaf values:
            >>> recursive_count([[], [[], []]])
            0

    Hint:
        Use flatten_nested(data) and return len() of the result.
    """
    return None  # TODO: replace None — call flatten_nested(data) then return len() of the result


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

