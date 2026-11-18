# System Architecture

## 1. Introduction

The Dynamic Graph Coloring Based Exam Timetabling and Seating Plan Generator is designed as a web-based application that automates examination scheduling and seating allocation.

The system accepts student, course, examination, and room information. It uses graph-coloring algorithms to generate a conflict-free timetable and then allocates students to rooms according to their capacities.

## 2. Architecture Overview

The proposed system consists of the following main layers:

1. **User Interface:** Allows administrators to enter academic data, manage rooms, generate timetables, and view seating plans.
2. **Application Logic:** Processes input data and coordinates graph construction, scheduling, and room allocation.
3. **Graph Processing Module:** Creates the examination conflict graph and applies Greedy Coloring and DSATUR.
4. **Database Layer:** Stores student, course, examination, room, and generated schedule information.
5. **Output Module:** Displays the timetable and seating arrangements and generates PDF reports.

## 3. Main System Modules

### 3.1 Input Management Module

This module collects:

- Student details.
- Course and subject details.
- Student-course enrollment information.
- Examination details.
- Room details and room capacities.

### 3.2 Conflict Graph Module

This module represents each examination as a vertex.

An edge is created between two examination vertices when they share at least one student.

The resulting graph represents all examination conflicts.

### 3.3 Timetable Generation Module

This module applies graph-coloring algorithms to assign examinations to time slots.

It supports:

- Greedy Coloring.
- DSATUR Coloring.

The generated schedules can be compared based on the number of colors or time slots used.

### 3.4 Room Allocation Module

After timetable generation, this module assigns available rooms to examinations.

Room allocation considers the number of students and the capacity of each room.

### 3.5 Seating Plan Module

This module generates an organized seating arrangement for students in their allocated examination rooms.

### 3.6 Visualization and Export Module

This module displays:

- Examination conflict graph.
- Generated timetable.
- Room allocation.
- Student seating arrangements.

It also supports generating a PDF of the seating plan.

## 4. Proposed System Workflow

1. Administrator enters student, course, examination, and room details.
2. System processes student-course enrollment information.
3. Conflict graph is constructed.
4. Greedy Coloring and DSATUR are applied.
5. Examinations are assigned to time slots.
6. Rooms are allocated according to capacity.
7. Students are assigned seats.
8. Timetable and seating plan are displayed.
9. Seating plan can be exported as a PDF.

## 5. Proposed Architecture Diagram

The following diagram represents the overall system flow:

```text
        Administrator
              |
              v
       Data Input Module
              |
              v
      Data Processing Module
              |
              v
      Examination Conflict Graph
              |
              v
       Graph Coloring Module
        /             \
       v               v
  Greedy Coloring    DSATUR
        \             /
         v           v
       Timetable Generation
              |
              v
        Room Allocation
              |
              v
       Seating Plan Generation
              |
              v
       Display and PDF Export
```

## 6. Proposed Technology Architecture

The detailed technology proposal includes:

- Next.js and React for the web application.
- TypeScript and Node.js for application and algorithm logic.
- Supabase with PostgreSQL for database storage.
- Cytoscape.js or D3.js for graph visualization.
- @react-pdf/renderer or Playwright for PDF generation.
- Optional Python FastAPI and NetworkX for advanced graph processing.

The final technology stack should be confirmed by the team before implementation.

## 7. Conclusion

The proposed architecture separates data management, graph processing, timetable generation, room allocation, and output generation into different modules.

This structure makes the system easier to develop, test, maintain, and extend.
