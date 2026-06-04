"""Tests for Week 06: Big O Analysis."""

import importlib

assignment = importlib.import_module('assignments.week06_big_o.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_time_function_returns_float():
    elapsed = assignment.time_function(sum, [1, 2, 3])
    assert isinstance(elapsed, float)


def test_time_function_non_negative():
    elapsed = assignment.time_function(sum, [1, 2, 3])
    assert elapsed >= 0


def test_compare_operations_size_field():
    results = assignment.compare_operations([10, 20])
    assert results[0]['size'] == 10
    assert results[1]['size'] == 20


def test_compare_operations_operations_field():
    results = assignment.compare_operations([10, 20])
    assert results[0]['operations'] == 20
    assert results[1]['operations'] == 40


def test_compare_operations_length():
    results = assignment.compare_operations([5, 10, 15])
    assert len(results) == 3


def test_generate_complexity_report_contains_analyzed():
    results = assignment.compare_operations([10, 20])
    report = assignment.generate_complexity_report(results)
    assert 'Analyzed' in report


def test_generate_complexity_report_contains_count():
    results = assignment.compare_operations([10, 20])
    report = assignment.generate_complexity_report(results)
    assert '2' in report

