"""Tests for Week 07: Arrays and Linked Lists."""

import importlib

assignment = importlib.import_module('assignments.week07_arrays_linked_lists.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_week7_data_structures():
    dynamic = assignment.DynamicArray()
    dynamic.append(5)
    assert len(dynamic) == 1
    linked = assignment.LinkedList()
    linked.append(1)
    linked.append(2)
    assert linked.to_list() == [1, 2]
