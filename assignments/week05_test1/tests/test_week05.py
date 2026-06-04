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


def test_describe_dataset_basic():
    data = [{'score': 10}, {'score': 20}, {'score': 15}]
    assert assignment.describe_dataset(data) == {'records': 3, 'columns': 1}


def test_describe_dataset_empty():
    assert assignment.describe_dataset([]) == {'records': 0, 'columns': 0}


def test_filter_by_value_basic():
    data = [{'score': 10}, {'score': 20}, {'score': 15}]
    result = assignment.filter_by_value(data, 'score', 15)
    assert len(result) == 2


def test_filter_by_value_all_below():
    data = [{'score': 5}, {'score': 8}]
    assert assignment.filter_by_value(data, 'score', 10) == []


def test_filter_by_value_exact_threshold():
    data = [{'score': 10}]
    assert len(assignment.filter_by_value(data, 'score', 10)) == 1


def test_rank_items_first():
    data = [{'score': 10}, {'score': 20}, {'score': 15}]
    assert assignment.rank_items(data, 'score')[0]['score'] == 20


def test_rank_items_last():
    data = [{'score': 10}, {'score': 20}, {'score': 15}]
    assert assignment.rank_items(data, 'score')[-1]['score'] == 10


def test_rank_items_length_unchanged():
    data = [{'score': 10}, {'score': 20}, {'score': 15}]
    assert len(assignment.rank_items(data, 'score')) == 3

