# Requirements Traceability Matrix (RTM)

The Requirements Traceability Matrix (RTM) validates bidirectional traceability between Functional Requirements (FRs), Product Backlog User Stories (US), Architecture Components, and Automated Test Cases.

## 1. Traceability Mapping

| Req ID | Requirement Description | User Story | Component / Module | Automated Test Case | Verification Status |
|---|---|---|---|---|---|
| **FR01** | Student, Course, Room, and Exam management with capacity rules | US01 | `models/schemas.py`, `api/sample_data.py` | `test_sample_data_endpoint` | **VERIFIED (PASSED)** |
| **FR02** | Automatic conflict detection using shared-student information | US02, US03 | `services/conflict_graph.py` | `test_conflict_graph_shared_students` | **VERIFIED (PASSED)** |
| **FR03** | Graph representation $G = (V, E)$ with adjacency list | US02 | `services/conflict_graph.py` | `test_conflict_graph_shared_students` | **VERIFIED (PASSED)** |
| **FR04** | Timetable generation using graph-coloring logic | US04 | `services/timetable_generator.py` | `test_generate_timetable_endpoint` | **VERIFIED (PASSED)** |
| **FR05** | Support Greedy Coloring and DSATUR for comparison | US04, US05 | `services/graph_coloring.py` | `test_greedy_coloring_validity`, `test_dsatur_coloring_bipartite_and_tie_breaker`, `test_compare_algorithms_endpoint` | **VERIFIED (PASSED)** |
| **FR06** | Assign rooms according to room capacity | US06 | `services/room_allocator.py` | `test_room_allocation_respects_capacity` | **VERIFIED (PASSED)** |
| **FR07** | Generate structured seating plan for examination sessions | US08 | `services/room_allocator.py` | `test_room_allocation_respects_capacity` | **VERIFIED (PASSED)** |
| **FR08** | Capacity shortage detection and warning reporting | US07 | `services/room_allocator.py` | `test_room_allocation_insufficient_capacity_warning` | **VERIFIED (PASSED)** |
| **FR09** | Regenerate timetable and seating plan dynamically | US11 | `services/timetable_generator.py` | `test_timetable_generator_both_comparison` | **VERIFIED (PASSED)** |
| **FR10** | Conflict graph visualization (nodes, edges, slot colors) | US09 | `frontend/index.html` (Cytoscape.js) | UI inspection & response contract validation | **VERIFIED (PASSED)** |
| **FR11** | Exportable seating plan and timetable (Print/PDF) | US10 | `frontend/index.html` (Print CSS) | Print media query evaluation | **VERIFIED (PASSED)** |

## 2. Test Execution Summary
- **Test Framework:** `pytest 8.4.2`
- **Total Test Cases Executed:** 10
- **Pass Rate:** **100% (10 passed, 0 failed)**
- **Average Execution Time:** ~5.04 seconds
