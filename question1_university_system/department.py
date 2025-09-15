from question1_university_system.student import Student
from question1_university_system.faculty import Faculty

class Course:
    def __init__(self, code: str, title: str, credits: int, max_students: int = 30, prerequisites=None):
        self.code = code
        self.title = title
        self.credits = credits
        self.max_students = max_students
        self.prerequisites = prerequisites or []
        self.enrolled_students = []
        self.instructor_id = None

    def has_capacity(self) -> bool:
        return len(self.enrolled_students) < self.max_students

    def add_student(self, student: Student) -> bool:
        for prereq in self.prerequisites:
            grade = student.courses.get(prereq)
            if grade is None or grade < 2.0:
                raise ValueError(f"Missing/insufficient prereq {prereq}")
        if not self.has_capacity():
            raise ValueError("Course capacity reached")
        if student.person_id not in self.enrolled_students:
            self.enrolled_students.append(student.person_id)
            student.enroll_course(self.code)
            return True
        return False

    def assign_instructor(self, faculty: Faculty):
        self.instructor_id = faculty.person_id
        faculty.assign_course(self.code)


class Department:
    def __init__(self, name: str):
        self.name = name
        self.faculty = {}
        self.courses = {}

    def add_faculty(self, faculty: Faculty):
        self.faculty[faculty.person_id] = faculty

    def create_course(self, course: Course):
        self.courses[course.code] = course

    def assign_faculty_to_course(self, faculty_id: str, course_code: str):
        self.courses[course_code].assign_instructor(self.faculty[faculty_id])

    def register_student(self, course_code: str, student: Student):
        return self.courses[course_code].add_student(student)
