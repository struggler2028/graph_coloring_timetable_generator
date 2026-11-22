# Team Contributions & Role Breakdown

## 1. Project Organization
The development of the **Dynamic Graph Coloring Based Exam Timetabling and Seating Plan Generator** was executed collaboratively following Agile engineering principles.

## 2. Role Assignments & Contributions

### 1. Product Owner & Architecture Lead
- Formulated the examination timetabling problem into graph-theoretic minimum vertex coloring ($G = (V, E)$).
- Defined requirements, user stories, acceptance criteria, and prioritized the Product Backlog.
- Guided the comparative evaluation between Greedy Coloring and the DSATUR algorithm.

### 2. Scrum Master & QA Lead
- Facilitated Agile ceremonies: Sprint Planning, Daily Standups, Sprint Reviews, and Retrospectives.
- Enforced the Definition of Done (DoD) and Definition of Ready (DoR).
- Designed and maintained the Requirements Traceability Matrix (`RTM`) and Risk Register.
- Automated CI testing workflows and verified 100% test pass rate across unit and API suites.

### 3. Algorithm & Backend Developer
- Implemented the core graph construction engine using student enrollment intersections.
- Developed the Greedy Graph Coloring and DSATUR saturation-degree scheduling algorithms.
- Built the room allocation engine sorting rooms by capacity descending and generating coordinate-based student seat matrices.
- Implemented FastAPI REST routes and automated test suites (`test_graph_service.py`, `test_api_endpoints.py`).

### 4. Frontend & Visualization Developer
- Integrated Cytoscape.js for interactive examination conflict graph visualization with dynamic color palettes and node dragging.
- Built the algorithm comparison dashboard, schedule grid, and seating matrix UI components.
- Implemented printable PDF styles and dynamic timetable regeneration workflows.
