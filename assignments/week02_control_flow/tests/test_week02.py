"""Tests for Week 02: Control Flow."""

import importlib
import pytest

assignment = importlib.import_module('assignments.week02_control_flow.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_find_missing_values_basic():
    data = [{'value': 1}, {'value': ''}, {'value': 1}, {'value': 1}]
    assert assignment.find_missing_values(data) == 1


def test_find_missing_values_none():
    data = [{'a': None, 'b': 1}]
    assert assignment.find_missing_values(data) == 1


def test_find_missing_values_none_present():
    data = [{'id': 1, 'name': None}, {'id': 2, 'name': 'Ava'}]
    assert assignment.find_missing_values(data) == 1


def test_find_missing_values_clean():
    data = [{'id': 1, 'name': 'Ava'}]
    assert assignment.find_missing_values(data) == 0


def test_find_duplicates_one_duplicate_pattern():
    data = [{'value': 1}, {'value': ''}, {'value': 1}, {'value': 1}]
    assert assignment.find_duplicates(data) == 1


def test_find_duplicates_no_duplicates():
    data = [{'x': 1}, {'x': 2}, {'x': 3}]
    assert assignment.find_duplicates(data) == 0


def test_validate_positive_zero():
    assert assignment.validate_positive(0, 'value') is True


def test_validate_positive_positive():
    assert assignment.validate_positive(5, 'price') is True


def test_validate_positive_negative_raises():
    with pytest.raises(ValueError):
        assignment.validate_positive(-1, 'price')


def test_count_valid_records_basic():
    data = [{'value': 1}, {'value': ''}, {'value': 1}, {'value': 1}]
    assert assignment.count_valid_records(data) == 3


def test_count_valid_records_all_valid():
    data = [{'id': 1, 'name': 'Ava'}, {'id': 2, 'name': 'Leo'}]
    assert assignment.count_valid_records(data) == 2


def test_count_valid_records_none_value():
    data = [{'id': 1, 'name': None}]
    assert assignment.count_valid_records(data) == 0

