"""Tests for Week 03: Collections and Classes."""

import importlib

assignment = importlib.import_module('assignments.week03_collections_classes.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_week3_classes_work():
    dataset = assignment.Dataset('sales')
    dataset.add_record({'id': 1, 'amount': 50})
    assert dataset.get_summary()['records'] == 1
    kpi = assignment.KPI('Revenue')
    assert kpi.calculate([10, 20, 30]) == 20
    assert kpi.format_value() == '20.00'
