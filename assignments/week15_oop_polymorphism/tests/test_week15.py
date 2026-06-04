"""Tests for Week 15: OOP and Polymorphism."""

import importlib

assignment = importlib.import_module('assignments.week15_oop_polymorphism.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_analytics_report_title_stored():
    report = assignment.AnalyticsReport('Overview')
    assert report.title == 'Overview'


def test_analytics_report_render():
    assert assignment.AnalyticsReport('Overview').render() == 'Analytics Report: Overview'


def test_kpi_report_render():
    assert assignment.KPIReport('Revenue').render() == 'KPI Report: Revenue'


def test_kpi_report_has_title():
    report = assignment.KPIReport('Revenue')
    assert report.title == 'Revenue'


def test_visualization_report_render():
    assert assignment.VisualizationReport('Trend').render() == 'Visualization Report: Trend'


def test_recommendation_report_render():
    assert assignment.RecommendationReport('Next Steps').render() == 'Recommendation Report: Next Steps'


def test_polymorphism_different_outputs():
    reports = [
        assignment.AnalyticsReport('X'),
        assignment.KPIReport('X'),
        assignment.VisualizationReport('X'),
        assignment.RecommendationReport('X'),
    ]
    rendered = [r.render() for r in reports]
    # All four should produce different strings
    assert len(set(rendered)) == 4


def test_kpi_report_is_analytics_report():
    report = assignment.KPIReport('Sales')
    assert isinstance(report, assignment.AnalyticsReport)


def test_visualization_report_is_analytics_report():
    report = assignment.VisualizationReport('Chart')
    assert isinstance(report, assignment.AnalyticsReport)


def test_recommendation_report_is_analytics_report():
    report = assignment.RecommendationReport('Tips')
    assert isinstance(report, assignment.AnalyticsReport)


def test_visualization_report_title_stored():
    report = assignment.VisualizationReport('Sales Trend')
    assert report.title == 'Sales Trend'


def test_recommendation_report_title_stored():
    report = assignment.RecommendationReport('Action Items')
    assert report.title == 'Action Items'


def test_analytics_report_render_is_string():
    assert isinstance(assignment.AnalyticsReport('x').render(), str)


def test_all_render_contain_title():
    title = 'DataTest'
    reports = [
        assignment.AnalyticsReport(title),
        assignment.KPIReport(title),
        assignment.VisualizationReport(title),
        assignment.RecommendationReport(title),
    ]
    for r in reports:
        assert title in r.render()
