"""
InsightHub Progress Service
Tracks assignment completion and unlocks dashboard features.
"""
import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Any

# Map each week to the feature it unlocks
WEEK_FEATURES = {
    1: {
        "name": "Dataset Explorer",
        "route": "/datasets",
        "description": "Explore and analyze available datasets",
        "icon": "database",
    },
    2: {
        "name": "Data Cleaning Center",
        "route": "/cleaning",
        "description": "Clean and validate datasets",
        "icon": "broom",
    },
    3: {
        "name": "KPI Dashboard",
        "route": "/kpis",
        "description": "Key performance indicators and metrics",
        "icon": "chart-line",
    },
    4: {
        "name": "Analytics Progress Dashboard",
        "route": "/progress",
        "description": "Track your analytics progress",
        "icon": "tasks",
    },
    5: {
        "name": "Python Fundamentals Badge",
        "route": "/badge/python",
        "description": "Earned Python Fundamentals badge",
        "icon": "award",
    },
    6: {
        "name": "Algorithm Analysis Center",
        "route": "/algorithms",
        "description": "Analyze algorithm performance",
        "icon": "tachometer-alt",
    },
    7: {
        "name": "Data Structures Showcase",
        "route": "/structures",
        "description": "Data structures implementations",
        "icon": "sitemap",
    },
    8: {
        "name": "Data Pipeline Monitor",
        "route": "/pipeline",
        "description": "Monitor data processing pipelines",
        "icon": "stream",
    },
    9: {
        "name": "Nested Data Explorer",
        "route": "/nested",
        "description": "Explore nested and hierarchical data",
        "icon": "layer-group",
    },
    10: {
        "name": "Advanced Dataset Search",
        "route": "/search",
        "description": "Advanced search capabilities",
        "icon": "search",
    },
    11: {
        "name": "Ranking and Leaderboard Dashboard",
        "route": "/rankings",
        "description": "Rankings sorted by algorithms",
        "icon": "trophy",
    },
    12: {
        "name": "Algorithm Review Center",
        "route": "/algo-review",
        "description": "Review algorithm implementations",
        "icon": "redo",
    },
    13: {
        "name": "Data Structures Badge",
        "route": "/badge/structures",
        "description": "Earned Data Structures badge",
        "icon": "award",
    },
    14: {
        "name": "Hierarchy Visualization Center",
        "route": "/hierarchy",
        "description": "Visualize tree hierarchies",
        "icon": "project-diagram",
    },
    15: {
        "name": "Insights & Recommendations Center",
        "route": "/insights",
        "description": "AI-generated insights and recommendations",
        "icon": "lightbulb",
    },
    16: {
        "name": "Recruiter View",
        "route": "/recruiter",
        "description": "Professional portfolio for employers",
        "icon": "briefcase",
    },
}


def get_assignments_dir() -> Path:
    """Return path to assignments directory."""
    base = Path(__file__).parent.parent.parent
    return base / "assignments"


def load_assignment_module(week_dir: Path) -> ModuleType | None:
    """Dynamically load an assignment.py module."""
    assignment_file = week_dir / "assignment.py"
    if not assignment_file.exists():
        return None
    try:
        spec = importlib.util.spec_from_file_location(
            f"assignment_{week_dir.name}", str(assignment_file)
        )
        if spec is None or spec.loader is None:
            return None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception:
        return None


def check_week_completion(week_num: int) -> bool:
    """Check if a specific week's assignment is complete."""
    assignments_dir = get_assignments_dir()
    week_folders = sorted(assignments_dir.glob(f"week{week_num:02d}_*"))
    if not week_folders:
        return False
    week_dir = week_folders[0]
    module = load_assignment_module(week_dir)
    if module is None:
        return False
    try:
        return bool(module.is_complete())
    except Exception:
        return False


def get_all_progress() -> dict[int, dict[str, Any]]:
    """
    Return full progress data for all 16 weeks.
    Returns a dict with week numbers as keys.
    """
    progress: dict[int, dict[str, Any]] = {}
    assignments_dir = get_assignments_dir()

    for week_num in range(1, 17):
        week_folders = sorted(assignments_dir.glob(f"week{week_num:02d}_*"))
        feature = WEEK_FEATURES.get(week_num, {})

        if not week_folders:
            progress[week_num] = {
                "week": week_num,
                "folder": None,
                "complete": False,
                "feature": feature,
                "summary": None,
            }
            continue

        week_dir = week_folders[0]
        module = load_assignment_module(week_dir)
        complete = False
        summary: str | dict[str, Any] | None = None

        if module:
            try:
                complete = bool(module.is_complete())
            except Exception:
                complete = False
            try:
                summary = module.get_week_summary()
            except Exception:
                summary = None

        progress[week_num] = {
            "week": week_num,
            "folder": week_dir.name,
            "complete": complete,
            "feature": feature,
            "summary": summary,
        }

    return progress


def get_unlocked_features() -> list[str]:
    """Return list of unlocked feature names."""
    progress = get_all_progress()
    return [
        data["feature"]["name"]
        for _, data in progress.items()
        if data["complete"] and data["feature"]
    ]


def get_completion_percentage() -> int:
    """Return overall completion percentage (0-100)."""
    progress = get_all_progress()
    completed = sum(1 for d in progress.values() if d["complete"])
    return round((completed / 16) * 100)


def get_executive_stats() -> dict[str, int]:
    """Return stats for the executive dashboard."""
    progress = get_all_progress()
    completed_weeks = [w for w, d in progress.items() if d["complete"]]

    stats = {
        "total_records": 0,
        "datasets_loaded": 0,
        "kpis_generated": 0,
        "reports_generated": len(completed_weeks),
        "visualizations_generated": 0,
        "algorithms_completed": 0,
        "completion_percentage": get_completion_percentage(),
        "weeks_completed": len(completed_weeks),
        "total_weeks": 16,
    }

    data_dir = Path(__file__).parent.parent.parent / "data"
    if data_dir.exists():
        csv_files = list(data_dir.glob("*.csv"))
        json_files = list(data_dir.glob("*.json"))
        stats["datasets_loaded"] = len(csv_files) + len(json_files)

        for csv_file in csv_files:
            try:
                with csv_file.open() as handle:
                    lines = handle.readlines()
                    stats["total_records"] += max(0, len(lines) - 1)
            except Exception:
                pass

    algo_weeks = [6, 7, 10, 11, 14]
    stats["algorithms_completed"] = sum(
        1 for w in algo_weeks if progress.get(w, {}).get("complete", False)
    )

    if progress.get(3, {}).get("complete", False):
        stats["kpis_generated"] = 8

    viz_weeks = [3, 6, 11, 14, 15]
    stats["visualizations_generated"] = sum(
        1 for w in viz_weeks if progress.get(w, {}).get("complete", False)
    ) * 3

    return stats


def get_recruiter_summary() -> dict[str, Any]:
    """Return resume-ready summary for the recruiter view."""
    progress = get_all_progress()
    completed = [d for d in progress.values() if d["complete"]]

    skills: list[str] = []
    if any(d["week"] <= 2 for d in completed):
        skills.append("Python Programming (Variables, Loops, Functions)")
    if any(d["week"] == 3 for d in completed):
        skills.append("Object-Oriented Programming (Classes, Methods)")
    if any(d["week"] == 6 for d in completed):
        skills.append("Algorithm Analysis & Big O Notation")
    if any(d["week"] in [7, 8] for d in completed):
        skills.append("Data Structures (Arrays, Linked Lists, Stacks, Queues)")
    if any(d["week"] == 9 for d in completed):
        skills.append("Recursive Algorithms")
    if any(d["week"] in [10, 11] for d in completed):
        skills.append("Searching & Sorting Algorithms")
    if any(d["week"] == 14 for d in completed):
        skills.append("Tree Data Structures & Traversals")
    if any(d["week"] == 15 for d in completed):
        skills.append("Inheritance & Polymorphism")

    bullets: list[str] = []
    if completed:
        bullets.append(f"Completed {len(completed)} of 16 Python programming assignments")
        bullets.append("Built and deployed a full-stack analytics platform using Flask")
    if any(d["week"] >= 6 for d in completed):
        bullets.append(
            "Implemented and benchmarked sorting/searching algorithms with Big O analysis"
        )
    if any(d["week"] >= 7 for d in completed):
        bullets.append(
            "Built custom data structures: arrays, linked lists, stacks, queues, trees"
        )
    if any(d["week"] == 16 for d in completed):
        bullets.append(
            "Deployed live analytics dashboard to Vercel demonstrating full-stack Python skills"
        )

    return {
        "skills": skills,
        "bullets": bullets,
        "weeks_completed": len(completed),
        "completion_pct": get_completion_percentage(),
        "features_unlocked": get_unlocked_features(),
    }
