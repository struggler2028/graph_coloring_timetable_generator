# Performance Analysis

## 1. Introduction

Performance analysis evaluates how efficiently the examination scheduling and seating-plan system processes academic data.

The main focus is on graph construction, conflict detection, graph coloring, room allocation, and seating-plan generation.

## 2. Important Performance Factors

The system's performance depends on:

- Number of students.
- Number of examinations.
- Number of examination conflicts.
- Number of available rooms.
- Number of students assigned to each examination.
- Complexity of the selected graph-coloring algorithm.

## 3. Algorithm Complexity

Let:

- V = Number of examination vertices.
- E = Number of conflict edges.
- S = Number of students.
- R = Number of available rooms.

| Operation | Expected Complexity | Purpose |
|---|---|---|
| Graph construction | Depends on enrollment data and conflict generation | Creates the conflict graph. |
| Conflict detection | Depends on student enrollments | Identifies shared-student examinations. |
| Greedy Coloring | O(V + E) for a fixed ordering with adjacency lists | Assigns time slots. |
| DSATUR | Depends on implementation; a simple implementation may take O(V² + E) | Selects vertices using saturation degree. |
| Room allocation | Depends on examinations and available rooms | Assigns rooms according to capacity. |
| Seating allocation | O(S) for a simple sequential assignment after room allocation | Assigns students to seats. |

## 4. Greedy Coloring Performance

Greedy Coloring is simple and requires less implementation effort.

Its result depends on the order in which examinations are processed.

A suitable vertex ordering may help reduce the number of time slots required.

## 5. DSATUR Performance

DSATUR selects examinations according to their saturation degree.

It gives priority to examinations that have more differently colored neighbouring examinations.

This can produce a timetable using fewer colors than a basic Greedy ordering in some graphs, although the result depends on the graph structure.

## 6. Algorithm Comparison

The project compares Greedy Coloring and DSATUR using:

- Number of time slots generated.
- Correctness of the timetable.
- Execution time.
- Behaviour with different conflict graphs.

Both algorithms must produce valid schedules in which connected examinations receive different colors.

## 7. Room Allocation Performance

Room allocation depends on the number of examinations, available rooms, and student counts.

The system should use available room capacity efficiently while ensuring that no room is assigned more students than it can accommodate.

If the available capacity is insufficient, the system should report the problem instead of generating an invalid allocation.

## 8. Scalability

The system should be tested with different input sizes:

- Small datasets with fewer students and examinations.
- Medium datasets with more courses and conflicts.
- Larger datasets with increased student enrollment and room requirements.

These tests can help identify performance limitations as the input size increases.

## 9. Expected Performance Results

The expected outcomes are:

- Correct identification of examination conflicts.
- Valid timetable generation using both algorithms.
- Comparison of the number of time slots used.
- Room allocation within capacity limits.
- Complete seating assignment for eligible students.
- Timely generation of timetable and seating-plan outputs.

Actual execution time and performance measurements should be recorded during testing.

## 10. Conclusion

Performance analysis helps evaluate the efficiency and correctness of the proposed examination scheduling system.

Comparing Greedy Coloring and DSATUR provides an understanding of how different graph-coloring approaches affect timetable generation.
