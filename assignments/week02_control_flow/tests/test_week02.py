"""Tests for Week 02: Control Flow."""

import importlib
import pytest

assignment = importlib.import_module('assignments.week02_control_flow.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_classify_number_positive():
    assert assignment.classify_number(5) == "positive"


def test_classify_number_negative():
    assert assignment.classify_number(-3) == "negative"


def test_classify_number_zero():
    assert assignment.classify_number(0) == "zero"


def test_fizzbuzz_fizzbuzz():
    assert assignment.fizzbuzz(15) == "FizzBuzz"


def test_fizzbuzz_fizz():
    assert assignment.fizzbuzz(9) == "Fizz"


def test_fizzbuzz_buzz():
    assert assignment.fizzbuzz(10) == "Buzz"


def test_fizzbuzz_other():
    assert assignment.fizzbuzz(7) == "7"


def test_count_positives_mixed():
    assert assignment.count_positives([1, -2, 3, 0, 5]) == 3


def test_count_positives_all_negative():
    assert assignment.count_positives([-1, -2]) == 0


def test_count_positives_empty():
    assert assignment.count_positives([]) == 0


def test_find_first_negative_found():
    assert assignment.find_first_negative([3, 1, -5, 2]) == -5


def test_find_first_negative_none():
    assert assignment.find_first_negative([1, 2, 3]) is None


def test_find_first_negative_first_element():
    assert assignment.find_first_negative([-1, 2, 3]) == -1

def test_classify_number_float_positive():
    assert assignment.classify_number(3.14) == "positive"


def test_classify_number_float_negative():
    assert assignment.classify_number(-0.1) == "negative"


def test_fizzbuzz_three():
    assert assignment.fizzbuzz(3) == "Fizz"


def test_fizzbuzz_five():
    assert assignment.fizzbuzz(5) == "Buzz"


def test_fizzbuzz_thirty():
    assert assignment.fizzbuzz(30) == "FizzBuzz"


def test_fizzbuzz_one():
    assert assignment.fizzbuzz(1) == "1"


def test_count_positives_all_positive():
    assert assignment.count_positives([1, 2, 3]) == 3


def test_count_positives_zero_not_counted():
    assert assignment.count_positives([0, 0, 0]) == 0


def test_find_first_negative_multiple_negatives():
    assert assignment.find_first_negative([-3, -1, -5]) == -3


def test_find_first_negative_last_element():
    assert assignment.find_first_negative([1, 2, -4]) == -4
