"""Week 13 assignment starter for Comprehensive Test 2 Prep."""

WEEK_NUMBER = 13
TOPIC = 'Comprehensive Test 2 Prep'
FEATURE_NAME = 'Data Structures Badge'

LEARNING_OBJECTIVES = [
    "Practice mixed data structure problems.",
    "Summarize assessment readiness.",
    "Work with multiple complexity scenarios.",
]


def evaluate_skills(scores: list[int]) -> dict[str, float]:
    """Return the total and average of a list of practice scores.

    Return {"total": 0, "average": 0.0} for an empty list.

    Example:
        >>> evaluate_skills([80, 90])
        {'total': 170, 'average': 85.0}
        >>> evaluate_skills([])
        {'total': 0, 'average': 0.0}

    Hints:
        total = sum(scores)
        average = total / len(scores) if scores else 0.0
        return {'total': total, 'average': average}
    """
    # TODO: Compute total and average, return as a dict
    pass


def next_study_topic(scores: dict[str, int]) -> str:
    """Return the topic with the lowest score, or 'review' if scores is empty.

    Example:
        >>> next_study_topic({"trees": 70, "sorting": 60})
        'sorting'
        >>> next_study_topic({})
        'review'

    Hints:
        if not scores: return 'review'
        return min(scores, key=scores.get)
    """
    # TODO: Find and return the topic with the minimum score
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

