from question1_university_system.person import Person

class Faculty(Person):
    def __init__(self, person_id: str, name: str, email: str, department: str):
        super().__init__(person_id, name, email)
        self.department = department
        self.assigned_courses = []

    def assign_course(self, course_code: str):
        if course_code not in self.assigned_courses:
            self.assigned_courses.append(course_code)
            return True
        return False

    def calculate_workload(self) -> float:
        return len(self.assigned_courses) * 3.0

    def get_responsibilities(self) -> str:
        return "Teach courses and advise students."


class Professor(Faculty):
    def calculate_workload(self) -> float:
        return len(self.assigned_courses) * 4.5 + 8.0

    def get_responsibilities(self) -> str:
        return "Lead research, teach advanced courses, supervise grads."


class Lecturer(Faculty):
    def calculate_workload(self) -> float:
        return len(self.assigned_courses) * 3.5

    def get_responsibilities(self) -> str:
        return "Deliver lectures and prepare course materials."


class TA(Faculty):
    def calculate_workload(self) -> float:
        return len(self.assigned_courses) * 2.0

    def get_responsibilities(self) -> str:
        return "Assist labs, grade assignments, hold office hours."
