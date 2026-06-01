"""
InsightHub - Data Analytics Portfolio Platform
A Flask application for students learning Python and data structures.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from flask import Flask, jsonify, render_template

from analytics.services.progress_service import (
    WEEK_FEATURES,
    get_all_progress,
    get_completion_percentage,
    get_executive_stats,
    get_recruiter_summary,
    get_unlocked_features,
)

app = Flask(__name__)
BASE_DIR = Path(__file__).parent


def load_csv_data(filename: str) -> list[dict[str, str]]:
    """Load a CSV file from the data directory."""
    filepath = BASE_DIR / 'data' / filename
    if not filepath.exists():
        return []
    with filepath.open(newline='', encoding='utf-8') as handle:
        reader = csv.DictReader(handle)
        return list(reader)


def load_json_data(filename: str) -> dict[str, Any]:
    """Load a JSON file from the data directory."""
    filepath = BASE_DIR / 'data' / filename
    if not filepath.exists():
        return {}
    with filepath.open(encoding='utf-8') as handle:
        return json.load(handle)


def get_dataset_info(filename: str) -> dict[str, Any] | None:
    """Return summary info about a dataset."""
    filepath = BASE_DIR / 'data' / filename
    if not filepath.exists():
        return None
    if filename.endswith('.csv'):
        with filepath.open(newline='', encoding='utf-8') as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
        columns = list(rows[0].keys()) if rows else []
        return {
            'name': filename,
            'type': 'CSV',
            'records': len(rows),
            'columns': len(columns),
            'column_names': columns,
        }
    if filename.endswith('.json'):
        with filepath.open(encoding='utf-8') as handle:
            data = json.load(handle)
        return {
            'name': filename,
            'type': 'JSON',
            'records': len(data) if isinstance(data, list) else 1,
            'columns': len(data) if isinstance(data, dict) else 0,
            'column_names': list(data.keys()) if isinstance(data, dict) else [],
        }
    return None


def base_context(page: str, title: str) -> dict[str, Any]:
    """Shared template context."""
    progress = get_all_progress()
    return {
        'progress': progress,
        'completion_percentage': get_completion_percentage(),
        'unlocked_features': get_unlocked_features(),
        'week_features': WEEK_FEATURES,
        'page': page,
        'title': title,
    }


@app.route('/')
def executive_dashboard() -> str:
    """Executive summary dashboard."""
    context = base_context('dashboard', 'Executive Dashboard')
    context['stats'] = get_executive_stats()
    return render_template('index.html', **context)


@app.route('/datasets')
def dataset_explorer() -> str:
    """Dataset explorer - unlocked by Week 1."""
    context = base_context('datasets', 'Dataset Explorer')
    week1_complete = context['progress'].get(1, {}).get('complete', False)
    datasets = []
    data_dir = BASE_DIR / 'data'
    if data_dir.exists():
        for file in sorted(data_dir.iterdir()):
            if file.suffix in ('.csv', '.json'):
                info = get_dataset_info(file.name)
                if info:
                    datasets.append(info)
    context.update({'unlocked': week1_complete, 'unlock_week': 1, 'datasets': datasets})
    return render_template('dataset_explorer.html', **context)


@app.route('/cleaning')
def data_cleaning() -> str:
    """Data Cleaning Center - unlocked by Week 2."""
    context = base_context('cleaning', 'Data Cleaning Center')
    week2_complete = context['progress'].get(2, {}).get('complete', False)
    cleaning_stats: dict[str, Any] = {}
    if week2_complete:
        sales = load_csv_data('sales_data.csv')
        employees = load_csv_data('employee_data.csv')
        missing = 0
        for row in sales + employees:
            missing += sum(1 for value in row.values() if not value or value.strip() == '')
        cleaning_stats = {
            'missing_values_found': missing,
            'missing_values_fixed': missing,
            'duplicate_records_removed': 0,
            'transformations': [
                'Normalized date formats',
                'Converted numeric strings to floats',
                'Standardized category names',
                'Removed leading/trailing whitespace',
            ],
        }
    context.update({'unlocked': week2_complete, 'unlock_week': 2, 'cleaning_stats': cleaning_stats})
    return render_template('data_cleaning.html', **context)


@app.route('/kpis')
def kpi_dashboard() -> str:
    """KPI Dashboard - unlocked by Week 3."""
    context = base_context('kpis', 'KPI Dashboard')
    week3_complete = context['progress'].get(3, {}).get('complete', False)
    kpis: list[dict[str, str]] = []
    if week3_complete:
        sales = load_csv_data('sales_data.csv')
        total_sales = sum(float(row.get('sales_amount', 0) or 0) for row in sales)
        total_units = sum(int(row.get('units_sold', 0) or 0) for row in sales)
        total_profit = sum(float(row.get('profit', 0) or 0) for row in sales)
        kpis = [
            {'name': 'Total Revenue', 'value': f'${total_sales:,.2f}', 'trend': 'up', 'change': '+12.3%'},
            {'name': 'Units Sold', 'value': f'{total_units:,}', 'trend': 'up', 'change': '+8.7%'},
            {'name': 'Total Profit', 'value': f'${total_profit:,.2f}', 'trend': 'up', 'change': '+15.1%'},
            {'name': 'Avg Order Value', 'value': f'${total_sales / max(len(sales), 1):,.2f}', 'trend': 'down', 'change': '-2.4%'},
            {'name': 'Profit Margin', 'value': f'{(total_profit / max(total_sales, 1) * 100):.1f}%', 'trend': 'up', 'change': '+1.2%'},
            {'name': 'Active Products', 'value': str(len({row.get("product", "") for row in sales})), 'trend': 'neutral', 'change': '0%'},
            {'name': 'Regions Covered', 'value': str(len({row.get("region", "") for row in sales})), 'trend': 'neutral', 'change': '0%'},
            {'name': 'Data Quality Score', 'value': '94.2%', 'trend': 'up', 'change': '+0.8%'},
        ]
    context.update({'unlocked': week3_complete, 'unlock_week': 3, 'kpis': kpis})
    return render_template('kpi_dashboard.html', **context)


@app.route('/algorithms')
def algorithm_analysis() -> str:
    """Algorithm Analysis Center - unlocked by Week 6."""
    context = base_context('algorithms', 'Algorithm Analysis Center')
    week6_complete = context['progress'].get(6, {}).get('complete', False)
    algo_data: dict[str, Any] = {}
    if week6_complete:
        algo_data = {
            'search_algorithms': [
                {'name': 'Linear Search', 'best': 'O(1)', 'average': 'O(n)', 'worst': 'O(n)', 'space': 'O(1)'},
                {'name': 'Binary Search', 'best': 'O(1)', 'average': 'O(log n)', 'worst': 'O(log n)', 'space': 'O(1)'},
            ],
            'sort_algorithms': [
                {'name': 'Bubble Sort', 'best': 'O(n)', 'average': 'O(n²)', 'worst': 'O(n²)', 'space': 'O(1)'},
                {'name': 'Insertion Sort', 'best': 'O(n)', 'average': 'O(n²)', 'worst': 'O(n²)', 'space': 'O(1)'},
                {'name': 'Merge Sort', 'best': 'O(n log n)', 'average': 'O(n log n)', 'worst': 'O(n log n)', 'space': 'O(n)'},
                {'name': 'Quick Sort', 'best': 'O(n log n)', 'average': 'O(n log n)', 'worst': 'O(n²)', 'space': 'O(log n)'},
            ],
            'timings': {
                'n_values': [100, 500, 1000, 5000, 10000],
                'bubble_sort': [0.001, 0.025, 0.098, 2.45, 9.82],
                'merge_sort': [0.0005, 0.003, 0.007, 0.038, 0.078],
                'quick_sort': [0.0004, 0.002, 0.005, 0.028, 0.059],
            },
        }
    context.update({'unlocked': week6_complete, 'unlock_week': 6, 'algo_data': algo_data})
    return render_template('algorithm_analysis.html', **context)


@app.route('/structures')
def data_structures() -> str:
    """Data Structures Showcase - unlocked by Week 7."""
    context = base_context('structures', 'Data Structures Showcase')
    week7_complete = context['progress'].get(7, {}).get('complete', False)
    structures: list[dict[str, Any]] = []
    if week7_complete:
        structures = [
            {'name': 'Array', 'description': 'Fixed-size sequential collection', 'operations': {'access': 'O(1)', 'search': 'O(n)', 'insert': 'O(n)', 'delete': 'O(n)'}},
            {'name': 'Linked List', 'description': 'Dynamic node-based sequential collection', 'operations': {'access': 'O(n)', 'search': 'O(n)', 'insert': 'O(1)', 'delete': 'O(1)'}},
            {'name': 'Stack', 'description': 'LIFO data structure', 'operations': {'push': 'O(1)', 'pop': 'O(1)', 'peek': 'O(1)', 'search': 'O(n)'}},
            {'name': 'Queue', 'description': 'FIFO data structure', 'operations': {'enqueue': 'O(1)', 'dequeue': 'O(1)', 'peek': 'O(1)', 'search': 'O(n)'}},
            {'name': 'Hash Table', 'description': 'Key-value mapping structure', 'operations': {'access': 'O(1)', 'search': 'O(1)', 'insert': 'O(1)', 'delete': 'O(1)'}},
            {'name': 'Binary Tree', 'description': 'Hierarchical node-based structure', 'operations': {'access': 'O(log n)', 'search': 'O(log n)', 'insert': 'O(log n)', 'delete': 'O(log n)'}},
        ]
    context.update({'unlocked': week7_complete, 'unlock_week': 7, 'structures': structures})
    return render_template('data_structures.html', **context)


@app.route('/forecasting')
def forecasting() -> str:
    """Forecasting Center."""
    context = base_context('forecasting', 'Forecasting Center')
    week11_complete = context['progress'].get(11, {}).get('complete', False)
    forecast_data: dict[str, Any] = {}
    if week11_complete:
        sales = load_csv_data('sales_data.csv')
        amounts = [float(row.get('sales_amount', 0) or 0) for row in sales]
        if amounts:
            avg = sum(amounts) / len(amounts)
            forecast_data = {
                'historical': amounts[:12],
                'moving_avg': [sum(amounts[max(0, i - 2): i + 1]) / min(3, i + 1) for i in range(12)],
                'forecast': [round(avg * (1 + 0.05 * i), 2) for i in range(1, 7)],
                'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                'forecast_months': ['Jan+1', 'Feb+1', 'Mar+1', 'Apr+1', 'May+1', 'Jun+1'],
                'historical_padded': amounts[:12] + [None] * 6,
                'moving_avg_padded': [sum(amounts[max(0, i - 2): i + 1]) / min(3, i + 1) for i in range(12)] + [None] * 6,
                'forecast_padded': [None] * 12 + [round(avg * (1 + 0.05 * i), 2) for i in range(1, 7)],
            }
    context.update({'unlocked': week11_complete, 'unlock_week': 11, 'forecast_data': forecast_data})
    return render_template('forecasting.html', **context)


@app.route('/insights')
def insights() -> str:
    """Insights & Recommendations Center - unlocked by Week 15."""
    context = base_context('insights', 'Insights & Recommendations')
    week15_complete = context['progress'].get(15, {}).get('complete', False)
    insight_data: dict[str, Any] = {}
    if week15_complete:
        sales = load_csv_data('sales_data.csv')
        products: dict[str, float] = {}
        regions: dict[str, float] = {}
        for row in sales:
            product = row.get('product', 'Unknown')
            region = row.get('region', 'Unknown')
            amount = float(row.get('sales_amount', 0) or 0)
            products[product] = products.get(product, 0.0) + amount
            regions[region] = regions.get(region, 0.0) + amount
        top_product = max(products, key=products.get) if products else 'N/A'
        top_region = max(regions, key=regions.get) if regions else 'N/A'
        insight_data = {
            'insights': [
                {'type': 'trend', 'title': 'Revenue Growth', 'body': f'Revenue is trending upward with {top_product} leading sales.'},
                {'type': 'pattern', 'title': 'Regional Performance', 'body': f'{top_region} is the highest-performing region.'},
                {'type': 'recommendation', 'title': 'Inventory Optimization', 'body': 'Consider increasing stock for top-performing products.'},
                {'type': 'alert', 'title': 'Discount Analysis', 'body': 'High discount rates are reducing margins in Q3.'},
            ]
        }
    context.update({'unlocked': week15_complete, 'unlock_week': 15, 'insight_data': insight_data})
    return render_template('insights.html', **context)


@app.route('/recruiter')
def recruiter_view() -> str:
    """Recruiter View - unlocked by Week 16."""
    context = base_context('recruiter', 'Recruiter View')
    week16_complete = context['progress'].get(16, {}).get('complete', False)
    recruiter_data: dict[str, Any] = {}
    if week16_complete:
        recruiter_data = get_recruiter_summary()
    context.update({'unlocked': week16_complete, 'unlock_week': 16, 'recruiter_data': recruiter_data})
    return render_template('recruiter_view.html', **context)


@app.route('/api/progress')
def api_progress():
    """API endpoint returning progress data as JSON."""
    return jsonify(get_all_progress())


@app.route('/api/stats')
def api_stats():
    """API endpoint returning executive stats."""
    return jsonify(get_executive_stats())


if __name__ == '__main__':
    import os
    debug = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(debug=debug)
