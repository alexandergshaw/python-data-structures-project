"""Week 16 assignment starter for Final Portfolio Build."""

WEEK_NUMBER = 16
TOPIC = 'Final Portfolio Build'
FEATURE_NAME = 'Recruiter View'

LEARNING_OBJECTIVES = [
    "Summarize weekly progress.",
    "Draft resume-ready bullet points.",
    "Compute a final grade from completion.",
]


def generate_final_summary(progress: dict[int, dict[str, object]]) -> dict[str, int]:
    """Return counts of completed and total weeks."""
    completed = sum(1 for item in progress.values() if item.get('complete'))
    return {'completed': completed, 'total': len(progress)}


def create_resume_bullets(skills: list[str]) -> list[str]:
    """Convert skills into concise resume bullets."""
    return [f"Applied {skill} in InsightHub portfolio work." for skill in skills]


def calculate_final_grade(weeks_completed: int) -> str:
    """Return a letter grade from completed weeks."""
    percentage = (weeks_completed / 16) * 100
    if percentage >= 90:
        return 'A'
    if percentage >= 80:
        return 'B'
    if percentage >= 70:
        return 'C'
    if percentage >= 60:
        return 'D'
    return 'F'


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

