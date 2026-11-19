# Sprint 2 – Sprint Backlog

## 1. Selected User Stories

| ID | User Story | Priority | Story Points |
|---|---|---|---|
| US-04 | Examination Conflict Graph | High | 5 |
| US-05 | Conflict Detection | High | 3 |
| US-06 | Greedy Coloring | High | 5 |
| US-07 | DSATUR Scheduling | High | 5 |

**Total Story Points: 18**

## 2. Detailed Task Breakdown

### US-04: Examination Conflict Graph

- Represent each examination as a graph vertex.
- Create a graph data structure.
- Implement an adjacency list.
- Store examination relationships.
- Display graph vertices and edges.

### US-05: Conflict Detection

- Retrieve student-course enrollment information.
- Identify examinations taken by the same student.
- Compare examination enrollment lists.
- Create edges between conflicting examinations.
- Validate the generated conflict graph.

### US-06: Greedy Coloring

- Implement the Greedy Coloring algorithm.
- Select examinations in a defined order.
- Identify colors already used by neighbouring examinations.
- Assign the smallest available color.
- Generate time-slot allocations.
- Validate that conflicting examinations receive different colors.

### US-07: DSATUR Scheduling

- Calculate the degree of each examination vertex.
- Calculate saturation degree.
- Select the uncolored vertex with the highest saturation degree.
- Apply tie-breaking using vertex degree.
- Assign the smallest available color.
- Update neighbouring vertex saturation values.
- Generate the timetable.
- Compare the number of colors used with Greedy Coloring.

## 3. Acceptance Criteria

### US-04

- Each examination is represented by a vertex.
- Conflicting examinations are connected by edges.
- The graph represents the examination relationships correctly.

### US-05

- Shared-student examinations are identified.
- An edge is created for every conflicting examination pair.
- Examinations without shared students are not connected.

### US-06

- Greedy Coloring assigns a color to every examination.
- Connected examinations receive different colors.
- The generated time slots are displayed.

### US-07

- DSATUR selects vertices according to saturation degree.
- All examinations receive a valid color.
- Connected examinations receive different colors.
- The number of colors used can be compared with Greedy Coloring.

## 4. Sprint Priority

1. Examination conflict graph.
2. Conflict detection.
3. Greedy Coloring.
4. DSATUR scheduling.
5. Algorithm comparison.

## 5. Current Progress

Implementation and testing progress will be updated as tasks are completed.
