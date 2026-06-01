"""Week 15 assignment starter for OOP and Polymorphism."""

WEEK_NUMBER = 15
TOPIC = 'OOP and Polymorphism'
FEATURE_NAME = 'Insights & Recommendations Center'

LEARNING_OBJECTIVES = [
    "Use inheritance for multiple report types.",
    "Override summary behavior polymorphically.",
    "Model analytics outputs with classes.",
]


class AnalyticsReport:
    def __init__(self, title: str) -> None:
        self.title = title

    def render(self) -> str:
        return f"Analytics Report: {self.title}"


class KPIReport(AnalyticsReport):
    def render(self) -> str:
        return f"KPI Report: {self.title}"


class VisualizationReport(AnalyticsReport):
    def render(self) -> str:
        return f"Visualization Report: {self.title}"


class RecommendationReport(AnalyticsReport):
    def render(self) -> str:
        return f"Recommendation Report: {self.title}"


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

