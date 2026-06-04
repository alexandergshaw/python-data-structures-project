"""Week 00 assignment starter for Git Workflow."""

WEEK_NUMBER = 0
TOPIC = 'Git Workflow'

# ============================================================
# YOUR TASK
# ============================================================
# Change the value below from "John Doe" to your own full name.
# Example: STUDENT_NAME = "Maria Garcia"
#
# Rules:
#   - Keep the quotes around your name.
#   - Use your real first and last name.
#   - Do not leave it as "John Doe" — the tests will fail.
# ============================================================

STUDENT_NAME = "John Doe"


def get_student_name() -> str:
    """Return the student's name stored in STUDENT_NAME."""
    return STUDENT_NAME


def is_complete() -> bool:
    """Return True when the student has replaced the placeholder name."""
    return STUDENT_NAME.strip() != "John Doe" and len(STUDENT_NAME.strip()) > 0


def get_week_summary() -> dict:
    """Return a summary dict for this week."""
    return {
        'week': WEEK_NUMBER,
        'topic': TOPIC,
        'student_name': STUDENT_NAME,
        'complete': is_complete(),
    }
