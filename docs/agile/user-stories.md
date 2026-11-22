# Detailed User Stories & Acceptance Criteria

This document details all Product Backlog User Stories, their business value, acceptance criteria, and verification methods.

---

### US01: Data Input & Academic Record Management
- **As an** examination administrator,
- **I want to** enter student records, courses, exams, and rooms with capacities,
- **So that** complete scheduling data is available for processing.
- **Acceptance Criteria:**
  - System accepts structured JSON or UI form inputs with proper validation.
  - Student enrollments are mapped to specific course codes.
  - Invalid records (missing codes or negative capacities) are rejected.

---

### US02: Conflict Graph Construction
- **As an** examination administrator,
- **I want** the system to construct a conflict graph where vertices represent examinations and edges represent shared student enrollments,
- **So that** potential scheduling clashes can be represented mathematically.
- **Acceptance Criteria:**
  - Each examination is uniquely mapped to a graph vertex $v \in V$.
  - An edge $(u, v) \in E$ is formed if and only if $\text{Enrolled}(u) \cap \text{Enrolled}(v) \neq \emptyset$.
  - The edge weight records the number of shared students.

---

### US03: Conflict Detection & Inspection
- **As an** examination administrator,
- **I want to** inspect the exact students causing an examination conflict,
- **So that** I understand why two exams cannot be held concurrently.
- **Acceptance Criteria:**
  - Graph API returns the list of student IDs for every conflict edge.
  - Clicking on a node in the UI highlights all conflicting neighbors.

---

### US04: Graph Coloring Timetable Scheduling (Greedy & DSATUR)
- **As an** examination administrator,
- **I want** the system to automatically assign examinations to time slots using graph coloring,
- **So that** no overlapping examinations are scheduled for shared students and total exam days are minimized.
- **Acceptance Criteria:**
  - Zero-conflict guarantee: $\forall (u, v) \in E \implies \text{color}(u) \neq \text{color}(v)$.
  - Supports Greedy Coloring and DSATUR algorithms.
  - Colors are mapped directly to sequential dates and time slots (Morning / Afternoon).

---

### US05: Algorithm Comparison & Benchmarking
- **As an** examination administrator,
- **I want to** compare Greedy Coloring and DSATUR side-by-side,
- **So that** I can evaluate chromatic performance, time slots saved, and execution efficiency.
- **Acceptance Criteria:**
  - Displays total time slots used by both algorithms.
  - Displays execution time in milliseconds.
  - Highlights color distribution and recommendations.

---

### US06: Room Allocation by Capacity
- **As an** examination administrator,
- **I want** rooms to be allocated to examinations in each session based on room capacity,
- **So that** student occupancy does not exceed room limits.
- **Acceptance Criteria:**
  - High-capacity rooms are assigned first to large exams.
  - Total allocated candidates in a room $\le$ room capacity.
  - If an exam exceeds a single room's capacity, candidates are systematically split across multiple rooms.

---

### US07: Insufficient Capacity Warnings
- **As an** examination administrator,
- **I want** immediate alerts if available room capacity is insufficient for the candidates in a session,
- **So that** I can add rooms or adjust room assignments without silent failures.
- **Acceptance Criteria:**
  - Warnings emitted with unallocated student counts and specific examination details.
  - Visible warning banner displayed in the UI.

---

### US08: Structured Student Seating Plan
- **As an** examination administrator,
- **I want** an organized seating plan with Row and Column seat coordinates for each allocated room,
- **So that** invigilators can systematically seat candidates and prevent malpractice.
- **Acceptance Criteria:**
  - Generates clear coordinates: `R01-S01`, `R01-S02`, etc.
  - Associates each seat with the candidate's Roll No, Name, and Course.

---

### US09: Interactive Graph Visualizer
- **As an** examination administrator,
- **I want** an interactive visualization of the examination conflict network,
- **So that** I can explore the schedule visually.
- **Acceptance Criteria:**
  - Nodes colored according to assigned time slots.
  - Interactive dragging, zooming, panning, and tap-to-inspect panel.

---

### US10: Printable / PDF Export
- **As an** examination administrator,
- **I want to** export or print the generated timetable and seating plan,
- **So that** hard copies can be published on campus notice boards and distributed to invigilators.
- **Acceptance Criteria:**
  - Clean print-friendly CSS formatting removing UI controls and header bars.
  - Formatted tabular output for both timetable and seating arrangements.
