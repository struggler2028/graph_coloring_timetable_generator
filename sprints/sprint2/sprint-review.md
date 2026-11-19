# Sprint 2 – Review and Retrospective

## 1. Sprint Review Overview

Sprint 2 focuses on developing the examination conflict graph and implementing graph-coloring algorithms.

The review will evaluate conflict detection, graph construction, Greedy Coloring, DSATUR, and timetable generation.

## 2. Planned Deliverables

- Examination conflict graph.
- Shared-student conflict detection.
- Greedy Coloring implementation.
- DSATUR implementation.
- Generated examination timetable.
- Comparison of algorithm results.

## 3. Sprint Outcomes

Sprint 2 focuses on defining the examination conflict graph and timetable generation methods. Greedy Coloring and DSATUR are used to assign examinations to different time slots while avoiding clashes between examinations sharing students.

## 4. Demonstration

The planned demonstration includes:
- Displaying examinations as graph vertices.
- Showing edges between conflicting examinations.
- Running Greedy Coloring.
- Running DSATUR.
- Comparing the number of time slots generated.
- Checking that conflicting examinations are assigned different time slots.

## 5. Sprint Review

The graph representation and coloring algorithms provide the scheduling foundation of the system. The generated time slots are used as input for room allocation and seating plan generation in Sprint 3.

## 6. Retrospective

### What Went Well?
- Graph coloring provides a suitable approach for examination scheduling.
- Greedy Coloring and DSATUR offer two methods for comparison.
- Conflict detection is based on shared student enrollment.

### Challenges Faced
- Correctly identifying examination conflicts.
- Choosing an appropriate vertex ordering for Greedy Coloring.
- Handling vertices with similar saturation degrees in DSATUR.
- Comparing algorithm results fairly.

### Improvements for Next Sprint
- Connect timetable output with room allocation.
- Implement seating plan generation.
- Validate room capacity and student assignments.

## 7. Sprint Status
Sprint 2 defines the core graph-based scheduling approach and prepares the system for room allocation and seating plan development.

## 8. Sprint Conclusion

Sprint 2 develops the main graph-based scheduling functionality of the project.

Its final completion status will be determined after implementation, testing, and sprint review.
