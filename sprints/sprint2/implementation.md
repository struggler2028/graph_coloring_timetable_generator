# Sprint 2 – Implementation Details

## 1. Introduction

This document records the implementation activities performed during Sprint 2 of the Dynamic Graph Coloring Based Exam Timetabling and Seating Plan Generator.

The objective is to develop the examination conflict graph, identify scheduling conflicts, and implement graph-coloring algorithms for timetable generation.

## 2. Technologies Used

The proposed technologies include:

- TypeScript and Node.js for graph and algorithm logic.
- Next.js and React for application integration.
- Supabase with PostgreSQL for academic data storage.
- Cytoscape.js or D3.js for graph visualization.
- Git and GitHub for version control.

The final technologies used will be updated according to the team's implementation.

## 3. Source Code Modules

The implementation is expected to contain modules for:

| Module | Responsibility |
|---|---|
| Graph Module | Creates and manages the examination conflict graph. |
| Conflict Detection Module | Identifies shared-student examination conflicts. |
| Greedy Coloring Module | Assigns time slots using Greedy Coloring. |
| DSATUR Module | Assigns time slots using saturation degree. |
| Timetable Module | Generates and stores examination time slots. |
| Visualization Module | Displays the conflict graph and generated results. |

Actual source filenames will be recorded after implementation.

## 4. Graph Representation

The examination conflict graph is represented as:

G = (V, E)

Where:

- V represents examinations.
- E represents conflicts between examinations.

Each examination is stored as a vertex. An edge is created between two examinations if at least one student is enrolled in both.

An adjacency list is used to represent the connections between examination vertices.

## 5. Conflict Detection Implementation

The system processes student-course enrollment information to identify overlapping examinations.

The implementation follows these steps:

1. Retrieve examination enrollment data.
2. Identify examinations associated with each student.
3. Find examination pairs sharing students.
4. Create edges between conflicting examination vertices.
5. Store the resulting conflict graph.

## 6. Greedy Coloring Implementation

Greedy Coloring assigns colors to examinations one by one.

The implementation:

- Checks the colors of neighbouring examinations.
- Finds the smallest available color.
- Assigns that color to the current examination.
- Repeats the process until all examinations are scheduled.

Each color represents a time slot.

## 7. DSATUR Implementation

DSATUR selects the next examination according to its saturation degree.

The implementation:

- Calculates the degree of each vertex.
- Identifies uncolored vertices.
- Selects the vertex with the highest saturation degree.
- Uses vertex degree to break ties.
- Assigns the smallest available color.
- Updates neighbouring saturation degrees.

## 8. Timetable Generation

After coloring, examinations are grouped according to their assigned colors.

Each color represents one examination time slot.

The system can display the generated timetable and compare the number of time slots produced by Greedy Coloring and DSATUR.

## 9. Implementation Evidence

The following evidence will be added after successful implementation:

- Conflict graph screenshot.
- Conflict detection output.
- Greedy Coloring execution output.
- DSATUR execution output.
- Generated timetable screenshot.
- GitHub commit references.

## 10. Implementation Status

Actual implementation progress and verified results will be updated as development progresses.

## 11. Conclusion

Sprint 2 focuses on the core graph algorithms of the project.

The conflict graph, Greedy Coloring, and DSATUR form the foundation for generating examination timetables without shared-student clashes.
