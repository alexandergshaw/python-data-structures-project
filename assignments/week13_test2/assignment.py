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

    Examples:
        Two scores — total is their sum and average is the mean:
            >>> evaluate_skills([80, 90])
            {'total': 170, 'average': 85.0}

        An empty list returns a zero-filled dict to avoid division-by-zero:
            >>> evaluate_skills([])
            {'total': 0, 'average': 0.0}

        A single score has a total and average equal to itself:
            >>> evaluate_skills([75])
            {'total': 75, 'average': 75.0}

        Three scores — average is (60 + 70 + 80) / 3 = 70.0:
            >>> evaluate_skills([60, 70, 80])
            {'total': 210, 'average': 70.0}

    Hints:
        total = sum(scores)
        average = total / len(scores) if scores else 0.0
        return {'total': total, 'average': average}
    """
    total = sum(scores)
    average = None  # TODO: replace None — compute total / len(scores) if scores else 0.0
    return {"total": total, "average": average}


def next_study_topic(scores: dict[str, int]) -> str:
    """Return the topic with the lowest score, or 'review' if scores is empty.

    Examples:
        The topic with the lowest score is returned — here 'sorting' at 60:
            >>> next_study_topic({"trees": 70, "sorting": 60})
            'sorting'

        An empty dict returns 'review' as a fallback:
            >>> next_study_topic({})
            'review'

        A single topic is returned as the minimum by default:
            >>> next_study_topic({"arrays": 85})
            'arrays'

        When all scores are equal, any one topic may be returned (the first encountered):
            >>> next_study_topic({"searching": 70, "stacks": 70, "queues": 70}) in {"searching", "stacks", "queues"}
            True

    Hints:
        if not scores: return 'review'
        return min(scores, key=scores.get)
    """
    if not scores:
        return 'review'
    return None  # TODO: replace None — use min(scores, key=scores.get) to find the lowest topic


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

