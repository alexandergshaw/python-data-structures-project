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

        Examples:
            A student is created with a name and a list of scores:
                >>> s = Student("Alice", [80, 90])
                >>> s.name
                'Alice'
                >>> s.scores
                [80, 90]

            When no scores are provided, the list defaults to empty:
                >>> s2 = Student("Bob")
                >>> s2.scores
                []

            The stored scores are an independent copy — modifying the original
            list does not affect the student's scores:
                >>> original = [70, 80]
                >>> s = Student("Carol", original)
                >>> original.append(90)
                >>> s.scores
                [70, 80]

        Hints:
            - self.name = name
            - self.scores = scores[:] if scores is not None else []
        """
        self.name = None    # TODO: replace None — store name
        self.scores = None  # TODO: replace None — store a copy of scores, or [] if None

    def add_score(self, score: int | float) -> None:
        """Append score to self.scores.

        Examples:
            Adding a score to a new student creates a one-element scores list:
                >>> s = Student("Alice")
                >>> s.add_score(95)
                >>> s.scores
                [95]

            Multiple calls add scores in order:
                >>> s = Student("Alice")
                >>> s.add_score(80)
                >>> s.add_score(90)
                >>> s.scores
                [80, 90]

            Scores are appended to any pre-existing scores:
                >>> s = Student("Alice", [70])
                >>> s.add_score(85)
                >>> s.scores
                [70, 85]

        Hint:
            self.scores.append(score)
        """
        pass  # TODO: self.scores.append(score)

    def get_average(self) -> float:
        """Return the average of self.scores, or 0.0 if there are no scores.

        Examples:
            The average of 80 and 100 is 90.0:
                >>> Student("Alice", [80, 100]).get_average()
                90.0

            A student with no scores returns 0.0 (no division by zero):
                >>> Student("Bob").get_average()
                0.0

            A single score averages to itself:
                >>> Student("Carol", [75]).get_average()
                75.0

            Works with float scores:
                >>> Student("Dave", [88.5, 91.5]).get_average()
                90.0

        Hints:
            - Guard against empty: if not self.scores, return 0.0
            - Average = sum(self.scores) / len(self.scores)
        """
        if not self.scores:
            return 0.0
        return None  # TODO: replace None — return sum(self.scores) / len(self.scores)

    def get_letter_grade(self) -> str:
        """Return the letter grade based on get_average().

        Grade scale:
            >= 90 → 'A'
            >= 80 → 'B'
            >= 70 → 'C'
            >= 60 → 'D'
            < 60  → 'F'

        Examples:
            A score of 95 earns an 'A':
                >>> Student("Alice", [95]).get_letter_grade()
                'A'

            A score below 60 earns an 'F':
                >>> Student("Bob", [55]).get_letter_grade()
                'F'

            Exactly 90 is the threshold for an 'A':
                >>> Student("Carol", [90]).get_letter_grade()
                'A'

            A score of 89 falls into the 'B' range:
                >>> Student("Dave", [89]).get_letter_grade()
                'B'

            A student with no scores has an average of 0.0, which earns an 'F':
                >>> Student("Eve").get_letter_grade()
                'F'

        Hint:
            avg = self.get_average()
            Then use if/elif/else comparing avg to 90, 80, 70, 60.
        """
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            pass  # TODO: return 'B'
        elif avg >= 70:
            pass  # TODO: return 'C'
        elif avg >= 60:
            pass  # TODO: return 'D'
        else:
            pass  # TODO: return 'F'


# ---------------------------------------------------------------------------
# Task 2: sort_students
# ---------------------------------------------------------------------------

def sort_students(students: list[Student]) -> list[Student]:
    """Return students sorted from highest to lowest average score.

    Examples:
        Students are returned in descending order by average score:
            >>> a = Student("Alice", [90])
            >>> b = Student("Bob", [70])
            >>> c = Student("Carol", [80])
            >>> [s.name for s in sort_students([a, b, c])]
            ['Alice', 'Carol', 'Bob']

        An empty list returns an empty list:
            >>> sort_students([])
            []

        A single student is returned as-is:
            >>> s = Student("Alice", [85])
            >>> sort_students([s])[0].name
            'Alice'

        The original list is not modified — a new sorted list is returned:
            >>> a = Student("Alice", [90])
            >>> b = Student("Bob", [70])
            >>> original = [b, a]
            >>> sorted_list = sort_students(original)
            >>> original[0].name
            'Bob'

    Hint:
        Use sorted() with a key and reverse=True:
        sorted(students, key=lambda s: s.get_average(), reverse=True)
    """
    return None  # TODO: replace None — use sorted() with key=lambda s: s.get_average() and reverse=True


# ---------------------------------------------------------------------------
# Task 3: find_student
# ---------------------------------------------------------------------------

def find_student(students: list[Student], name: str) -> Student | None:
    """Return the first Student whose name matches, or None if not found.

    Examples:
        Returns the student whose name matches the search string:
            >>> a = Student("Alice", [90])
            >>> b = Student("Bob", [70])
            >>> find_student([a, b], "Bob").name
            'Bob'

        Returns None when no student has the given name:
            >>> a = Student("Alice", [90])
            >>> b = Student("Bob", [70])
            >>> find_student([a, b], "Carol") is None
            True

        An empty list always returns None:
            >>> find_student([], "Alice") is None
            True

        The first matching student is returned when there are duplicates:
            >>> a = Student("Alice", [90])
            >>> b = Student("Alice", [70])
            >>> find_student([a, b], "Alice").scores
            [90]

    Hints:
        1. Loop over students.
        2. If student.name == name, return that student.
        3. After the loop, return None.
    """
    for student in students:
        if student.name == name:
            pass  # TODO: return student
    return None


# ---------------------------------------------------------------------------
# Task 4: sum_recursive
# ---------------------------------------------------------------------------

def sum_recursive(numbers: list[int | float]) -> int | float:
    """Return the sum of numbers using recursion.

    Examples:
        Four numbers summed recursively:
            >>> sum_recursive([1, 2, 3, 4])
            10

        The base case — an empty list has a sum of zero:
            >>> sum_recursive([])
            0

        A single-element list returns that element:
            >>> sum_recursive([5])
            5

        Works with negative numbers:
            >>> sum_recursive([-1, -2, -3])
            -6

        Works with floats:
            >>> sum_recursive([1.5, 2.5])
            4.0

    Hints:
        Base case:  if not numbers, return 0
        Recursive:  return numbers[0] + sum_recursive(numbers[1:])
    """
    if not numbers:
        return 0
    return None  # TODO: replace None — return numbers[0] + sum_recursive(numbers[1:])


# ---------------------------------------------------------------------------
# Task 5: grade_distribution
# ---------------------------------------------------------------------------

def grade_distribution(students: list[Student]) -> dict[str, int]:
    """Return a dict counting how many students received each letter grade.

    Only include grades that appear at least once.

    Examples:
        Two 'A' students and one 'B' student:
            >>> a = Student("Alice", [95])   # 'A'
            >>> b = Student("Bob", [85])     # 'B'
            >>> c = Student("Carol", [92])   # 'A'
            >>> grade_distribution([a, b, c])
            {'A': 2, 'B': 1}

        An empty list returns an empty dict — no grades to count:
            >>> grade_distribution([])
            {}

        A single student produces a dict with exactly one entry:
            >>> grade_distribution([Student("Alice", [75])])
            {'C': 1}

        Students with no scores have average 0.0 and receive an 'F':
            >>> grade_distribution([Student("Alice"), Student("Bob")])
            {'F': 2}

    Hints:
        1. Start with dist = {}
        2. Loop over students.
        3. Get each student's letter grade.
        4. dist[grade] = dist.get(grade, 0) + 1
        5. Return dist.
    """
    dist = {}
    for student in students:
        grade = student.get_letter_grade()
        pass  # TODO: dist[grade] = dist.get(grade, 0) + 1
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
