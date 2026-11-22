from typing import List, Dict, Optional, Tuple
from datetime import datetime, timedelta
from collections import defaultdict

from app.models.schemas import (
    TimetableGenerationRequest,
    TimetableResponse,
    TimeSlotSchedule,
    AlgorithmType,
    AlgorithmMetrics,
)
from app.services.conflict_graph import ConflictGraphBuilder
from app.services.graph_coloring import GraphColoringService
from app.services.room_allocator import RoomAllocatorService

class TimetableGeneratorService:
    @staticmethod
    def generate(request: TimetableGenerationRequest) -> TimetableResponse:
        # 1. Build Conflict Graph
        builder = ConflictGraphBuilder(request.exams, request.students)
        adjacency, shared_map = builder.build_graph()

        # 2. Run selected algorithm (or both)
        coloring: Dict[str, int] = {}
        primary_metrics: AlgorithmMetrics = None
        comparison_dict: Optional[Dict[str, AlgorithmMetrics]] = None

        if request.algorithm == AlgorithmType.GREEDY:
            coloring, primary_metrics = GraphColoringService.greedy_coloring(adjacency)
            algo_name = "Greedy Coloring"
        elif request.algorithm == AlgorithmType.DSATUR:
            coloring, primary_metrics = GraphColoringService.dsatur_coloring(adjacency)
            algo_name = "DSATUR"
        else:  # AlgorithmType.BOTH
            greedy_coloring, greedy_metrics = GraphColoringService.greedy_coloring(adjacency)
            dsatur_coloring, dsatur_metrics = GraphColoringService.dsatur_coloring(adjacency)
            
            # Use DSATUR as primary schedule output when comparing both
            coloring = dsatur_coloring
            primary_metrics = dsatur_metrics
            algo_name = "DSATUR vs Greedy Comparison"
            
            comparison_dict = {
                "greedy": greedy_metrics,
                "dsatur": dsatur_metrics
            }

        # 3. Group examinations by color (time slot)
        slots_to_exams: Dict[int, List] = defaultdict(list)
        for exam in request.exams:
            color = coloring.get(exam.exam_id, 0)
            slots_to_exams[color].append(exam)

        sorted_color_indices = sorted(list(slots_to_exams.keys()))
        total_slots = len(sorted_color_indices)

        # 4. Generate Dates, Times, Room Allocations, and Seating Plans
        start_dt = datetime.strptime(request.start_date, "%Y-%m-%d")
        slots_per_day = max(1, request.slots_per_day)
        session_times = ["09:00 - 12:00 (Morning)", "14:00 - 17:00 (Afternoon)", "18:00 - 21:00 (Evening)"]

        student_dict = {s.student_id: s for s in request.students}
        schedule: List[TimeSlotSchedule] = []
        all_warnings: List[str] = []
        total_unallocated = 0

        for idx, color in enumerate(sorted_color_indices):
            day_offset = idx // slots_per_day
            slot_in_day = idx % slots_per_day
            slot_date_str = (start_dt + timedelta(days=day_offset)).strftime("%Y-%m-%d")
            session_time_str = session_times[slot_in_day % len(session_times)]
            slot_label = f"Slot {idx + 1} (Day {day_offset + 1}, {session_time_str.split(' ')[0]})"

            exams_in_this_slot = slots_to_exams[color]
            
            scheduled_exams, warnings, unallocated = RoomAllocatorService.allocate_rooms_for_slot(
                exams_in_slot=exams_in_this_slot,
                exam_students=builder.exam_students,
                student_dict=student_dict,
                available_rooms=request.rooms,
                slot_label=slot_label,
                slot_date=slot_date_str,
                session_time=session_time_str,
                color_index=color
            )

            all_warnings.extend(warnings)
            total_unallocated += unallocated

            schedule.append(TimeSlotSchedule(
                slot_index=idx + 1,
                slot_label=slot_label,
                date=slot_date_str,
                time=session_time_str,
                exams=scheduled_exams
            ))

        primary_metrics.unallocated_students_count = total_unallocated
        if comparison_dict and "dsatur" in comparison_dict:
            comparison_dict["dsatur"].unallocated_students_count = total_unallocated

        # 5. Build full graph response with colors applied
        conflict_graph_resp = builder.to_response(adjacency, shared_map, coloring)

        return TimetableResponse(
            success=True,
            algorithm_used=algo_name,
            total_slots=total_slots,
            total_exams=len(request.exams),
            total_students=len(request.students),
            conflict_graph=conflict_graph_resp,
            schedule=schedule,
            metrics=primary_metrics,
            comparison=comparison_dict,
            warnings=all_warnings
        )
