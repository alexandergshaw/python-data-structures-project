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


def test_generate_final_summary_counts_completed():
    progress = {1: {'complete': True}, 2: {'complete': False}}
    result = assignment.generate_final_summary(progress)
    assert result['completed'] == 1


def test_generate_final_summary_total():
    progress = {1: {'complete': True}, 2: {'complete': False}, 3: {'complete': True}}
    result = assignment.generate_final_summary(progress)
    assert result['total'] == 3


def test_generate_final_summary_all_complete():
    progress = {1: {'complete': True}, 2: {'complete': True}}
    result = assignment.generate_final_summary(progress)
    assert result['completed'] == 2


def test_create_resume_bullets_content():
    bullets = assignment.create_resume_bullets(['Python'])
    assert bullets[0] == 'Applied Python in InsightHub portfolio work.'


def test_create_resume_bullets_multiple():
    bullets = assignment.create_resume_bullets(['Python', 'Sorting'])
    assert len(bullets) == 2


def test_create_resume_bullets_empty():
    assert assignment.create_resume_bullets([]) == []


def test_calculate_final_grade_a():
    assert assignment.calculate_final_grade(16) == 'A'


def test_calculate_final_grade_b():
    assert assignment.calculate_final_grade(13) == 'B'


def test_calculate_final_grade_f():
    assert assignment.calculate_final_grade(0) == 'F'
