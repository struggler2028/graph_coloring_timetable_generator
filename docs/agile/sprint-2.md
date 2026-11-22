# Sprint 2 – Graph Construction & Timetable Generation Algorithms

## 1. Sprint Goal
Implement the examination conflict graph generator, conflict detection module, Greedy Graph Coloring, and the DSATUR algorithm with comparative benchmarking.

## 2. Sprint Information
- **Duration:** Week 2
- **Status:** Completed
- **Story Points Committed:** 21
- **Story Points Delivered:** 21

## 3. Backlog Items Delivered
- [x] **US02 & US03:** Automated conflict graph construction using student enrollment intersections with edge weight metrics.
- [x] **US04:** Greedy Graph Coloring algorithm implementation.
- [x] **US04:** DSATUR (Degree of Saturation) algorithm implementation with vertex degree tie-breaker.
- [x] **US05:** Algorithmic comparison service benchmarking color counts, runtime (ms), and distribution.
- [x] Conflict invariant verifier ensuring no two adjacent exams share the same color.

## 4. Key Decisions & Outcomes
- DSATUR dynamically computes the number of unique colors in the neighborhood of every uncolored vertex, prioritizing heavily constrained exams.
- Benchmarks showed DSATUR consistently achieves minimum chromatic number ($\chi(G)$), often using fewer time slots than naive Greedy on dense conflict networks.
- Full unit test suite (`test_graph_service.py`) written to validate coloring invariants.
