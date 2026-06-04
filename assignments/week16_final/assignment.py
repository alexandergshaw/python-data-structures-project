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
    """Count completed weeks and total weeks.

    Args:
        progress: dict mapping week numbers to dicts with a "complete" key.

    Returns:
        A dict with "completed" (int) and "total" (int).

    Example:
        >>> p = {1: {"complete": True}, 2: {"complete": False}, 3: {"complete": True}}
        >>> generate_final_summary(p)
        {'completed': 2, 'total': 3}

    Hints:
        Step 1: Count how many values have .get("complete") == True.
                You can use: sum(1 for v in progress.values() if v.get("complete"))
        Step 2: "total" is just len(progress).
        Step 3: Return {"completed": ..., "total": ...}
    """
    completed = sum(1 for v in progress.values() if v.get("complete"))
    return {"completed": completed, "total": None}  # TODO: replace None with len(progress)


def create_resume_bullets(skills: list[str]) -> list[str]:
    """Convert a list of skills into resume-style bullet strings.

    Args:
        skills: List of skill names (e.g., ["Python", "Sorting"]).

    Returns:
        A list of strings: "Applied {skill} in InsightHub portfolio work."

    Example:
        >>> create_resume_bullets(["Python", "Sorting"])
        ['Applied Python in InsightHub portfolio work.',
         'Applied Sorting in InsightHub portfolio work.']

    Hints:
        Step 1: Use a list comprehension.
        Step 2: For each skill: f"Applied {skill} in InsightHub portfolio work."
    """
    return [None for skill in skills]  # TODO: replace None with f"Applied {skill} in InsightHub portfolio work."


def calculate_final_grade(weeks_completed: int) -> str:
    """Return a letter grade based on weeks completed out of 16.

    Grade scale (percentage of 16 weeks):
        >= 90% → 'A'
        >= 80% → 'B'
        >= 70% → 'C'
        >= 60% → 'D'
        < 60%  → 'F'

    Examples:
        >>> calculate_final_grade(16)
        'A'
        >>> calculate_final_grade(0)
        'F'

    Hints:
        Step 1: percentage = (weeks_completed / 16) * 100
        Step 2: Use if/elif/else comparing percentage to 90, 80, 70, 60.
    """
    percentage = (weeks_completed / 16) * 100
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return None  # TODO: replace None — what letter grade is 80–89%?
    elif percentage >= 70:
        return None  # TODO: replace None — what letter grade is 70–79%?
    elif percentage >= 60:
        return None  # TODO: replace None — what letter grade is 60–69%?
    else:
        return None  # TODO: replace None — what letter grade is below 60%?


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

