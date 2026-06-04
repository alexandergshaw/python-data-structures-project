"""Tests for Week 02: Control Flow."""

import importlib

assignment = importlib.import_module('assignments.week02_control_flow.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_week2_functions_exist_and_work():
    data = [{'value': 1}, {'value': ''}, {'value': 1}, {'value': 1}]
    assert assignment.find_missing_values(data) == 1
    assert assignment.find_duplicates(data) == 1
    assert assignment.validate_positive(0, 'value') is True
    assert assignment.count_valid_records(data) == 3
