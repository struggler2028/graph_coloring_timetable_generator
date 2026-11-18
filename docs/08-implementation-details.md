# Implementation Details

## 1. Introduction

The Dynamic Graph Coloring Based Exam Timetabling and Seating Plan Generator is designed using a modular architecture. The implementation combines graph-based scheduling algorithms, database management, room allocation, and an interactive web interface.

## 2. System Modules

### 2.1 Student Management
- Maintains student information.
- Stores student-course enrollment details.
- Provides data required for examination conflict detection.

### 2.2 Examination Management
- Maintains examination and subject details.
- Associates examinations with enrolled students.
- Provides the input required for timetable generation.

### 2.3 Graph Construction Module
- Represents each examination as a vertex.
- Creates an edge between two examinations if they share at least one student.
- Uses an adjacency-list representation to store graph connections.

### 2.4 Timetable Generation Module

The system implements two graph-coloring algorithms:

**Greedy Coloring**
- Processes vertices sequentially.
- Assigns the lowest available color.
- Each color represents an examination time slot.

**DSATUR Algorithm**
- Selects the uncolored vertex with the highest saturation degree.
- Uses vertex degree as a tie-breaking criterion.
- Dynamically assigns colors based on neighboring vertices.

### 2.5 Room Allocation Module
- Retrieves available examination rooms.
- Checks room capacity before allocation.
- Distributes students among available rooms.
- Identifies insufficient room capacity.

### 2.6 Seating Plan Generation
- Generates student seating arrangements.
- Organizes students according to allocated rooms.
- Produces structured seating-plan information.

### 2.7 Visualization and Export
- Displays the examination conflict graph.
- Presents the generated timetable.
- Displays room allocation and seating information.
- Supports PDF generation for seating plans.

## 3. Proposed Technology Implementation

| Component | Technology |
|---|---|
| Frontend | Next.js, React |
| Database | Supabase, PostgreSQL |
| Backend Logic | TypeScript, Node.js |
| Graph Visualization | Cytoscape.js / D3.js |
| Graph Algorithms | Greedy Coloring, DSATUR |
| PDF Generation | React PDF / Playwright |
| Version Control | Git, GitHub |
| Deployment | Vercel |

## 4. Implementation Workflow

1. Collect student, course, examination, and room information.
2. Store the information in the database.
3. Construct the examination conflict graph.
4. Execute graph-coloring algorithms.
5. Generate the examination timetable.
6. Allocate rooms according to capacity.
7. Generate seating arrangements.
8. Display and export the final results.

## 5. Expected Implementation Outcome

The implementation is expected to provide an integrated system that automates examination scheduling and seating allocation while reducing manual effort and preventing examination conflicts.
