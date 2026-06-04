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


def test_combine_datasets_length():
    combined = assignment.combine_datasets([{'id': 1}], [{'id': 2}])
    assert len(combined) == 2


def test_combine_datasets_order():
    combined = assignment.combine_datasets([{'id': 1}], [{'id': 2}, {'id': 3}])
    assert combined[0]['id'] == 1
    assert combined[2]['id'] == 3


def test_combine_datasets_empty_first():
    combined = assignment.combine_datasets([], [{'id': 1}])
    assert len(combined) == 1


def test_generate_report_dataset_count():
    report = assignment.generate_report([[{'id': 1}], [{'id': 2}, {'id': 3}]])
    assert report['dataset_count'] == 2


def test_generate_report_total_records():
    report = assignment.generate_report([[{'id': 1}], [{'id': 2}, {'id': 3}]])
    assert report['total_records'] == 3


def test_calculate_growth_rate_positive():
    assert assignment.calculate_growth_rate(100, 125) == 25.0


def test_calculate_growth_rate_negative():
    assert assignment.calculate_growth_rate(200, 150) == -25.0


def test_calculate_growth_rate_zero_old():
    assert assignment.calculate_growth_rate(0, 50) == 0.0

