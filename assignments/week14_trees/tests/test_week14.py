"""Tests for Week 14: Trees."""

import importlib

assignment = importlib.import_module('assignments.week14_trees.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_week14_tree_structure():
    tree = assignment.BinarySearchTree()
    for value in [10, 5, 15, 12]:
        tree.insert(value)
    assert tree.search(12) is True
    assert tree.inorder() == [5, 10, 12, 15]
    assert tree.get_height() >= 2
