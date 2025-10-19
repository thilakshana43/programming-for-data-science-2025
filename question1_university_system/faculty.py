# Demonstrates inheritance and polymorphism for different faculty types
# Imports the Person class to inherit from it.
from question1_university_system.person import Person

class Faculty(Person):
    def __init__(self, person_id: str, name: str, email: str, department: str):
        # Calls the parent constructor to initialize common fields.
        super().__init__(person_id, name, email)
        self.department = department        # Department name
        self.assigned_courses = []          # List of course codes assigned

    def assign_course(self, course_code: str):
        # Assign new course if not already assigned
        if course_code not in self.assigned_courses:
            self.assigned_courses.append(course_code)
            return True
        return False

    def calculate_workload(self) -> float:
        # Generic workload: 3 hours per course
        return len(self.assigned_courses) * 3.0

    def get_responsibilities(self) -> str:
        # Base responsibility (will be overridden)
        return "Teach courses and advise students."


class Professor(Faculty):
    def calculate_workload(self) -> float:
        # Professors have additional workload
        return len(self.assigned_courses) * 4.5 + 8.0

    def get_responsibilities(self) -> str:
        # Specialized duties for Professors
        return "Lead research, teach advanced courses, supervise grads."


class Lecturer(Faculty):
    def calculate_workload(self) -> float:
        # Lecturers spend slightly more time per course
        return len(self.assigned_courses) * 3.5

    def get_responsibilities(self) -> str:
        # Duties specific to lecturers
        return "Deliver lectures and prepare course materials."


class TA(Faculty):
    def calculate_workload(self) -> float:
        # TAs have lighter workload compared to professors
        return len(self.assigned_courses) * 2.0

    def get_responsibilities(self) -> str:
        # Duties specific to TAs
        return "Assist labs, grade assignments, hold office hours."
