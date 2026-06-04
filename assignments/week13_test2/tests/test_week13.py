"""Tests for Week 13: Comprehensive Test 2 Prep."""

import importlib

assignment = importlib.import_module('assignments.week13_test2.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_week13_test2_helpers():
    stats = assignment.evaluate_skills([80, 90])
    assert stats['average'] == 85.0
    assert assignment.next_study_topic({'trees': 70, 'sorting': 60}) == 'sorting'
