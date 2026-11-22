from typing import List, Optional, Dict, Any
from enum import Enum
from pydantic import BaseModel, Field

class AlgorithmType(str, Enum):
    GREEDY = "greedy"
    DSATUR = "dsatur"
    BOTH = "both"

class Student(BaseModel):
    student_id: str
    name: str
    enrolled_courses: List[str] = Field(default_factory=list)

class Course(BaseModel):
    course_code: str
    course_name: str

class Exam(BaseModel):
    exam_id: str
    course_code: str
    exam_name: str
    duration_minutes: int = 120

class Room(BaseModel):
    room_id: str
    room_number: str
    capacity: int
    building: Optional[str] = "Main Hall"

class GraphNode(BaseModel):
    id: str
    label: str
    course_code: str
    degree: int = 0
    saturation: int = 0
    color: Optional[int] = None
    color_hex: Optional[str] = None
    student_count: int = 0

class GraphEdge(BaseModel):
    source: str
    target: str
    weight: int = 1
    shared_students: List[str] = Field(default_factory=list)

class ConflictGraphResponse(BaseModel):
    nodes: List[GraphNode]
    edges: List[GraphEdge]
    total_nodes: int
    total_edges: int
    density: float

class StudentSeat(BaseModel):
    student_id: str
    student_name: str
    exam_id: str
    course_code: str
    seat_number: str
    row: int
    col: int

class ExamRoomAllocation(BaseModel):
    room_id: str
    room_number: str
    building: Optional[str] = None
    capacity: int
    allocated_count: int
    seats: List[StudentSeat] = Field(default_factory=list)

class ScheduledExam(BaseModel):
    exam_id: str
    course_code: str
    exam_name: str
    color_index: int
    slot_label: str
    date: str
    session_time: str
    total_students: int
    room_allocations: List[ExamRoomAllocation] = Field(default_factory=list)

class TimeSlotSchedule(BaseModel):
    slot_index: int
    slot_label: str
    date: str
    time: str
    exams: List[ScheduledExam]

class AlgorithmMetrics(BaseModel):
    algorithm_name: str
    slots_used: int
    execution_time_ms: float
    color_distribution: Dict[int, int]
    is_valid_coloring: bool
    unallocated_students_count: int = 0

class TimetableGenerationRequest(BaseModel):
    students: List[Student]
    courses: List[Course]
    exams: List[Exam]
    rooms: List[Room]
    algorithm: AlgorithmType = AlgorithmType.DSATUR
    start_date: str = "2026-12-01"
    slots_per_day: int = 2

class TimetableResponse(BaseModel):
    success: bool
    algorithm_used: str
    total_slots: int
    total_exams: int
    total_students: int
    conflict_graph: ConflictGraphResponse
    schedule: List[TimeSlotSchedule]
    metrics: AlgorithmMetrics
    comparison: Optional[Dict[str, AlgorithmMetrics]] = None
    warnings: List[str] = Field(default_factory=list)
