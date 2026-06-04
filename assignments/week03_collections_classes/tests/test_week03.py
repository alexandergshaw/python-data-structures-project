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


def test_dataset_name_stored():
    ds = assignment.Dataset('sales')
    assert ds.name == 'sales'


def test_dataset_starts_empty():
    ds = assignment.Dataset('test')
    assert len(ds.records) == 0


def test_dataset_add_record():
    ds = assignment.Dataset('sales')
    ds.add_record({'id': 1, 'amount': 50})
    assert len(ds.records) == 1


def test_dataset_get_summary_records():
    ds = assignment.Dataset('sales')
    ds.add_record({'id': 1, 'amount': 50})
    assert ds.get_summary()['records'] == 1


def test_dataset_get_summary_columns():
    ds = assignment.Dataset('sales')
    ds.add_record({'id': 1, 'amount': 50})
    assert ds.get_summary()['columns'] == 2


def test_dataset_get_summary_name():
    ds = assignment.Dataset('sales')
    assert ds.get_summary()['name'] == 'sales'


def test_kpi_calculate_average():
    kpi = assignment.KPI('Revenue')
    result = kpi.calculate([10, 20, 30])
    assert result == 20.0


def test_kpi_calculate_stores_value():
    kpi = assignment.KPI('Revenue')
    kpi.calculate([10, 20, 30])
    assert kpi.value == 20.0


def test_kpi_calculate_empty():
    kpi = assignment.KPI('Revenue')
    assert kpi.calculate([]) == 0.0


def test_kpi_format_value():
    kpi = assignment.KPI('Revenue', 20.0)
    assert kpi.format_value() == '20.00'


def test_kpi_format_value_after_calculate():
    kpi = assignment.KPI('Revenue')
    kpi.calculate([10, 20, 30])
    assert kpi.format_value() == '20.00'

