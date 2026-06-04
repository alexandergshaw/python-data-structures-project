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


def test_stack_push_and_pop():
    stack = assignment.Stack()
    stack.push('a')
    assert stack.pop() == 'a'


def test_stack_lifo_order():
    stack = assignment.Stack()
    stack.push('first')
    stack.push('second')
    assert stack.pop() == 'second'


def test_stack_push_multiple():
    stack = assignment.Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3


def test_queue_enqueue_and_dequeue():
    queue = assignment.Queue()
    queue.enqueue('x')
    assert queue.dequeue() == 'x'


def test_queue_fifo_order():
    queue = assignment.Queue()
    queue.enqueue('first')
    queue.enqueue('second')
    assert queue.dequeue() == 'first'


def test_pipeline_add_and_run():
    pipeline = assignment.DataPipeline()
    pipeline.add_step('extract')
    assert pipeline.run() == ['extract']


def test_pipeline_multiple_steps():
    pipeline = assignment.DataPipeline()
    pipeline.add_step('extract')
    pipeline.add_step('transform')
    pipeline.add_step('load')
    assert pipeline.run() == ['extract', 'transform', 'load']


def test_pipeline_run_returns_copy():
    pipeline = assignment.DataPipeline()
    pipeline.add_step('step1')
    result = pipeline.run()
    result.append('extra')
    assert len(pipeline.run()) == 1

