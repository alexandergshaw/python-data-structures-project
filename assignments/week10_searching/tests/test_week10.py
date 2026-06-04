"""Tests for Week 10: Searching Algorithms."""

import importlib

assignment = importlib.import_module('assignments.week10_searching.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_week10_searching_functions():
    data = [{'id': 1}, {'id': 2}, {'id': 3}]
    assert assignment.linear_search(data, 2, 'id') == 1
    assert assignment.binary_search(data, 3, 'id') == 2
    comparison = assignment.compare_search_algorithms(data, 1, 'id')
    assert comparison['linear_index'] == 0
