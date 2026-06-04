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


def test_evaluate_skills_single_score():
    stats = assignment.evaluate_skills([100])
    assert stats['total'] == 100
    assert stats['average'] == 100.0


def test_evaluate_skills_three_scores():
    stats = assignment.evaluate_skills([70, 80, 90])
    assert stats['total'] == 240
    assert stats['average'] == 80.0


def test_evaluate_skills_returns_dict():
    stats = assignment.evaluate_skills([90])
    assert isinstance(stats, dict)
    assert 'total' in stats
    assert 'average' in stats


def test_next_study_topic_returns_string():
    assert isinstance(assignment.next_study_topic({'a': 5}), str)


def test_next_study_topic_all_same():
    # Any key is acceptable when all scores are equal
    result = assignment.next_study_topic({'a': 50, 'b': 50})
    assert result in ('a', 'b')


def test_next_study_topic_not_highest():
    result = assignment.next_study_topic({'trees': 70, 'sorting': 60, 'arrays': 80})
    assert result == 'sorting'
