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
    """Return a checklist of topics to review."""
    return ['arrays', 'linked lists', 'stacks', 'queues', 'searching', 'sorting']


def score_readiness(completed_topics: int, total_topics: int = 6) -> float:
    """Return completion ratio as a percentage."""
    if total_topics == 0:
        return 0.0
    return (completed_topics / total_topics) * 100


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

