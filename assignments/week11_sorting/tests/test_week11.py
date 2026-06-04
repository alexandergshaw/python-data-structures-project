"""Tests for Week 11: Sorting Algorithms."""

import importlib

assignment = importlib.import_module('assignments.week11_sorting.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_week11_sorting_functions():
    data = [{'score': 3}, {'score': 1}, {'score': 2}]
    assert [item['score'] for item in assignment.bubble_sort(data, 'score')] == [1, 2, 3]
    comparisons = assignment.compare_sort_algorithms(data, 'score')
    assert [item['score'] for item in comparisons['quick']] == [1, 2, 3]
