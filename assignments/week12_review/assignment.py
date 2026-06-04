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

    Examples:
        'arrays' is one of the six required topics:
            >>> 'arrays' in review_checklist()
            True

        All six topics are present:
            >>> set(review_checklist()) == {'arrays', 'linked lists', 'stacks', 'queues', 'searching', 'sorting'}
            True

        Exactly six topics are returned:
            >>> len(review_checklist())
            6

        'sorting' is the final topic in the semester sequence:
            >>> 'sorting' in review_checklist()
            True

    Hint:
        return ['arrays', 'linked lists', 'stacks', 'queues', 'searching', 'sorting']
    """
    return ['arrays', 'linked lists', 'stacks', 'queues', 'searching', None]  # TODO: replace None with the last missing topic


def score_readiness(completed_topics: int, total_topics: int = 6) -> float:
    """Return the percentage of topics completed.

    Return 0.0 if total_topics is 0.

    Formula: (completed_topics / total_topics) * 100

    Examples:
        Half the topics completed gives 50%:
            >>> score_readiness(3, 6)
            50.0

        All topics completed gives 100%:
            >>> score_readiness(6, 6)
            100.0

        No topics completed gives 0%:
            >>> score_readiness(0, 6)
            0.0

        Passing zero as total_topics returns 0.0 to avoid a division-by-zero error:
            >>> score_readiness(3, 0)
            0.0

        Works with the default total of 6 topics:
            >>> score_readiness(2)
            33.333333333333336

    Hint:
        if total_topics == 0: return 0.0
        return (completed_topics / total_topics) * 100
    """
    if total_topics == 0:
        return 0.0
    return None  # TODO: replace None — compute (completed_topics / total_topics) * 100


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

