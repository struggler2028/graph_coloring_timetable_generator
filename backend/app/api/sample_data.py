from typing import List
from app.models.schemas import Student, Course, Exam, Room

def get_default_sample_data():
    courses = [
        Course(course_code="CS101", course_name="Data Structures & Algorithms"),
        Course(course_code="CS102", course_name="Database Management Systems"),
        Course(course_code="CS103", course_name="Computer Networks"),
        Course(course_code="CS104", course_name="Operating Systems"),
        Course(course_code="MA201", course_name="Discrete Mathematics"),
        Course(course_code="MA202", course_name="Linear Algebra & Probability"),
        Course(course_code="PH101", course_name="Engineering Physics"),
        Course(course_code="CH101", course_name="Engineering Chemistry"),
        Course(course_code="EE101", course_name="Basic Electrical Engineering"),
        Course(course_code="ME101", course_name="Engineering Mechanics"),
    ]

    exams = [
        Exam(exam_id="EXAM_CS101", course_code="CS101", exam_name="Data Structures Final", duration_minutes=180),
        Exam(exam_id="EXAM_CS102", course_code="CS102", exam_name="DBMS Final", duration_minutes=180),
        Exam(exam_id="EXAM_CS103", course_code="CS103", exam_name="Computer Networks Final", duration_minutes=180),
        Exam(exam_id="EXAM_CS104", course_code="CS104", exam_name="Operating Systems Final", duration_minutes=180),
        Exam(exam_id="EXAM_MA201", course_code="MA201", exam_name="Discrete Math Exam", duration_minutes=180),
        Exam(exam_id="EXAM_MA202", course_code="MA202", exam_name="Linear Algebra Exam", duration_minutes=180),
        Exam(exam_id="EXAM_PH101", course_code="PH101", exam_name="Physics Theory Exam", duration_minutes=180),
        Exam(exam_id="EXAM_CH101", course_code="CH101", exam_name="Chemistry Theory Exam", duration_minutes=180),
        Exam(exam_id="EXAM_EE101", course_code="EE101", exam_name="Electrical Eng Final", duration_minutes=180),
        Exam(exam_id="EXAM_ME101", course_code="ME101", exam_name="Engineering Mechanics", duration_minutes=180),
    ]

    rooms = [
        Room(room_id="ROOM_101", room_number="Auditorium-A", capacity=25, building="Main Block"),
        Room(room_id="ROOM_102", room_number="Hall-B", capacity=20, building="Science Block"),
        Room(room_id="ROOM_103", room_number="Lecture-Hall-1", capacity=15, building="Academic Block"),
        Room(room_id="ROOM_104", room_number="Seminar-Hall", capacity=15, building="Main Block"),
    ]

    # 30 Realistic Students enrolled in intersecting academic programs
    students: List[Student] = [
        # CS Batch 1 (Takes CS101, CS102, MA201)
        Student(student_id="STU01", name="Aarav Sharma", enrolled_courses=["CS101", "CS102", "MA201"]),
        Student(student_id="STU02", name="Ananya Patel", enrolled_courses=["CS101", "CS102", "MA201"]),
        Student(student_id="STU03", name="Rohan Iyer", enrolled_courses=["CS101", "CS102", "MA202"]),
        Student(student_id="STU04", name="Priya Nair", enrolled_courses=["CS101", "CS104", "MA201"]),
        Student(student_id="STU05", name="Vikram Sen", enrolled_courses=["CS101", "CS103", "MA201"]),
        
        # CS & IT Batch 2 (Takes CS102, CS103, CS104)
        Student(student_id="STU06", name="Siddharth Rao", enrolled_courses=["CS102", "CS103", "CS104"]),
        Student(student_id="STU07", name="Kavya Joshi", enrolled_courses=["CS102", "CS103", "MA202"]),
        Student(student_id="STU08", name="Rahul Verma", enrolled_courses=["CS103", "CS104", "EE101"]),
        Student(student_id="STU09", name="Divya Menon", enrolled_courses=["CS103", "CS104", "MA201"]),
        Student(student_id="STU10", name="Arjun Kapoor", enrolled_courses=["CS104", "EE101", "MA202"]),

        # Math / Science Cross-Enrolled (Takes MA201, MA202, PH101)
        Student(student_id="STU11", name="Meera Kulkarni", enrolled_courses=["MA201", "MA202", "PH101"]),
        Student(student_id="STU12", name="Karan Malhotra", enrolled_courses=["MA201", "PH101", "CH101"]),
        Student(student_id="STU13", name="Sneha Reddy", enrolled_courses=["MA202", "PH101", "EE101"]),
        Student(student_id="STU14", name="Aditya Das", enrolled_courses=["MA202", "CH101", "ME101"]),
        Student(student_id="STU15", name="Pooja Hegde", enrolled_courses=["CS101", "MA202", "PH101"]),

        # Engineering Common Batch (PH101, CH101, EE101, ME101)
        Student(student_id="STU16", name="Manish Pandey", enrolled_courses=["PH101", "CH101", "ME101"]),
        Student(student_id="STU17", name="Tanvi Deshmukh", enrolled_courses=["PH101", "EE101", "ME101"]),
        Student(student_id="STU18", name="Nikhil Bansal", enrolled_courses=["CH101", "EE101", "ME101"]),
        Student(student_id="STU19", name="Ritu Chawla", enrolled_courses=["CH101", "ME101", "CS101"]),
        Student(student_id="STU20", name="Gaurav Bhatia", enrolled_courses=["EE101", "ME101", "CS102"]),

        # Specialized / Minor students
        Student(student_id="STU21", name="Ishaan Roy", enrolled_courses=["CS101", "EE101"]),
        Student(student_id="STU22", name="Shruti Mishra", enrolled_courses=["CS102", "PH101"]),
        Student(student_id="STU23", name="Abhinav Saxena", enrolled_courses=["CS103", "CH101"]),
        Student(student_id="STU24", name="Neha Gupta", enrolled_courses=["CS104", "ME101"]),
        Student(student_id="STU25", name="Varun Dhawan", enrolled_courses=["MA201", "ME101"]),
    ]

    return {
        "courses": courses,
        "exams": exams,
        "rooms": rooms,
        "students": students
    }
