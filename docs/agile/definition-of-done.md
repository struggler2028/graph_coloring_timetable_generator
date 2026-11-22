# Definition of Done (DoD)

A user story, feature, or task is classified as **Done** only when all of the following engineering and academic criteria are strictly satisfied:

## 1. Algorithmic Correctness
- [x] **Zero Conflict Guarantee:** No two examinations sharing one or more enrolled students are assigned the same time slot color:
  $$\forall (u, v) \in E \implies \text{color}(u) \neq \text{color}(v)$$
- [x] **Capacity Invariant:** Total students allocated to any given room in a session never exceed the specified room capacity:
  $$\sum \text{allocated}(R_i) \le \text{capacity}(R_i)$$
- [x] **Complete Seat Coverage:** Every student enrolled in an exam scheduled in the time slot is assigned an unambiguous seat coordinate (`Row`, `Col`, `SeatNumber`) or an explicit shortage warning is emitted.

## 2. Engineering & Code Quality
- [x] Python backend code conforms to PEP 8 standards with strict type hinting.
- [x] Code is modularized into discrete responsibilities: `models`, `services`, `api`, `tests`.
- [x] All unit and integration tests written in `pytest` execute successfully with a 100% pass rate.
- [x] No deprecated API calls or unhandled exceptions under empty or boundary inputs.

## 3. Documentation & Traceability
- [x] Architecture, algorithm designs, and API contracts are fully documented in `/docs`.
- [x] Every functional requirement is mapped in the Requirements Traceability Matrix (`RTM`).
- [x] Sprints, backlog items, reviews, and retrospectives are logged.

## 4. Usability & Export
- [x] Graph network visualizer renders nodes with assigned slot colors and edges with shared student weights.
- [x] Seating plan matrices are readable and formatted for export or physical printing.
