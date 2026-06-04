"""Tests for Week 12: Algorithms and Data Structures Review."""

import importlib

assignment = importlib.import_module('assignments.week12_review.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_week12_review_helpers():
    checklist = assignment.review_checklist()
    assert 'arrays' in checklist
    assert assignment.score_readiness(3, 6) == 50.0
