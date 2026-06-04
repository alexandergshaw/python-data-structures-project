"""Tests for Week 03: Collections and Classes."""

import importlib

assignment = importlib.import_module('assignments.week03_collections_classes.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_get_unique_items_numbers():
    assert assignment.get_unique_items([3, 1, 2, 1, 3]) == [1, 2, 3]


def test_get_unique_items_strings():
    assert assignment.get_unique_items(["b", "a", "b"]) == ["a", "b"]


def test_get_unique_items_already_unique():
    assert assignment.get_unique_items([1, 2, 3]) == [1, 2, 3]


def test_word_frequency_basic():
    assert assignment.word_frequency(["hi", "bye", "hi"]) == {"hi": 2, "bye": 1}


def test_word_frequency_empty():
    assert assignment.word_frequency([]) == {}


def test_word_frequency_all_same():
    assert assignment.word_frequency(["a", "a", "a"]) == {"a": 3}


def test_counter_default_start():
    c = assignment.Counter()
    assert c.count == 0


def test_counter_custom_start():
    c = assignment.Counter(10)
    assert c.count == 10


def test_counter_increment():
    c = assignment.Counter()
    c.increment()
    assert c.count == 1


def test_counter_increment_twice():
    c = assignment.Counter()
    c.increment()
    c.increment()
    assert c.count == 2


def test_counter_decrement():
    c = assignment.Counter(5)
    c.decrement()
    assert c.count == 4


def test_counter_reset():
    c = assignment.Counter(5)
    c.reset()
    assert c.count == 0


def test_counter_get_value():
    c = assignment.Counter(7)
    assert c.get_value() == 7

def test_get_unique_items_empty():
    assert assignment.get_unique_items([]) == []


def test_get_unique_items_single():
    assert assignment.get_unique_items([42]) == [42]


def test_get_unique_items_all_same():
    assert assignment.get_unique_items([7, 7, 7]) == [7]


def test_word_frequency_single():
    assert assignment.word_frequency(["hello"]) == {"hello": 1}


def test_word_frequency_multiple_unique():
    assert assignment.word_frequency(["a", "b", "c"]) == {"a": 1, "b": 1, "c": 1}


def test_counter_decrement_to_negative():
    c = assignment.Counter()
    c.decrement()
    assert c.count == -1


def test_counter_sequence():
    c = assignment.Counter(5)
    c.increment()
    c.decrement()
    c.decrement()
    assert c.count == 4


def test_counter_reset_after_increments():
    c = assignment.Counter()
    c.increment()
    c.increment()
    c.increment()
    c.reset()
    assert c.count == 0


def test_counter_get_value_after_operations():
    c = assignment.Counter(10)
    c.decrement()
    assert c.get_value() == 9
