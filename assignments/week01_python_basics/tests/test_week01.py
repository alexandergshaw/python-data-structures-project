"""Tests for Week 01: Python Basics."""

import importlib

assignment = importlib.import_module('assignments.week01_python_basics.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_week1_functions_exist_and_work():
    data = [{'id': 1, 'name': 'Ava'}, {'id': 2, 'name': 'Liam'}]
    assert assignment.count_records(data) == 2
    assert assignment.count_columns(data) == 2
    assert assignment.get_dataset_summary(data, 'sample')['name'] == 'sample'
    assert assignment.format_number(12000) == '12,000'
