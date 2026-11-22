# Sprint 3 – Room Allocation & Seating Plan Matrix

## 1. Sprint Goal
Develop the room capacity validation and allocation engine, build the coordinate-based student seating plan generator, and integrate backend REST APIs.

## 2. Sprint Information
- **Duration:** Week 3
- **Status:** Completed
- **Story Points Committed:** 19
- **Story Points Delivered:** 19

## 3. Backlog Items Delivered
- [x] **US06:** Room allocation algorithm assigning rooms to exams scheduled concurrently in each slot.
- [x] **US07:** Capacity constraint validation detecting and warning on room capacity shortages.
- [x] **US08:** Seating plan matrix generator assigning systematic Row, Column, and Seat IDs (`R01-S01`).
- [x] Multi-room exam split logic enabling exams with large candidate counts to be distributed across multiple halls without student overlap.
- [x] REST API endpoints (`/api/timetable/generate`, `/api/timetable/compare`, `/api/sample-data`, `/api/health`).

## 4. Key Decisions & Outcomes
- Rooms are sorted by capacity descending to place large exams into auditoriums and main halls efficiently.
- Seating positions are formatted into standard 5-column grid coordinates per room.
- Integration tests (`test_api_endpoints.py`) implemented with FastAPI `TestClient`.
