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


def test_bubble_sort_ascending():
    data = [{'score': 3}, {'score': 1}, {'score': 2}]
    result = assignment.bubble_sort(data, 'score')
    assert [item['score'] for item in result] == [1, 2, 3]


def test_bubble_sort_does_not_mutate():
    data = [{'score': 3}, {'score': 1}]
    assignment.bubble_sort(data, 'score')
    assert data[0]['score'] == 3  # original unchanged


def test_insertion_sort_ascending():
    data = [{'score': 3}, {'score': 1}, {'score': 2}]
    result = assignment.insertion_sort(data, 'score')
    assert [item['score'] for item in result] == [1, 2, 3]


def test_merge_sort_ascending():
    data = [{'score': 3}, {'score': 1}, {'score': 2}]
    result = assignment.merge_sort(data, 'score')
    assert [item['score'] for item in result] == [1, 2, 3]


def test_quick_sort_ascending():
    data = [{'score': 3}, {'score': 1}, {'score': 2}]
    result = assignment.quick_sort(data, 'score')
    assert [item['score'] for item in result] == [1, 2, 3]


def test_compare_sort_algorithms_keys():
    data = [{'score': 3}, {'score': 1}, {'score': 2}]
    comparisons = assignment.compare_sort_algorithms(data, 'score')
    assert set(comparisons.keys()) == {'bubble', 'insertion', 'merge', 'quick'}


def test_compare_sort_algorithms_results():
    data = [{'score': 3}, {'score': 1}, {'score': 2}]
    comparisons = assignment.compare_sort_algorithms(data, 'score')
    assert [item['score'] for item in comparisons['quick']] == [1, 2, 3]
    assert [item['score'] for item in comparisons['bubble']] == [1, 2, 3]


def test_bubble_sort_already_sorted():
    data = [{'score': 1}, {'score': 2}, {'score': 3}]
    result = assignment.bubble_sort(data, 'score')
    assert [item['score'] for item in result] == [1, 2, 3]


def test_bubble_sort_single():
    data = [{'score': 5}]
    result = assignment.bubble_sort(data, 'score')
    assert [item['score'] for item in result] == [5]


def test_insertion_sort_single():
    data = [{'score': 7}]
    result = assignment.insertion_sort(data, 'score')
    assert [item['score'] for item in result] == [7]


def test_merge_sort_does_not_mutate():
    data = [{'score': 3}, {'score': 1}]
    assignment.merge_sort(data, 'score')
    assert data[0]['score'] == 3


def test_quick_sort_larger():
    data = [{'score': i} for i in [5, 2, 8, 1, 9, 3]]
    result = assignment.quick_sort(data, 'score')
    assert [item['score'] for item in result] == [1, 2, 3, 5, 8, 9]


def test_compare_sort_all_same_result():
    data = [{'score': 3}, {'score': 1}, {'score': 2}]
    comparisons = assignment.compare_sort_algorithms(data, 'score')
    expected = [1, 2, 3]
    for key in ['bubble', 'insertion', 'merge', 'quick']:
        assert [item['score'] for item in comparisons[key]] == expected
