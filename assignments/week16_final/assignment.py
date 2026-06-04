"""Week 16 assignment starter for Final Portfolio Build."""

WEEK_NUMBER = 16
TOPIC = 'Final Portfolio Build'
FEATURE_NAME = 'Recruiter View'

LEARNING_OBJECTIVES = [
    "Build a class with instance methods and control flow.",
    "Sort a list of objects by a computed attribute.",
    "Search a list using a linear scan.",
    "Write a recursive function with a base case.",
    "Summarize a collection of objects into a dictionary.",
]


# ---------------------------------------------------------------------------
# Task 1: Student class
# ---------------------------------------------------------------------------

class Student:
    """Represents a student with a name and a list of test scores."""

    def __init__(self, name: str, scores: list[int | float] | None = None) -> None:
        """Store the student's name and a copy of their scores.

        Example:
            >>> s = Student("Alice", [80, 90])
            >>> s.name
            'Alice'
            >>> s.scores
            [80, 90]
            >>> s2 = Student("Bob")
            >>> s2.scores
            []

        """
        self.name = None    # TODO
        self.scores = None  # TODO

    def add_score(self, score: int | float) -> None:
        """Append score to self.scores.

        Example:
            >>> s = Student("Alice")
            >>> s.add_score(95)
            >>> s.scores
            [95]

        """
        pass  # TODO

    def get_average(self) -> float:
        """Return the average of self.scores, or 0.0 if there are no scores.

        Example:
            >>> Student("Alice", [80, 100]).get_average()
            90.0
            >>> Student("Bob").get_average()
            0.0

        """
        if not self.scores:
            return 0.0
        return None  # TODO

    def get_letter_grade(self) -> str:
        """Return the letter grade based on get_average().

        Grade scale:
            >= 90 → 'A'
            >= 80 → 'B'
            >= 70 → 'C'
            >= 60 → 'D'
            < 60  → 'F'

        Example:
            >>> Student("Alice", [95]).get_letter_grade()
            'A'
            >>> Student("Bob", [55]).get_letter_grade()
            'F'

        """
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            pass  # TODO
        elif avg >= 70:
            pass  # TODO
        elif avg >= 60:
            pass  # TODO
        else:
            pass  # TODO


# ---------------------------------------------------------------------------
# Task 2: sort_students
# ---------------------------------------------------------------------------

def sort_students(students: list[Student]) -> list[Student]:
    """Return students sorted from highest to lowest average score.

    Example:
        >>> a = Student("Alice", [90])
        >>> b = Student("Bob", [70])
        >>> c = Student("Carol", [80])
        >>> [s.name for s in sort_students([a, b, c])]
        ['Alice', 'Carol', 'Bob']

    """
    return None  # TODO


# ---------------------------------------------------------------------------
# Task 3: find_student
# ---------------------------------------------------------------------------

def find_student(students: list[Student], name: str) -> Student | None:
    """Return the first Student whose name matches, or None if not found.

    Example:
        >>> a = Student("Alice", [90])
        >>> b = Student("Bob", [70])
        >>> find_student([a, b], "Bob").name
        'Bob'
        >>> find_student([a, b], "Carol") is None
        True

    """
    for student in students:
        if student.name == name:
            pass  # TODO
    return None


# ---------------------------------------------------------------------------
# Task 4: sum_recursive
# ---------------------------------------------------------------------------

def sum_recursive(numbers: list[int | float]) -> int | float:
    """Return the sum of numbers using recursion.

    Example:
        >>> sum_recursive([1, 2, 3, 4])
        10
        >>> sum_recursive([])
        0
        >>> sum_recursive([5])
        5

    """
    if not numbers:
        return 0
    return None  # TODO


# ---------------------------------------------------------------------------
# Task 5: grade_distribution
# ---------------------------------------------------------------------------

def grade_distribution(students: list[Student]) -> dict[str, int]:
    """Return a dict counting how many students received each letter grade.

    Only include grades that appear at least once.

    Example:
        >>> a = Student("Alice", [95])   # 'A'
        >>> b = Student("Bob", [85])     # 'B'
        >>> c = Student("Carol", [92])   # 'A'
        >>> grade_distribution([a, b, c])
        {'A': 2, 'B': 1}

    """
    dist = {}
    for student in students:
        grade = student.get_letter_grade()
        pass  # TODO
    return dist


# ---------------------------------------------------------------------------
# Boilerplate — do not change below this line
# ---------------------------------------------------------------------------

def is_complete() -> bool:
    """Return completion status for this week's assignment starter."""
    return False


def get_unlocked_feature() -> str:
    """Return the dashboard feature unlocked by this week."""
    return FEATURE_NAME


def get_week_summary() -> dict[str, object]:
    """Return a dashboard-friendly summary for this week."""
    return {
        'week': WEEK_NUMBER,
        'topic': TOPIC,
        'feature': FEATURE_NAME,
        'objectives': LEARNING_OBJECTIVES,
        'complete': is_complete(),
    }
