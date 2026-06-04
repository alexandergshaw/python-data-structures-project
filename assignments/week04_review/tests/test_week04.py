"""Tests for Week 04: Review and Integration."""

import importlib

assignment = importlib.import_module('assignments.week04_review.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_is_palindrome_true():
    assert assignment.is_palindrome("racecar") is True


def test_is_palindrome_false():
    assert assignment.is_palindrome("hello") is False


def test_is_palindrome_single_char():
    assert assignment.is_palindrome("a") is True


def test_is_palindrome_empty():
    assert assignment.is_palindrome("") is True


def test_count_vowels_basic():
    assert assignment.count_vowels("hello") == 2


def test_count_vowels_uppercase():
    assert assignment.count_vowels("AEIOU") == 5


def test_count_vowels_no_vowels():
    assert assignment.count_vowels("gym") == 0


def test_clamp_within_range():
    assert assignment.clamp(5, 1, 10) == 5


def test_clamp_below_lo():
    assert assignment.clamp(-3, 0, 100) == 0


def test_clamp_above_hi():
    assert assignment.clamp(200, 0, 100) == 100


def test_summarize_basic():
    result = assignment.summarize([3, 1, 4, 1, 5])
    assert result == {"count": 5, "total": 14, "minimum": 1, "maximum": 5}


def test_summarize_empty():
    assert assignment.summarize([]) == {"count": 0, "total": 0, "minimum": 0, "maximum": 0}


def test_summarize_single():
    result = assignment.summarize([7])
    assert result["count"] == 1
    assert result["minimum"] == 7
    assert result["maximum"] == 7
