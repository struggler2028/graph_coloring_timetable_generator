# Sprint 3 – Sprint Backlog

## Sprint Goal
To implement room allocation and student seating plan generation and integrate them with the examination timetable.

## User Stories and Tasks

### S3-01: Room Allocation
**Priority:** High  
**Story Points:** 5

Tasks:
- Retrieve examination details and student counts.
- Retrieve available rooms and their capacities.
- Allocate suitable rooms to examinations.
- Ensure that room capacity is not exceeded.
- Handle cases where available room capacity is insufficient.

Acceptance Criteria:
- Rooms are assigned according to available capacity.
- No room is assigned beyond its capacity.
- Insufficient room availability is reported clearly.

### S3-02: Seating Plan Generation
**Priority:** High  
**Story Points:** 5

Tasks:
- Retrieve students registered for each examination.
- Generate seating arrangements.
- Assign students to available seats.
- Store student and seat details.
- Display the seating plan.

Acceptance Criteria:
- Every registered student receives a seat.
- No student is assigned more than once for the same examination.
- Seat allocation stays within room capacity.

### S3-03: Backend Integration
**Priority:** Medium  
**Story Points:** 3

Tasks:
- Connect room allocation with timetable data.
- Connect seating plan generation with room allocation.
- Store generated allocation details.
- Validate data exchanged between modules.

Acceptance Criteria:
- Room allocation uses the generated timetable.
- Seating plans use the correct examination and room details.
- Integrated modules produce consistent results.

## Total Story Points
13 Story Points

## Sprint Progress
To be updated during sprint execution.
