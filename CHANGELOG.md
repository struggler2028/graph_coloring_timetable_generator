# Changelog

All notable changes to the **Dynamic Graph Coloring Based Exam Timetabling and Seating Plan Generator** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-11-22

### Added
- **Core Algorithms:**
  - Automated examination conflict graph construction $G = (V, E)$ based on shared student course enrollments.
  - Greedy Graph Coloring algorithm for baseline scheduling.
  - DSATUR (Degree of Saturation) Graph Coloring algorithm with highest-degree tie breaker.
  - Room Allocation engine with capacity validation and descending fit.
  - Coordinate-based student seating plan matrix generator (`Row`, `Col`, `SeatNumber`).
  - Capacity shortage detection emitting real-time warning logs.
- **Backend API & Engine:**
  - FastAPI web service with routes: `/api/timetable/generate`, `/api/timetable/compare`, `/api/sample-data`, `/api/health`.
  - Pydantic models for validation of Students, Courses, Exams, and Rooms.
  - Embedded sample academic dataset (25 students, 10 exams, 4 halls).
- **Frontend & Visualization:**
  - Interactive Cytoscape.js examination conflict network visualizer with physics-based layout.
  - Time-slot color mapping with node inspection side panel.
  - Algorithm comparison dashboard (Greedy vs DSATUR slots, runtime, distribution).
  - Examination schedule timetable grid by date and session (Morning/Afternoon).
  - Room-wise student seating arrangement layout.
  - Print-friendly PDF export stylesheet.
- **Testing & Quality Assurance:**
  - Comprehensive unit test suite (`test_graph_service.py`) covering coloring correctness and capacity constraints.
  - REST API integration test suite (`test_api_endpoints.py`) using `TestClient`.
  - Automated GitHub Actions CI workflow (`.github/workflows/ci.yml`).
- **Agile Documentation:**
  - Complete documentation suite across `docs/agile/` (Sprint reports 1–4, Standups, DoD, DoR, Backlog, Retrospectives, Reviews, XP, Kanban, User Stories, RTM).
