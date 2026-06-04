"""Tests for Week 00: Git Workflow."""

import importlib

assignment = importlib.import_module('assignments.week00_git_workflow.assignment')


def test_student_name_is_a_string():
    """STUDENT_NAME must be a string."""
    assert isinstance(assignment.STUDENT_NAME, str), (
        "STUDENT_NAME should be a string (text surrounded by quotes)."
    )


def test_student_name_is_not_empty():
    """STUDENT_NAME must not be blank."""
    assert len(assignment.STUDENT_NAME.strip()) > 0, (
        "STUDENT_NAME is empty. Enter your full name between the quotes."
    )


def test_student_name_is_not_john_doe():
    """STUDENT_NAME must be changed from the placeholder 'John Doe'."""
    assert assignment.STUDENT_NAME.strip() != "John Doe", (
        "STUDENT_NAME is still 'John Doe'. "
        "Open assignment.py and replace 'John Doe' with your own full name."
    )


def test_get_student_name_matches_variable():
    """get_student_name() must return the same value as STUDENT_NAME."""
    assert assignment.get_student_name() == assignment.STUDENT_NAME


def test_is_complete_returns_boolean():
    """is_complete() must return a boolean."""
    assert isinstance(assignment.is_complete(), bool)


def test_is_complete_is_true_after_name_change():
    """is_complete() must return True once STUDENT_NAME is not 'John Doe'."""
    assert assignment.is_complete() is True, (
        "is_complete() returned False. Make sure STUDENT_NAME is set to your real name."
    )


def test_get_week_summary_is_a_dict():
    """get_week_summary() must return a dict."""
    assert isinstance(assignment.get_week_summary(), dict)


def test_get_week_summary_contains_student_name():
    """get_week_summary() must include a 'student_name' key."""
    summary = assignment.get_week_summary()
    assert 'student_name' in summary, (
        "The summary dict is missing the 'student_name' key."
    )
