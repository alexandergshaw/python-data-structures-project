"""Tests for Week 09: Recursion."""

import importlib

assignment = importlib.import_module('assignments.week09_recursion.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_week9_recursion_functions():
    assert assignment.recursive_sum([1, 2, 3]) == 6
    assert assignment.recursive_search(['a', 'b', 'c'], 'b') == 1
    assert assignment.flatten_nested([1, [2, [3]]]) == [1, 2, 3]
    assert assignment.recursive_count([1, [2, [3]]]) == 3
