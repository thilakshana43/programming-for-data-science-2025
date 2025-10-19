# Contains Course and Department classes to manage university structure.

from question1_university_system.student import Student
from question1_university_system.faculty import Faculty

class Course:
    def __init__(self, code: str, title: str, credits: int, max_students: int = 30, prerequisites=None):
        self.code = code
        self.title = title
        self.credits = credits
        self.max_students = max_students
        self.prerequisites = prerequisites or []    # Avoid mutable default parameter issue
        self.enrolled_students = []                 # List of enrolled student IDs
        self.instructor_id = None                   # Faculty assigned to teach

    def has_capacity(self) -> bool:
        # Returns True if the course is not full
        return len(self.enrolled_students) < self.max_students

    def add_student(self, student: Student) -> bool:
        # Check prerequisite courses before adding student
        for prereq in self.prerequisites:
            grade = student.courses.get(prereq)
            if grade is None or grade < 2.0:
                raise ValueError(f"Missing/insufficient prereq {prereq}")
        # Check course capacity
        if not self.has_capacity():
            raise ValueError("Course capacity reached")
        # Enroll student if not already enrolled
        if student.person_id not in self.enrolled_students:
            self.enrolled_students.append(student.person_id)
            student.enroll_course(self.code)
            return True
        return False

    def assign_instructor(self, faculty: Faculty):
        # Assign a faculty member to the course
        self.instructor_id = faculty.person_id
        faculty.assign_course(self.code)


class Department:
    def __init__(self, name: str):
        self.name = name
        self.faculty = {}       # Dictionary of faculty {id: Faculty object}
        self.courses = {}       # Dictionary of courses {code: Course object}

    def add_faculty(self, faculty: Faculty):
        # Adds a faculty member to the department
        self.faculty[faculty.person_id] = faculty

    def create_course(self, course: Course):
        # Adds a new course to the department
        self.courses[course.code] = course

    def assign_faculty_to_course(self, faculty_id: str, course_code: str):
        # Assign faculty to a specific course
        self.courses[course_code].assign_instructor(self.faculty[faculty_id])

    def register_student(self, course_code: str, student: Student):
        # Register a student for a course
        return self.courses[course_code].add_student(student)
