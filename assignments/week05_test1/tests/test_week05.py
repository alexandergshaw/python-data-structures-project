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


def test_is_anagram_true():
    assert assignment.is_anagram("listen", "silent") is True


def test_is_anagram_false():
    assert assignment.is_anagram("hello", "world") is False


def test_is_anagram_case_insensitive():
    assert assignment.is_anagram("Listen", "Silent") is True


def test_find_max_basic():
    assert assignment.find_max([3, 1, 4, 1, 5, 9]) == 9


def test_find_max_negatives():
    assert assignment.find_max([-5, -1, -3]) == -1


def test_find_max_empty():
    assert assignment.find_max([]) is None


def test_find_max_single():
    assert assignment.find_max([42]) == 42


def test_reverse_string_basic():
    assert assignment.reverse_string("hello") == "olleh"


def test_reverse_string_mixed_case():
    assert assignment.reverse_string("Python") == "nohtyP"


def test_reverse_string_empty():
    assert assignment.reverse_string("") == ""


def test_merge_dicts_basic():
    result = assignment.merge_dicts({"a": 1, "b": 2}, {"b": 99, "c": 3})
    assert result == {"a": 1, "b": 99, "c": 3}


def test_merge_dicts_no_overlap():
    assert assignment.merge_dicts({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}


def test_merge_dicts_empty_first():
    assert assignment.merge_dicts({}, {"x": 10}) == {"x": 10}
