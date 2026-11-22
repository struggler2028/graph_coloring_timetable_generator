# Sprint 1 – Requirement Analysis, Architecture & Data Modeling

## 1. Sprint Goal
Analyze academic timetabling constraints, formalize graph-theoretic models, establish system architecture, and design data schemas for students, courses, exams, and rooms.

## 2. Sprint Information
- **Duration:** Week 1
- **Status:** Completed
- **Story Points Committed:** 18
- **Story Points Delivered:** 18

## 3. Backlog Items Delivered
- [x] **US01:** Data input schema definition for Students, Courses, Examinations, and Rooms.
- [x] Architectural design dividing responsibilities into Data Management, Graph Engine, Room Allocator, and Presentation.
- [x] Mathematical modeling of the examination conflict graph $G = (V, E)$.
- [x] Pydantic validation models ensuring data consistency and edge case handling.

## 4. Key Decisions & Outcomes
- Formulated the timetabling problem as a minimum vertex coloring problem where:
  $$V = \{E_1, E_2, \dots, E_n\}$$
  $$E = \{(E_i, E_j) \mid \text{Enrollment}(E_i) \cap \text{Enrollment}(E_j) \neq \emptyset\}$$
- Selected FastAPI and Python for backend engine performance and clean algorithmic representation.
- Designed UI wireframes and visual structure for graph exploration and schedule grid.
