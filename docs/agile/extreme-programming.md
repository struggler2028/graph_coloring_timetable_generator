# Extreme Programming (XP) Practices

To ensure maximum software reliability and mathematical accuracy, the development team incorporated core **Extreme Programming (XP)** engineering practices alongside Scrum:

## 1. Test-Driven Development (TDD)
- **Red-Green-Refactor Cycle:**
  1. **Red:** Write failing unit tests for graph conflict detection, edge construction, and vertex coloring before writing algorithm code.
  2. **Green:** Implement the minimal code necessary to satisfy conflict invariants and chromatic bounds.
  3. **Refactor:** Clean up adjacency lookups, optimize saturation maps, and decouple room allocation from graph models.
- **Coverage:** High test coverage across `test_graph_service.py` and `test_api_endpoints.py`.

## 2. Pair Programming
- Critical algorithmic segments—specifically the DSATUR degree-of-saturation selection logic and room capacity distribution—were developed using pair programming to eliminate off-by-one errors and subtle tie-breaking discrepancies.

## 3. Continuous Integration (CI)
- An automated GitHub Actions CI pipeline (`.github/workflows/ci.yml`) runs on every push and pull request.
- The pipeline executes linting and full pytest test suites across multiple environments to ensure regressions are caught instantaneously.

## 4. Collective Code Ownership & Refactoring
- All team members have access to the full repository.
- Algorithms are modularized into independent services (`conflict_graph.py`, `graph_coloring.py`, `room_allocator.py`, `timetable_generator.py`) allowing continuous refactoring without breaking public API contracts.

## 5. Simple Design (KISS & YAGNI)
- Start with clean in-memory adjacency list data structures.
- Avoid over-engineered ORMs or complex databases where fast in-memory graph operations are more optimal for scheduling computations.
