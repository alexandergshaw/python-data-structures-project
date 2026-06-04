"""Tests for Week 16: Final Portfolio Build."""

import importlib

assignment = importlib.import_module('assignments.week16_final.assignment')


def test_is_complete_returns_boolean():
    assert isinstance(assignment.is_complete(), bool)


def test_get_week_summary_type():
    summary = assignment.get_week_summary()
    assert isinstance(summary, (str, dict))


def test_unlocked_feature_returns_string():
    assert isinstance(assignment.get_unlocked_feature(), str)


# --- Student class ---

def test_student_name_stored():
    s = assignment.Student("Alice")
    assert s.name == "Alice"


def test_student_scores_default_empty():
    s = assignment.Student("Alice")
    assert s.scores == []


def test_student_scores_stored():
    s = assignment.Student("Alice", [80, 90])
    assert s.scores == [80, 90]


def test_student_add_score():
    s = assignment.Student("Alice")
    s.add_score(95)
    assert s.scores == [95]


def test_student_get_average_basic():
    s = assignment.Student("Alice", [80, 100])
    assert s.get_average() == 90.0


def test_student_get_average_empty():
    s = assignment.Student("Bob")
    assert s.get_average() == 0.0


def test_student_get_letter_grade_a():
    s = assignment.Student("Alice", [95])
    assert s.get_letter_grade() == 'A'


def test_student_get_letter_grade_b():
    s = assignment.Student("Bob", [85])
    assert s.get_letter_grade() == 'B'


def test_student_get_letter_grade_c():
    s = assignment.Student("Carol", [75])
    assert s.get_letter_grade() == 'C'


def test_student_get_letter_grade_d():
    s = assignment.Student("Dave", [65])
    assert s.get_letter_grade() == 'D'


def test_student_get_letter_grade_f():
    s = assignment.Student("Eve", [50])
    assert s.get_letter_grade() == 'F'


# --- sort_students ---

def test_sort_students_order():
    a = assignment.Student("Alice", [90])
    b = assignment.Student("Bob", [70])
    c = assignment.Student("Carol", [80])
    result = assignment.sort_students([a, b, c])
    assert [s.name for s in result] == ["Alice", "Carol", "Bob"]


def test_sort_students_length():
    students = [assignment.Student(n, [s]) for n, s in [("A", 60), ("B", 90)]]
    assert len(assignment.sort_students(students)) == 2


# --- find_student ---

def test_find_student_found():
    a = assignment.Student("Alice", [90])
    b = assignment.Student("Bob", [70])
    result = assignment.find_student([a, b], "Bob")
    assert result is b


def test_find_student_not_found():
    a = assignment.Student("Alice", [90])
    assert assignment.find_student([a], "Zara") is None


# --- sum_recursive ---

def test_sum_recursive_basic():
    assert assignment.sum_recursive([1, 2, 3, 4]) == 10


def test_sum_recursive_empty():
    assert assignment.sum_recursive([]) == 0


def test_sum_recursive_single():
    assert assignment.sum_recursive([5]) == 5


# --- grade_distribution ---

def test_grade_distribution_basic():
    a = assignment.Student("Alice", [95])
    b = assignment.Student("Bob", [85])
    c = assignment.Student("Carol", [92])
    result = assignment.grade_distribution([a, b, c])
    assert result == {'A': 2, 'B': 1}


def test_grade_distribution_empty():
    assert assignment.grade_distribution([]) == {}


def test_grade_distribution_all_same():
    students = [assignment.Student(f"S{i}", [95]) for i in range(3)]
    result = assignment.grade_distribution(students)
    assert result == {'A': 3}

def test_student_scores_is_copy():
    original = [80, 90]
    s = assignment.Student("Alice", original)
    original.append(100)
    assert s.scores == [80, 90]


def test_student_add_multiple_scores():
    s = assignment.Student("Alice")
    s.add_score(70)
    s.add_score(80)
    assert s.scores == [70, 80]


def test_student_get_average_single():
    s = assignment.Student("Alice", [75])
    assert s.get_average() == 75.0


def test_student_get_letter_grade_boundary_b():
    s = assignment.Student("Alice", [90])
    assert s.get_letter_grade() == 'A'
    s2 = assignment.Student("Bob", [89])
    assert s2.get_letter_grade() == 'B'


def test_sort_students_empty():
    assert assignment.sort_students([]) == []


def test_sort_students_single():
    s = assignment.Student("Alice", [80])
    result = assignment.sort_students([s])
    assert len(result) == 1
    assert result[0].name == "Alice"


def test_find_student_first_in_list():
    a = assignment.Student("Alice", [90])
    b = assignment.Student("Bob", [70])
    result = assignment.find_student([a, b], "Alice")
    assert result is a


def test_sum_recursive_negatives():
    assert assignment.sum_recursive([-1, -2, -3]) == -6


def test_sum_recursive_floats():
    assert abs(assignment.sum_recursive([1.5, 2.5]) - 4.0) < 1e-9


def test_grade_distribution_all_grades():
    students = [
        assignment.Student("A", [95]),
        assignment.Student("B", [85]),
        assignment.Student("C", [75]),
        assignment.Student("D", [65]),
        assignment.Student("F", [55]),
    ]
    result = assignment.grade_distribution(students)
    assert result == {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'F': 1}


def test_grade_distribution_no_mutation():
    students = [assignment.Student("Alice", [95])]
    assignment.grade_distribution(students)
    assert students[0].scores == [95]
