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


def test_week6_big_o_functions():
    elapsed = assignment.time_function(sum, [1, 2, 3])
    assert elapsed >= 0
    results = assignment.compare_operations([10, 20])
    assert results[0]['size'] == 10
    assert 'Analyzed' in assignment.generate_complexity_report(results)
