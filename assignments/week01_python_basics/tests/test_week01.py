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


def test_count_records_basic():
    data = [{"id": 1, "name": "Ava"}, {"id": 2, "name": "Liam"}]
    assert assignment.count_records(data) == 2


def test_count_records_empty():
    assert assignment.count_records([]) == 0


def test_count_records_single():
    assert assignment.count_records([{"x": 1}]) == 1


def test_count_columns_basic():
    data = [{"id": 1, "name": "Ava"}]
    assert assignment.count_columns(data) == 2


def test_count_columns_empty():
    assert assignment.count_columns([]) == 0


def test_get_dataset_summary_keys():
    data = [{"id": 1}]
    result = assignment.get_dataset_summary(data, "sales")
    assert result["name"] == "sales"
    assert result["records"] == 1
    assert result["columns"] == 1


def test_get_dataset_summary_two_rows():
    data = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    result = assignment.get_dataset_summary(data, "test")
    assert result["records"] == 2
    assert result["columns"] == 2


def test_format_number_thousands():
    assert assignment.format_number(12000) == "12,000"


def test_format_number_millions():
    assert assignment.format_number(1000000) == "1,000,000"


def test_format_number_small():
    assert assignment.format_number(999) == "999"

