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


def test_review_checklist_contains_arrays():
    assert 'arrays' in assignment.review_checklist()


def test_review_checklist_contains_sorting():
    assert 'sorting' in assignment.review_checklist()


def test_review_checklist_contains_all_six():
    checklist = assignment.review_checklist()
    expected = {'arrays', 'linked lists', 'stacks', 'queues', 'searching', 'sorting'}
    assert expected.issubset(set(checklist))


def test_score_readiness_half():
    assert assignment.score_readiness(3, 6) == 50.0


def test_score_readiness_full():
    assert assignment.score_readiness(6, 6) == 100.0


def test_score_readiness_zero_completed():
    assert assignment.score_readiness(0, 6) == 0.0


def test_score_readiness_zero_total():
    assert assignment.score_readiness(0, 0) == 0.0

