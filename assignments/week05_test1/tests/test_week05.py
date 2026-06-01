"""Tests for Week 05: Test 1 Preparation."""

import importlib

assignment = importlib.import_module('assignments.week05_test1.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_week5_preparation_functions():
    data = [{'score': 10}, {'score': 20}, {'score': 15}]
    assert assignment.describe_dataset(data) == {'records': 3, 'columns': 1}
    assert len(assignment.filter_by_value(data, 'score', 15)) == 2
    assert assignment.rank_items(data, 'score')[0]['score'] == 20
