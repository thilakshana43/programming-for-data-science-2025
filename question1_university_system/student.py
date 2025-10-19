# Imports the Person class to inherit from it.
from question1_university_system.person import Person

class Student(Person):
    def __init__(self, person_id: str, name: str, email: str, program: str):
        # Calls the parent constructor to initialize common fields.
        super().__init__(person_id, name, email)
        # Adds student-specific attributes.
        self.program = program
        self.courses = {}          #  Dictionary to store course_code and grade.{course_code: grade}
        self._gpa_history = {}     # Private-like attribute to store semester GPAs.{semester: gpa}

    def enroll_course(self, course_code: str):
        # Prevent duplicate enrollments.
        if course_code in self.courses:
            print(f"Already enrolled in {course_code}")
            return False
        # Enroll new course with 'None' as placeholder grade.
        self.courses[course_code] = None
        return True

    def drop_course(self, course_code: str):
        # Prevent dropping a course not enrolled.
        if course_code not in self.courses:
            print(f"Not enrolled in {course_code}")
            return False
        # Remove course from dictionary.
        del self.courses[course_code]
        return True

    def record_grade(self, course_code: str, grade: float):
        # Ensures student must be enrolled before adding a grade.
        if course_code not in self.courses:
            raise ValueError("Not enrolled in course")
        # Input validation for GPA range.
        if not (0.0 <= grade <= 4.0):
            raise ValueError("Grade must be 0.0–4.0")
        self.courses[course_code] = grade   # Save grade

    def calculate_gpa(self) -> float:
        # Extracts valid grades (ignoring None).
        grades = [g for g in self.courses.values() if g is not None]
        # Avoids division by zero.
        return sum(grades) / len(grades) if grades else 0.0

    def add_semester_gpa(self, semester: str, gpa: float):
        if not (0.0 <= gpa <= 4.0):     # Validate GPA input
            raise ValueError("GPA must be 0.0–4.0")
        self._gpa_history[semester] = gpa           # Store GPA for a semester

    # Calculate cumulative GPA from all semesters
    def cumulative_gpa(self) -> float:
        return sum(self._gpa_history.values()) / len(self._gpa_history) if self._gpa_history else 0.0

    def get_academic_status(self) -> str:
        gpa = self.cumulative_gpa()
        # Uses conditional logic to classify academic performance.
        if gpa >= 3.5:
            return "Dean's List"
        if gpa >= 2.0:
            return "Good Standing"
        return "Probation"

    # Overrides base class method to provide student-specific responsibilities.
    def get_responsibilities(self) -> str:
        return "Attend classes, submit assignments, study for exams."


class UndergraduateStudent(Student):
    # Calls parent constructor and specifies the program type.
    def __init__(self, person_id: str, name: str, email: str, major: str):
        super().__init__(person_id, name, email, program="Undergraduate")
        self.major = major      # Specific major for undergraduate students
    # Overrides base class method
    def get_responsibilities(self) -> str:
        return "Complete undergrad coursework, attend labs, projects."


class GraduateStudent(Student):
    def __init__(self, person_id: str, name: str, email: str, research_area: str):
        super().__init__(person_id, name, email, program="Graduate")    # Fixed program type
        self.research_area = research_area      # Research area for graduate students

    def get_responsibilities(self) -> str:
        # Specific responsibilities for graduate students
        return "Conduct research, write thesis, assist in teaching."

# Demonstrates encapsulation and data validation
class SecureStudentRecord:
    def __init__(self, student: Student, max_courses: int = 6):
        # Composition: contains a Student object.
        self._student = student
        # Private attributes use double underscore.
        self.__gpa_history = dict(student._gpa_history)
        self.__max_courses = max_courses        #course limit

    def enroll_course(self, course_code: str):
        # Checks for enrollment limits.
        if len(self._student.courses) >= self.__max_courses:
            raise ValueError("Enrollment limit reached")
        return self._student.enroll_course(course_code)

    def set_semester_gpa(self, semester: str, gpa: float):
        # Validates input range before updating.
        if not (0.0 <= gpa <= 4.0):
            raise ValueError("GPA must be 0.0–4.0")
        self.__gpa_history[semester] = gpa
        self._student._gpa_history[semester] = gpa       # Synchronize with student record

    def get_cumulative_gpa(self) -> float:
        # Calculates GPA privately for encapsulated data.
        return sum(self.__gpa_history.values()) / len(self.__gpa_history) if self.__gpa_history else 0.0
