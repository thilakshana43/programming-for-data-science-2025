from question1_university_system.person import Person

class Student(Person):
    def __init__(self, person_id: str, name: str, email: str, program: str):
        super().__init__(person_id, name, email)
        self.program = program
        self.courses = {}          # {course_code: grade}
        self._gpa_history = {}     # {semester: gpa}

    def enroll_course(self, course_code: str):
        if course_code in self.courses:
            print(f"Already enrolled in {course_code}")
            return False
        self.courses[course_code] = None
        return True

    def drop_course(self, course_code: str):
        if course_code not in self.courses:
            print(f"Not enrolled in {course_code}")
            return False
        del self.courses[course_code]
        return True

    def record_grade(self, course_code: str, grade: float):
        if course_code not in self.courses:
            raise ValueError("Not enrolled in course")
        if not (0.0 <= grade <= 4.0):
            raise ValueError("Grade must be 0.0–4.0")
        self.courses[course_code] = grade

    def calculate_gpa(self) -> float:
        grades = [g for g in self.courses.values() if g is not None]
        return sum(grades) / len(grades) if grades else 0.0

    def add_semester_gpa(self, semester: str, gpa: float):
        if not (0.0 <= gpa <= 4.0):
            raise ValueError("GPA must be 0.0–4.0")
        self._gpa_history[semester] = gpa

    def cumulative_gpa(self) -> float:
        return sum(self._gpa_history.values()) / len(self._gpa_history) if self._gpa_history else 0.0

    def get_academic_status(self) -> str:
        gpa = self.cumulative_gpa()
        if gpa >= 3.5:
            return "Dean's List"
        if gpa >= 2.0:
            return "Good Standing"
        return "Probation"

    def get_responsibilities(self) -> str:
        return "Attend classes, submit assignments, study for exams."


class UndergraduateStudent(Student):
    def __init__(self, person_id: str, name: str, email: str, major: str):
        super().__init__(person_id, name, email, program="Undergraduate")
        self.major = major

    def get_responsibilities(self) -> str:
        return "Complete undergrad coursework, attend labs, projects."


class GraduateStudent(Student):
    def __init__(self, person_id: str, name: str, email: str, research_area: str):
        super().__init__(person_id, name, email, program="Graduate")
        self.research_area = research_area

    def get_responsibilities(self) -> str:
        return "Conduct research, write thesis, assist in teaching."


class SecureStudentRecord:
    def __init__(self, student: Student, max_courses: int = 6):
        self._student = student
        self.__gpa_history = dict(student._gpa_history)
        self.__max_courses = max_courses

    def enroll_course(self, course_code: str):
        if len(self._student.courses) >= self.__max_courses:
            raise ValueError("Enrollment limit reached")
        return self._student.enroll_course(course_code)

    def set_semester_gpa(self, semester: str, gpa: float):
        if not (0.0 <= gpa <= 4.0):
            raise ValueError("GPA must be 0.0–4.0")
        self.__gpa_history[semester] = gpa
        self._student._gpa_history[semester] = gpa

    def get_cumulative_gpa(self) -> float:
        return sum(self.__gpa_history.values()) / len(self.__gpa_history) if self.__gpa_history else 0.0
