from typing import List, Dict, Set, Tuple
from app.models.schemas import (
    Room,
    Exam,
    Student,
    StudentSeat,
    ExamRoomAllocation,
    ScheduledExam,
)

class RoomAllocatorService:
    @staticmethod
    def allocate_rooms_for_slot(
        exams_in_slot: List[Exam],
        exam_students: Dict[str, Set[str]],
        student_dict: Dict[str, Student],
        available_rooms: List[Room],
        slot_label: str,
        slot_date: str,
        session_time: str,
        color_index: int,
    ) -> Tuple[List[ScheduledExam], List[str], int]:
        """
        Allocates rooms for all exams scheduled concurrently in a given time slot.
        Ensures room capacity is respected and students are systematically seated.
        Returns:
            - List of ScheduledExam with room allocations and seating plans
            - List of warnings (e.g. capacity shortage)
            - Number of unallocated students
        """
        warnings: List[str] = []
        unallocated_total = 0
        scheduled_exams: List[ScheduledExam] = []

        # Sort rooms by capacity descending for best-fit allocation
        sorted_rooms = sorted(available_rooms, key=lambda r: r.capacity, reverse=True)
        # Track remaining capacity of each room during this time slot
        room_remaining_capacity = {r.room_id: r.capacity for r in sorted_rooms}
        room_allocations_map: Dict[str, List[StudentSeat]] = {r.room_id: [] for r in sorted_rooms}
        room_by_id = {r.room_id: r for r in sorted_rooms}

        for exam in exams_in_slot:
            student_ids = sorted(list(exam_students.get(exam.exam_id, set())))
            total_students = len(student_ids)
            exam_room_allocs: List[ExamRoomAllocation] = []

            curr_student_idx = 0

            # Find rooms with remaining capacity
            for room in sorted_rooms:
                if curr_student_idx >= total_students:
                    break
                
                avail_space = room_remaining_capacity[room.room_id]
                if avail_space <= 0:
                    continue

                needed = total_students - curr_student_idx
                assign_count = min(avail_space, needed)

                allocated_seats: List[StudentSeat] = []
                base_seat_index = len(room_allocations_map[room.room_id])

                # Grid geometry for room seating: 5 columns per row
                cols = 5
                for k in range(assign_count):
                    s_id = student_ids[curr_student_idx]
                    student_obj = student_dict.get(s_id)
                    s_name = student_obj.name if student_obj else s_id
                    seat_pos = base_seat_index + k
                    
                    row = (seat_pos // cols) + 1
                    col = (seat_pos % cols) + 1
                    seat_num = f"R{row:02d}-S{col:02d}"

                    seat = StudentSeat(
                        student_id=s_id,
                        student_name=s_name,
                        exam_id=exam.exam_id,
                        course_code=exam.course_code,
                        seat_number=seat_num,
                        row=row,
                        col=col
                    )
                    allocated_seats.append(seat)
                    room_allocations_map[room.room_id].append(seat)
                    curr_student_idx += 1

                room_remaining_capacity[room.room_id] -= assign_count

                exam_room_allocs.append(ExamRoomAllocation(
                    room_id=room.room_id,
                    room_number=room.room_number,
                    building=room.building,
                    capacity=room.capacity,
                    allocated_count=assign_count,
                    seats=allocated_seats
                ))

            # Check if any students could not be accommodated
            if curr_student_idx < total_students:
                unallocated = total_students - curr_student_idx
                unallocated_total += unallocated
                msg = (
                    f"Insufficient room capacity in {slot_label} for exam '{exam.course_code} - {exam.exam_name}'. "
                    f"{unallocated} out of {total_students} students could not be seated."
                )
                warnings.append(msg)

            scheduled_exams.append(ScheduledExam(
                exam_id=exam.exam_id,
                course_code=exam.course_code,
                exam_name=exam.exam_name,
                color_index=color_index,
                slot_label=slot_label,
                date=slot_date,
                session_time=session_time,
                total_students=total_students,
                room_allocations=exam_room_allocs
            ))

        return scheduled_exams, warnings, unallocated_total
