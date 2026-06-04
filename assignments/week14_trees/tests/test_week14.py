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


def test_insert_root():
    tree = assignment.BinarySearchTree()
    tree.insert(10)
    assert tree.root.value == 10


def test_search_found():
    tree = assignment.BinarySearchTree()
    for v in [10, 5, 15, 12]:
        tree.insert(v)
    assert tree.search(12) is True


def test_search_not_found():
    tree = assignment.BinarySearchTree()
    tree.insert(10)
    assert tree.search(99) is False


def test_inorder_sorted():
    tree = assignment.BinarySearchTree()
    for v in [10, 5, 15, 12]:
        tree.insert(v)
    assert tree.inorder() == [5, 10, 12, 15]


def test_preorder_root_first():
    tree = assignment.BinarySearchTree()
    for v in [10, 5, 15]:
        tree.insert(v)
    assert tree.preorder()[0] == 10


def test_postorder_root_last():
    tree = assignment.BinarySearchTree()
    for v in [10, 5, 15]:
        tree.insert(v)
    assert tree.postorder()[-1] == 10


def test_get_height_empty():
    tree = assignment.BinarySearchTree()
    assert tree.get_height() == 0


def test_get_height_single():
    tree = assignment.BinarySearchTree()
    tree.insert(10)
    assert tree.get_height() == 1


def test_get_height_multi():
    tree = assignment.BinarySearchTree()
    for v in [10, 5, 15, 12]:
        tree.insert(v)
    assert tree.get_height() >= 2


def test_insert_left_child():
    tree = assignment.BinarySearchTree()
    tree.insert(10)
    tree.insert(5)
    assert tree.root.left.value == 5


def test_insert_right_child():
    tree = assignment.BinarySearchTree()
    tree.insert(10)
    tree.insert(15)
    assert tree.root.right.value == 15


def test_search_left_subtree():
    tree = assignment.BinarySearchTree()
    for v in [10, 5, 3, 7]:
        tree.insert(v)
    assert tree.search(3) is True
    assert tree.search(7) is True


def test_inorder_full_result():
    tree = assignment.BinarySearchTree()
    for v in [10, 5, 15]:
        tree.insert(v)
    assert tree.inorder() == [5, 10, 15]


def test_preorder_full_result():
    tree = assignment.BinarySearchTree()
    for v in [10, 5, 15]:
        tree.insert(v)
    assert tree.preorder() == [10, 5, 15]


def test_postorder_full_result():
    tree = assignment.BinarySearchTree()
    for v in [10, 5, 15]:
        tree.insert(v)
    assert tree.postorder() == [5, 15, 10]


def test_get_height_skewed():
    tree = assignment.BinarySearchTree()
    for v in [10, 15, 20, 25]:
        tree.insert(v)
    assert tree.get_height() == 4


def test_inorder_empty():
    tree = assignment.BinarySearchTree()
    assert tree.inorder() == []
