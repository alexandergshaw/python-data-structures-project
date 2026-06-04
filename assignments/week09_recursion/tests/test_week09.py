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


def test_recursive_sum_basic():
    assert assignment.recursive_sum([1, 2, 3]) == 6


def test_recursive_sum_empty():
    assert assignment.recursive_sum([]) == 0


def test_recursive_sum_single():
    assert assignment.recursive_sum([5]) == 5


def test_recursive_search_found():
    assert assignment.recursive_search(['a', 'b', 'c'], 'b') == 1


def test_recursive_search_not_found():
    assert assignment.recursive_search(['a', 'b', 'c'], 'z') == -1


def test_recursive_search_first_element():
    assert assignment.recursive_search([10, 20, 30], 10) == 0


def test_flatten_nested_basic():
    assert assignment.flatten_nested([1, [2, [3]]]) == [1, 2, 3]


def test_flatten_nested_already_flat():
    assert assignment.flatten_nested([1, 2, 3]) == [1, 2, 3]


def test_flatten_nested_empty():
    assert assignment.flatten_nested([]) == []


def test_recursive_count_nested():
    assert assignment.recursive_count([1, [2, [3]]]) == 3


def test_recursive_count_flat():
    assert assignment.recursive_count([1, 2, 3, 4]) == 4

