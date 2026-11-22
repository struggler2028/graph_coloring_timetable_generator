# Dynamic Graph Coloring Based Exam Timetabling & Seating Plan Generator

[![CI Build](https://github.com/struggler2028/graph_coloring_timetable_generator/actions/workflows/ci.yml/badge.svg)](https://github.com/struggler2028/graph_coloring_timetable_generator/actions)
[![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Pytest](https://img.shields.io/badge/pytest-8.0+-0A9EDC.svg?logo=pytest&logoColor=white)](https://pytest.org)
[![Cytoscape](https://img.shields.io/badge/Visualization-Cytoscape.js-orange.svg)](https://js.cytoscape.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An automated, mathematically validated academic examination timetabling and room-wise seating plan generator. The system represents examination conflicts as a graph, applies **DSATUR** and **Greedy Graph Coloring** to minimize time slots with zero clashes, validates room capacities, and generates structured candidate seating matrices.

---

## 🏛️ System Architecture

```text
               Administrator / Academic Data
                             |
                             v
           +-----------------------------------+
           |        Data Input & Models        |
           | (Students, Courses, Exams, Rooms) |
           +-----------------------------------+
                             |
                             v
           +-----------------------------------+
           |    Examination Conflict Graph     |
           |             G = (V, E)            |
           |     Vertices: Exam Sessions       |
           |     Edges: Shared Students        |
           +-----------------------------------+
                             |
              +--------------+--------------+
              |                             |
              v                             v
     +-----------------+           +-----------------+
     | Greedy Coloring |           |     DSATUR      |
     |   (Sequential)  |           | (Max Saturation)|
     +-----------------+           +-----------------+
              |                             |
              +--------------+--------------+
                             |
                             v
           +-----------------------------------+
           |       Timetable Generation        |
           | (Clash-Free Session Slot Mapping) |
           +-----------------------------------+
                             |
                             v
           +-----------------------------------+
           |      Room Capacity Allocation     |
           | (Capacity Bounds & Multi-Room)    |
           +-----------------------------------+
                             |
                             v
           +-----------------------------------+
           |      Seating Plan Generation      |
           | (Systematic Row x Col Coordinates)|
           +-----------------------------------+
                             |
              +--------------+--------------+
              |                             |
              v                             v
     +------------------+         +-------------------+
     | Cytoscape.js Web |         | Printable / PDF   |
     | Graph Visualizer |         | Export Reports    |
     +------------------+         +-------------------+
```

---

## 🚀 Key Features

1. **Zero-Clash Conflict Detection:**
   - Automatically builds an adjacency network $G = (V, E)$.
   - Connects examinations with an edge if at least one student is enrolled in both.
   - Eliminates examination overlap for all cross-enrolled students.

2. **Graph Coloring Algorithms:**
   - **DSATUR (Degree of Saturation):** Dynamically prioritizes vertices with the highest number of distinct neighbor colors, with vertex degree as tie-breaker. Consistently achieves minimal chromatic bounds ($\chi(G)$).
   - **Greedy Coloring:** Rapid sequential assignment for baseline comparison.
   - **Benchmarking Engine:** Side-by-side metrics comparing time slots used, color distribution, and execution runtime (ms).

3. **Room Allocation & Capacity Checks:**
   - Sorts available examination rooms by capacity descending.
   - Allocates rooms per time slot without exceeding physical capacity bounds.
   - Emits alerts and shortage reports if capacity is exceeded.

4. **Structured Student Seating Plans:**
   - Coordinates students systematically into `Row`, `Col`, and `SeatNumber` (e.g. `R01-S01`).
   - Handles multi-room exam splits without student duplication.

5. **Interactive Cytoscape.js Network Visualizer:**
   - Physics-based interactive force-directed graph (`cose` layout).
   - Color-coded nodes indicating assigned examination time slots.
   - Interactive node tapping to inspect degree, saturation, and conflicting neighbors.

6. **Administrative PDF / Print View:**
   - Print-friendly CSS media queries formatting clean notice-board tables and seating rosters.

---

## 📁 Repository Structure

```text
graph_coloring_timetable_generator/
├── .github/
│   └── workflows/
│       └── ci.yml                          # GitHub Actions automated test workflow
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes.py                   # REST API routes
│   │   │   └── sample_data.py              # Realistic university benchmark dataset
│   │   ├── models/
│   │   │   └── schemas.py                  # Pydantic schemas (Student, Exam, Room, etc.)
│   │   ├── services/
│   │   │   ├── conflict_graph.py           # Adjacency list builder & conflict analyzer
│   │   │   ├── graph_coloring.py           # Greedy & DSATUR algorithms
│   │   │   ├── room_allocator.py           # Capacity checks & room distribution
│   │   │   └── timetable_generator.py      # Master timetable coordinator
│   │   ├── __init__.py
│   │   └── main.py                         # FastAPI application entrypoint
│   └── tests/
│       ├── test_api_endpoints.py           # REST API integration tests
│       ├── test_graph_service.py           # Unit tests for graph coloring & seating
│       ├── pytest.ini                      # Pytest configuration
│       └── requirements.txt                # Python backend dependencies
├── frontend/
│   ├── index.html                          # Interactive dashboard & Cytoscape visualizer
│   └── package.json                        # Frontend metadata & scripts
├── docs/
│   ├── agile/                              # Full Agile Scrum documentation suite
│   │   ├── agile-methodology.md
│   │   ├── daily-standups.md
│   │   ├── definition-of-done.md
│   │   ├── definition-of-ready.md
│   │   ├── extreme-programming.md
│   │   ├── kanban-workflow.md
│   │   ├── product-backlog.md
│   │   ├── risk-register.md
│   │   ├── sprint-1.md
│   │   ├── sprint-2.md
│   │   ├── sprint-3.md
│   │   ├── sprint-4.md
│   │   ├── sprint-planning.md
│   │   ├── sprint-retrospectives.md
│   │   ├── sprint-reviews.md
│   │   ├── team-contributions.md
│   │   └── user-stories.md
│   └── testing/
│       └── requirements-traceability-matrix.md
├── sprints/                                # Sprint execution documentation
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
└── README.md
```

---

## ⚡ Quick Start Guide

### 1. Prerequisites
- **Python 3.10+**
- **pip**

### 2. Setup Backend & Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 3. Run Automated Tests
```bash
cd backend
pytest -v
```

Expected output:
```text
tests/test_api_endpoints.py::test_health_check_endpoint PASSED           [ 10%]
tests/test_api_endpoints.py::test_sample_data_endpoint PASSED            [ 20%]
tests/test_api_endpoints.py::test_generate_timetable_endpoint PASSED     [ 30%]
tests/test_api_endpoints.py::test_compare_algorithms_endpoint PASSED     [ 40%]
tests/test_graph_service.py::test_conflict_graph_shared_students PASSED  [ 50%]
tests/test_graph_service.py::test_greedy_coloring_validity PASSED        [ 60%]
tests/test_graph_service.py::test_dsatur_coloring_bipartite_and_tie_breaker PASSED [ 70%]
tests/test_graph_service.py::test_room_allocation_respects_capacity PASSED [ 80%]
tests/test_graph_service.py::test_room_allocation_insufficient_capacity_warning PASSED [ 90%]
tests/test_graph_service.py::test_timetable_generator_both_comparison PASSED [100%]

======================== 10 passed in 5.04s ========================
```

### 4. Launch the Web Application
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
- **Web Dashboard & Visualizer:** Open `http://localhost:8000/` in your browser.
- **Interactive Swagger API Docs:** Open `http://localhost:8000/docs`.

---

## 📊 Algorithm Performance & Comparison

| Metric | Greedy Coloring | DSATUR Algorithm |
|---|---|---|
| **Vertex Selection** | Fixed / Sequential Ordering | Dynamic Maximum Saturation Degree |
| **Tie-Breaker** | None | Highest Degree in Graph |
| **Chromatic Minimization** | Order-dependent; can use suboptimal colors | Near-optimal / Minimum Chromatic Number $\chi(G)$ |
| **Time Complexity** | $O(V + E)$ | $O(V^2 + E)$ |
| **Conflict Verification** | Guaranteed 0 Clashes | Guaranteed 0 Clashes |

---

## 🧪 Agile Engineering Practices
- **Framework:** Scrum combined with Extreme Programming (XP) practices.
- **Sprints:** 4 time-boxed sprints covering Requirements, Graph Algorithms, Room Allocation, and Visualization.
- **Test-Driven Development (TDD):** Full unit and integration testing suite.
- **Traceability:** Requirements Traceability Matrix (`RTM`) mapping 100% of functional requirements to tests.

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
