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


def test_week15_polymorphism_classes():
    assert assignment.AnalyticsReport('Overview').render() == 'Analytics Report: Overview'
    assert assignment.KPIReport('Revenue').render() == 'KPI Report: Revenue'
    assert assignment.VisualizationReport('Trend').render() == 'Visualization Report: Trend'
    assert assignment.RecommendationReport('Next Steps').render() == 'Recommendation Report: Next Steps'
