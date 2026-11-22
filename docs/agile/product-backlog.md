# Product Backlog

## 1. Prioritized Epics & User Stories

| Story ID | Epic | User Story | Priority | Story Points | Sprint | Status |
|---|---|---|---|---|---|---|
| **US01** | Data Input | As an administrator, I want to input students, courses, exams, and rooms with capacities so that scheduling data is available. | High | 5 | Sprint 1 | Done |
| **US02** | Graph Construction | As an administrator, I want the system to construct an examination conflict graph where edges represent shared students. | High | 8 | Sprint 2 | Done |
| **US03** | Conflict Detection | As an administrator, I want to inspect all pairs of conflicting examinations and see the exact students causing the clash. | High | 5 | Sprint 2 | Done |
| **US04** | Graph Coloring Engine | As an administrator, I want to execute Greedy Coloring and DSATUR to schedule exams into minimal clash-free time slots. | High | 13 | Sprint 2 | Done |
| **US05** | Algorithm Benchmark | As an administrator, I want to compare Greedy and DSATUR side-by-side on time slots used, runtime, and distribution. | Medium | 5 | Sprint 2 | Done |
| **US06** | Room Allocation | As an administrator, I want students to be assigned to available examination rooms strictly respecting room capacity. | High | 8 | Sprint 3 | Done |
| **US07** | Capacity Shortage Detection | As an administrator, I want immediate warnings if total room capacity in a time slot is insufficient for enrolled candidates. | High | 3 | Sprint 3 | Done |
| **US08** | Seating Plan Matrix | As an administrator, I want structured seating arrangements with Row and Column seat coordinates for each room. | High | 8 | Sprint 3 | Done |
| **US09** | Interactive Visualization | As an administrator, I want an interactive Cytoscape.js network visualizer to view color-coded exam nodes and conflict edges. | High | 8 | Sprint 4 | Done |
| **US10** | Printable / PDF Export | As an administrator, I want to export or print formatted timetables and room seating plans for campus distribution. | Medium | 5 | Sprint 4 | Done |
| **US11** | Schedule Regeneration | As an administrator, I want to regenerate the timetable and seating plan dynamically whenever input data changes. | Medium | 5 | Sprint 4 | Done |

## 2. Estimation Summary
- Total Product Backlog Story Points: **73 points**
- Velocity per Sprint: ~18 - 20 points
- Completed across 4 planned sprints.
