# Daily Standup Logs & Scrum Notes

## Purpose
Daily standups are conducted as 15-minute time-boxed synchronous check-ins to synchronize activities, inspect daily progress toward the Sprint Goal, and flag technical impediments.

---

### Sprint 1 Standup Summary
- **Focus:** Problem statement formalization, conflict graph representation, and database schemas.
- **Key Updates:**
  - Designed initial Pydantic data models for Students, Courses, Exams, and Rooms.
  - Defined mathematical formulation $G = (V, E)$ where vertices represent examination sessions and edges represent shared student enrollment.
- **Impediments Resolved:** Clarified handling of elective courses where cross-department students enroll simultaneously.

---

### Sprint 2 Standup Summary
- **Focus:** Graph construction algorithm, adjacency matrix vs adjacency list, and graph coloring algorithms.
- **Key Updates:**
  - Implemented conflict detection logic comparing student course enrollment sets.
  - Implemented baseline Greedy Coloring with sequential vertex evaluation.
  - Implemented DSATUR algorithm with saturation degree tracking and vertex degree tie-breaker.
- **Impediments Resolved:** Addressed edge-case where two exams have identical saturation degrees and vertex degrees by enforcing deterministic secondary tie-breaking.

---

### Sprint 3 Standup Summary
- **Focus:** Room allocation, capacity constraints, and structured student seating plans.
- **Key Updates:**
  - Developed room allocation engine sorting rooms by capacity descending.
  - Built room capacity validation to detect and alert on student overflow.
  - Generated coordinate-based seating charts (Row, Col, Seat ID).
- **Impediments Resolved:** Resolved multi-exam room sharing collision detection so that students from different exams in the same time slot do not overwrite assigned seat coordinates.

---

### Sprint 4 Standup Summary
- **Focus:** Cytoscape.js interactive graph integration, REST API client, end-to-end testing, and PDF generation.
- **Key Updates:**
  - Mounted Cytoscape.js canvas with interactive physics-based layout (cose) and time-slot color coding.
  - Added algorithm comparison cards comparing time slots used and execution time.
  - Developed printable PDF report generator for academic administration.
  - Validated 100% test pass rate across unit and API integration test suites.
- **Impediments Resolved:** Optimized graph rendering performance for networks with high edge densities.
