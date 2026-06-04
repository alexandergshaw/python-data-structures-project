"""Tests for Week 01: Python Basics."""

import importlib
import pytest

assignment = importlib.import_module('assignments.week01_python_basics.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_greet_basic():
    assert assignment.greet("Alice") == "Hello, Alice!"


def test_greet_different_name():
    assert assignment.greet("World") == "Hello, World!"


def test_greet_single_char():
    assert assignment.greet("X") == "Hello, X!"


def test_add_integers():
    assert assignment.add(3, 4) == 7


def test_add_floats():
    assert assignment.add(1.5, 2.5) == 4.0


def test_add_negative():
    assert assignment.add(-1, 1) == 0


def test_is_even_even():
    assert assignment.is_even(4) is True


def test_is_even_odd():
    assert assignment.is_even(7) is False


def test_is_even_zero():
    assert assignment.is_even(0) is True


def test_celsius_to_fahrenheit_zero():
    assert assignment.celsius_to_fahrenheit(0) == 32.0


def test_celsius_to_fahrenheit_hundred():
    assert assignment.celsius_to_fahrenheit(100) == 212.0


def test_celsius_to_fahrenheit_negative_forty():
    assert assignment.celsius_to_fahrenheit(-40) == -40.0
