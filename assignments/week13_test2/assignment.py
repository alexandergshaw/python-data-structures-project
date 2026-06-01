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
    """Return total and average practice scores."""
    total = sum(scores)
    average = total / len(scores) if scores else 0.0
    return {'total': total, 'average': average}


def next_study_topic(scores: dict[str, int]) -> str:
    """Return the topic with the lowest score."""
    return min(scores, key=scores.get) if scores else 'review'


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

