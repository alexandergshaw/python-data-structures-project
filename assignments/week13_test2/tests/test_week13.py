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


def test_evaluate_skills_average():
    stats = assignment.evaluate_skills([80, 90])
    assert stats['average'] == 85.0


def test_evaluate_skills_total():
    stats = assignment.evaluate_skills([80, 90])
    assert stats['total'] == 170


def test_evaluate_skills_empty():
    stats = assignment.evaluate_skills([])
    assert stats['total'] == 0
    assert stats['average'] == 0.0


def test_next_study_topic_lowest():
    assert assignment.next_study_topic({'trees': 70, 'sorting': 60}) == 'sorting'


def test_next_study_topic_single():
    assert assignment.next_study_topic({'recursion': 50}) == 'recursion'


def test_next_study_topic_empty():
    assert assignment.next_study_topic({}) == 'review'

