"""Week 12 assignment starter for Algorithms and Data Structures Review."""

WEEK_NUMBER = 12
TOPIC = 'Algorithms and Data Structures Review'
FEATURE_NAME = 'Algorithm Review Center'

LEARNING_OBJECTIVES = [
    "Review previous data structures.",
    "Practice algorithm comparisons.",
    "Summarize readiness for assessments.",
]


def review_checklist() -> list[str]:
    """Return a list of the six core topics covered this semester.

    The list must contain:
        'arrays', 'linked lists', 'stacks', 'queues', 'searching', 'sorting'

    Example:
        >>> 'arrays' in review_checklist()
        True

    Hint:
        return ['arrays', 'linked lists', 'stacks', 'queues', 'searching', 'sorting']
    """
    # TODO: Return a list of the six topic strings
    pass


def score_readiness(completed_topics: int, total_topics: int = 6) -> float:
    """Return the percentage of topics completed.

    Return 0.0 if total_topics is 0.

    Formula: (completed_topics / total_topics) * 100

    Example:
        >>> score_readiness(3, 6)
        50.0
        >>> score_readiness(6, 6)
        100.0
        >>> score_readiness(0, 6)
        0.0

    Hint:
        if total_topics == 0: return 0.0
        return (completed_topics / total_topics) * 100
    """
    # TODO: Compute and return the readiness percentage
    pass


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

