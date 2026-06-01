"""Tests for Week 16: Final Portfolio Build."""

import importlib

assignment = importlib.import_module('assignments.week16_final.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_week16_final_functions():
    progress = {1: {'complete': True}, 2: {'complete': False}}
    assert assignment.generate_final_summary(progress) == {'completed': 1, 'total': 2}
    bullets = assignment.create_resume_bullets(['Python'])
    assert bullets[0].startswith('Applied Python')
    assert assignment.calculate_final_grade(16) == 'A'
