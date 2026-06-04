"""Tests for Week 07: Arrays and Linked Lists."""

import importlib

assignment = importlib.import_module('assignments.week07_arrays_linked_lists.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_dynamic_array_starts_empty():
    arr = assignment.DynamicArray()
    assert len(arr) == 0


def test_dynamic_array_append_one():
    arr = assignment.DynamicArray()
    arr.append(5)
    assert len(arr) == 1


def test_dynamic_array_append_multiple():
    arr = assignment.DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    assert len(arr) == 3


def test_dynamic_array_items_stored():
    arr = assignment.DynamicArray()
    arr.append(42)
    assert arr.items[0] == 42


def test_linked_list_starts_empty():
    ll = assignment.LinkedList()
    assert ll.to_list() == []


def test_linked_list_append_one():
    ll = assignment.LinkedList()
    ll.append(1)
    assert ll.to_list() == [1]


def test_linked_list_append_multiple():
    ll = assignment.LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]


def test_linked_list_head_value():
    ll = assignment.LinkedList()
    ll.append(99)
    assert ll.head.value == 99

