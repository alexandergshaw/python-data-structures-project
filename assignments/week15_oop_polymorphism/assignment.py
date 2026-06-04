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
    """Base class for all analytics report types."""

    def __init__(self, title: str) -> None:
        """Store the report title.

        Example:
            >>> report = AnalyticsReport("Overview")
            >>> report.title
            'Overview'

        Hint:
            self.title = title
        """
        self.title = None  # TODO: replace None — store the title parameter

    def render(self) -> str:
        """Return a formatted string describing this report.

        Example:
            >>> AnalyticsReport("Overview").render()
            'Analytics Report: Overview'

        Hint:
            return f"Analytics Report: {self.title}"
        """
        return None  # TODO: replace None — return f"Analytics Report: {self.title}"


class KPIReport(AnalyticsReport):
    """A report focused on key performance indicators.

    Inherits __init__ from AnalyticsReport — you only need to override render().
    """

    def render(self) -> str:
        """Return a KPI-specific report string.

        Example:
            >>> KPIReport("Revenue").render()
            'KPI Report: Revenue'

        Hint:
            return f"KPI Report: {self.title}"
        """
        return None  # TODO: replace None — return f"KPI Report: {self.title}"


class VisualizationReport(AnalyticsReport):
    """A report focused on visual charts and graphs.

    Inherits __init__ from AnalyticsReport — you only need to override render().
    """

    def render(self) -> str:
        """Return a Visualization-specific report string.

        Example:
            >>> VisualizationReport("Trend").render()
            'Visualization Report: Trend'

        Hint:
            return f"Visualization Report: {self.title}"
        """
        return None  # TODO: replace None — return f"Visualization Report: {self.title}"


class RecommendationReport(AnalyticsReport):
    """A report with actionable recommendations.

    Inherits __init__ from AnalyticsReport — you only need to override render().
    """

    def render(self) -> str:
        """Return a Recommendation-specific report string.

        Example:
            >>> RecommendationReport("Next Steps").render()
            'Recommendation Report: Next Steps'

        Hint:
            return f"Recommendation Report: {self.title}"
        """
        return None  # TODO: replace None — return f"Recommendation Report: {self.title}"


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

