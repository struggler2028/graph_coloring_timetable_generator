# Sprint Retrospectives & Continuous Improvement

At the end of each sprint, the team conducts a Sprint Retrospective using the **Start-Stop-Continue** and **What Went Well / What Can Be Improved** models.

---

## Sprint 1 Retrospective
- **What Went Well:**
  - Clear formalization of the graph coloring problem formulation $G = (V, E)$.
  - Fast consensus on Pydantic schemas for students, courses, exams, and rooms.
- **What Can Be Improved:**
  - Need realistic academic sample datasets with overlapping elective courses to properly stress test conflict density.
- **Action Items:**
  - Create a realistic 25-student, 10-course, 4-room benchmark scenario for Sprint 2 testing.

---

## Sprint 2 Retrospective
- **What Went Well:**
  - DSATUR algorithm implementation correctly prioritized vertices with higher saturation degrees.
  - Test-Driven Development (TDD) successfully caught color collision edge cases before code integration.
- **What Can Be Improved:**
  - Greedy coloring order needed to be deterministic to allow reproducible test benchmarks.
- **Action Items:**
  - Enforce sorted vertex ordering for baseline Greedy evaluation.

---

## Sprint 3 Retrospective
- **What Went Well:**
  - Room allocation accurately distributed candidates across rooms in descending capacity order.
  - Coordinate-based seating matrices (`Row`, `Col`) prevented student seat collisions.
- **What Can Be Improved:**
  - Handled single-room shortages, but needed clearer aggregate warning reporting when the entire campus is over capacity.
- **Action Items:**
  - Add explicit structured warning objects to the API response.

---

## Sprint 4 Retrospective
- **What Went Well:**
  - Cytoscape.js visualizer renders clear physics-based networks with interactive node inspection.
  - 100% test pass rate across unit and API integration suites.
  - Print-friendly CSS allows clean PDF generation directly from the browser.
- **Overall Project Takeaway:**
  - Applying graph coloring to exam scheduling eliminates manual administrative clashing and optimizes examination periods.
