from question1_university_system.student import UndergraduateStudent, GraduateStudent, SecureStudentRecord
from question1_university_system.faculty import Professor, Lecturer, TA
from question1_university_system.department import Department, Course

def demo():
    cs = Department("Computer Science")

    prof = Professor("F001", "Dr. Thiru", "thiru@uni.edu", "CS")
    lect = Lecturer("F002", "Vinuja", "vinu@uni.edu", "CS")
    ta = TA("F003", "Dayan", "dayan@uni.edu", "CS")
    cs.add_faculty(prof)
    cs.add_faculty(lect)
    cs.add_faculty(ta)

    intro = Course("CS101", "Intro to CS", 3, max_students=2)
    adv = Course("CS201", "Algorithms", 4, prerequisites=["CS101"])
    cs.create_course(intro)
    cs.create_course(adv)
    cs.assign_faculty_to_course("F001", "CS201")
    cs.assign_faculty_to_course("F002", "CS101")

    s1 = UndergraduateStudent("S001", "Maheshi", "mwasala@uni.edu", "CS")
    s2 = UndergraduateStudent("S002", "Nilukshi", "nilu@uni.edu", "CS")

    print("Registering students to CS101...")
    cs.register_student("CS101", s1)
    cs.register_student("CS101", s2)

    s1.record_grade("CS101", 3.7)
    s2.record_grade("CS101", 1.8)

    try:
        cs.register_student("CS201", s1)
        print("s1 enrolled in CS201")
    except Exception as e:
        print("Error enrolling s1 in CS201:", e)

    try:
        cs.register_student("CS201", s2)
    except Exception as e:
        print("Expected prereq error for s2:", e)

    secure_s1 = SecureStudentRecord(s1)
    secure_s1.set_semester_gpa("2025S1", 3.6)
    print("Cumulative GPA (secure):", secure_s1.get_cumulative_gpa())

    people = [s1, prof, lect, ta]
    for p in people:
        print(f"{p.name} responsibilities: {p.get_responsibilities()}")
        if hasattr(p, "calculate_workload"):
            print(f"Workload estimate: {p.calculate_workload()} hours/week")

if __name__ == "__main__":
    demo()
