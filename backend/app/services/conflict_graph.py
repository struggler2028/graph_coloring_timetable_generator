from typing import List, Dict, Set, Tuple
from collections import defaultdict
from app.models.schemas import Student, Course, Exam, GraphNode, GraphEdge, ConflictGraphResponse

# High-contrast, accessible color palette for visual graph slots
COLOR_PALETTE = [
    "#3B82F6",  # Blue
    "#10B981",  # Emerald
    "#F59E0B",  # Amber
    "#EF4444",  # Red
    "#8B5CF6",  # Purple
    "#EC4899",  # Pink
    "#06B6D4",  # Cyan
    "#F97316",  # Orange
    "#84CC16",  # Lime
    "#6366F1",  # Indigo
    "#14B8A6",  # Teal
    "#D946EF",  # Fuchsia
]

def get_color_hex(color_index: int) -> str:
    if color_index is None or color_index < 0:
        return "#94A3B8"  # Slate / uncolored
    return COLOR_PALETTE[color_index % len(COLOR_PALETTE)]

class ConflictGraphBuilder:
    def __init__(self, exams: List[Exam], students: List[Student]):
        self.exams = exams
        self.students = students
        self.exam_by_id = {exam.exam_id: exam for exam in exams}
        self.exam_by_course = {exam.course_code: exam for exam in exams}
        
        # Mapping: exam_id -> set of enrolled student_ids
        self.exam_students: Dict[str, Set[str]] = defaultdict(set)
        # Mapping: student_id -> set of enrolled exam_ids
        self.student_exams: Dict[str, Set[str]] = defaultdict(set)
        
        self._build_enrollments()

    def _build_enrollments(self):
        for student in self.students:
            for course_code in student.enrolled_courses:
                if course_code in self.exam_by_course:
                    exam = self.exam_by_course[course_code]
                    self.exam_students[exam.exam_id].add(student.student_id)
                    self.student_exams[student.student_id].add(exam.exam_id)

    def build_graph(self) -> Tuple[Dict[str, Set[str]], Dict[Tuple[str, str], List[str]]]:
        """
        Builds adjacency list and edge conflict details:
        - Vertices: examinations
        - Edge (E1, E2): exists if at least one student is enrolled in both
        """
        adjacency: Dict[str, Set[str]] = {exam.exam_id: set() for exam in self.exams}
        shared_map: Dict[Tuple[str, str], List[str]] = {}

        exam_ids = [exam.exam_id for exam in self.exams]
        n = len(exam_ids)

        for i in range(n):
            e1 = exam_ids[i]
            students_e1 = self.exam_students[e1]
            for j in range(i + 1, n):
                e2 = exam_ids[j]
                students_e2 = self.exam_students[e2]
                common_students = list(students_e1.intersection(students_e2))
                if common_students:
                    adjacency[e1].add(e2)
                    adjacency[e2].add(e1)
                    shared_map[(min(e1, e2), max(e1, e2))] = common_students

        return adjacency, shared_map

    def to_response(
        self,
        adjacency: Dict[str, Set[str]],
        shared_map: Dict[Tuple[str, str], List[str]],
        coloring: Dict[str, int] = None
    ) -> ConflictGraphResponse:
        nodes: List[GraphNode] = []
        edges: List[GraphEdge] = []
        coloring = coloring or {}

        for exam in self.exams:
            deg = len(adjacency.get(exam.exam_id, set()))
            color_idx = coloring.get(exam.exam_id)
            
            # Saturation: number of distinct neighbor colors
            neighbor_colors = {
                coloring[nbr] for nbr in adjacency.get(exam.exam_id, set())
                if nbr in coloring and coloring[nbr] is not None
            }

            nodes.append(GraphNode(
                id=exam.exam_id,
                label=f"{exam.course_code}: {exam.exam_name}",
                course_code=exam.course_code,
                degree=deg,
                saturation=len(neighbor_colors),
                color=color_idx,
                color_hex=get_color_hex(color_idx) if color_idx is not None else None,
                student_count=len(self.exam_students.get(exam.exam_id, set()))
            ))

        for (u, v), shared in shared_map.items():
            edges.append(GraphEdge(
                source=u,
                target=v,
                weight=len(shared),
                shared_students=shared
            ))

        total_nodes = len(nodes)
        total_edges = len(edges)
        possible_edges = (total_nodes * (total_nodes - 1)) / 2 if total_nodes > 1 else 1
        density = round(total_edges / possible_edges, 4) if total_nodes > 1 else 0.0

        return ConflictGraphResponse(
            nodes=nodes,
            edges=edges,
            total_nodes=total_nodes,
            total_edges=total_edges,
            density=density
        )
