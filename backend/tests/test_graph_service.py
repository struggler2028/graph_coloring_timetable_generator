import pytest
from app.models.schemas import Student, Course, Exam, Room, AlgorithmType, TimetableGenerationRequest
from app.services.conflict_graph import ConflictGraphBuilder
from app.services.graph_coloring import GraphColoringService, validate_coloring
from app.services.room_allocator import RoomAllocatorService
from app.services.timetable_generator import TimetableGeneratorService

def test_conflict_graph_shared_students():
    exams = [
        Exam(exam_id="E1", course_code="CS101", exam_name="Data Structures"),
        Exam(exam_id="E2", course_code="CS102", exam_name="Databases"),
        Exam(exam_id="E3", course_code="ME101", exam_name="Mechanics"),
    ]
    # S1 takes CS101 and CS102 -> creates edge (E1, E2)
    # S2 takes ME101 only -> no shared students with E1 or E2
    students = [
        Student(student_id="S1", name="Alice", enrolled_courses=["CS101", "CS102"]),
        Student(student_id="S2", name="Bob", enrolled_courses=["ME101"]),
    ]

    builder = ConflictGraphBuilder(exams, students)
    adj, shared = builder.build_graph()

    assert "E2" in adj["E1"]
    assert "E1" in adj["E2"]
    assert "E3" not in adj["E1"]
    assert "E3" not in adj["E2"]
    assert len(shared) == 1
    assert shared[("E1", "E2")] == ["S1"]

def test_greedy_coloring_validity():
    # Triangle graph (K3) requires exactly 3 colors
    adjacency = {
        "E1": {"E2", "E3"},
        "E2": {"E1", "E3"},
        "E3": {"E1", "E2"},
    }
    coloring, metrics = GraphColoringService.greedy_coloring(adjacency)

    assert metrics.is_valid_coloring is True
    assert metrics.slots_used == 3
    assert coloring["E1"] != coloring["E2"]
    assert coloring["E2"] != coloring["E3"]
    assert coloring["E1"] != coloring["E3"]

def test_dsatur_coloring_bipartite_and_tie_breaker():
    # Bipartite graph K2,2 should be colored with 2 colors
    adjacency = {
        "A1": {"B1", "B2"},
        "A2": {"B1", "B2"},
        "B1": {"A1", "A2"},
        "B2": {"A1", "A2"},
    }
    coloring, metrics = GraphColoringService.dsatur_coloring(adjacency)

    assert metrics.is_valid_coloring is True
    assert metrics.slots_used == 2
    assert coloring["A1"] == coloring["A2"]
    assert coloring["B1"] == coloring["B2"]
    assert coloring["A1"] != coloring["B1"]

def test_room_allocation_respects_capacity():
    exam = Exam(exam_id="E1", course_code="CS101", exam_name="DSA")
    exam_students = {"E1": {f"S{i}" for i in range(1, 26)}}  # 25 students
    student_dict = {f"S{i}": Student(student_id=f"S{i}", name=f"Student {i}", enrolled_courses=["CS101"]) for i in range(1, 26)}
    
    # Room 1: capacity 15, Room 2: capacity 15 -> total 30 >= 25
    rooms = [
        Room(room_id="R1", room_number="Room 101", capacity=15),
        Room(room_id="R2", room_number="Room 102", capacity=15),
    ]

    scheduled_exams, warnings, unallocated = RoomAllocatorService.allocate_rooms_for_slot(
        exams_in_slot=[exam],
        exam_students=exam_students,
        student_dict=student_dict,
        available_rooms=rooms,
        slot_label="Slot 1",
        slot_date="2026-12-01",
        session_time="09:00 - 12:00",
        color_index=0
    )

    assert len(scheduled_exams) == 1
    allocations = scheduled_exams[0].room_allocations
    assert len(allocations) == 2
    assert allocations[0].allocated_count == 15
    assert allocations[1].allocated_count == 10
    assert unallocated == 0
    assert len(warnings) == 0

def test_room_allocation_insufficient_capacity_warning():
    exam = Exam(exam_id="E1", course_code="CS101", exam_name="DSA")
    exam_students = {"E1": {f"S{i}" for i in range(1, 26)}}  # 25 students
    student_dict = {f"S{i}": Student(student_id=f"S{i}", name=f"Student {i}", enrolled_courses=["CS101"]) for i in range(1, 26)}
    
    # Only room with capacity 10 -> 15 students unallocated
    rooms = [
        Room(room_id="R1", room_number="Room 101", capacity=10),
    ]

    scheduled_exams, warnings, unallocated = RoomAllocatorService.allocate_rooms_for_slot(
        exams_in_slot=[exam],
        exam_students=exam_students,
        student_dict=student_dict,
        available_rooms=rooms,
        slot_label="Slot 1",
        slot_date="2026-12-01",
        session_time="09:00 - 12:00",
        color_index=0
    )

    assert unallocated == 15
    assert len(warnings) == 1
    assert "Insufficient room capacity" in warnings[0]

def test_timetable_generator_both_comparison():
    courses = [
        Course(course_code="C1", course_name="Course 1"),
        Course(course_code="C2", course_name="Course 2"),
        Course(course_code="C3", course_name="Course 3"),
    ]
    exams = [
        Exam(exam_id="E1", course_code="C1", exam_name="Exam 1"),
        Exam(exam_id="E2", course_code="C2", exam_name="Exam 2"),
        Exam(exam_id="E3", course_code="C3", exam_name="Exam 3"),
    ]
    rooms = [Room(room_id="R1", room_number="Hall 1", capacity=50)]
    students = [
        Student(student_id="S1", name="Alice", enrolled_courses=["C1", "C2"]),
        Student(student_id="S2", name="Bob", enrolled_courses=["C2", "C3"]),
    ]

    req = TimetableGenerationRequest(
        students=students,
        courses=courses,
        exams=exams,
        rooms=rooms,
        algorithm=AlgorithmType.BOTH
    )

    resp = TimetableGeneratorService.generate(req)
    assert resp.success is True
    assert resp.comparison is not None
    assert "greedy" in resp.comparison
    assert "dsatur" in resp.comparison
    assert resp.metrics.is_valid_coloring is True
