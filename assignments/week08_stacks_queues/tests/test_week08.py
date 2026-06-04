"""Tests for Week 08: Stacks and Queues."""

import importlib

assignment = importlib.import_module('assignments.week08_stacks_queues.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


def test_week8_stack_queue_pipeline():
    stack = assignment.Stack()
    stack.push('a')
    assert stack.pop() == 'a'
    queue = assignment.Queue()
    queue.enqueue('x')
    assert queue.dequeue() == 'x'
    pipeline = assignment.DataPipeline()
    pipeline.add_step('extract')
    assert pipeline.run() == ['extract']
