"""Tests for Week 04: Review and Integration."""

import importlib

assignment = importlib.import_module('assignments.week04_review.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_week4_review_functions():
    combined = assignment.combine_datasets([{'id': 1}], [{'id': 2}])
    assert len(combined) == 2
    report = assignment.generate_report([[{'id': 1}], [{'id': 2}, {'id': 3}]])
    assert report['total_records'] == 3
    assert assignment.calculate_growth_rate(100, 125) == 25.0
