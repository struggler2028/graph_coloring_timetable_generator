# Testing and Validation

## 1. Introduction

Testing is important to ensure that the examination timetable and seating plan are generated correctly.

The system should be checked for examination conflicts, graph-coloring correctness, room capacity, and seating allocation.

## 2. Testing Objectives

- Verify correct examination conflict detection.
- Ensure that shared-student examinations are not scheduled together.
- Check Greedy Coloring and DSATUR results.
- Verify room allocation according to capacity.
- Ensure every student receives a valid seat.
- Check timetable regeneration after input changes.
- Verify PDF generation.

## 3. Types of Testing

### 3.1 Unit Testing

Individual modules are tested separately.

Examples:

- Conflict detection.
- Graph construction.
- Greedy Coloring.
- DSATUR.
- Room allocation.
- Seating assignment.

### 3.2 Integration Testing

Different modules are tested together.

Examples:

- Student data with conflict graph generation.
- Graph coloring with timetable generation.
- Timetable with room allocation.
- Room allocation with seating-plan generation.

### 3.3 Functional Testing

The complete application is checked to ensure that its main features work as expected.

Examples:

- Adding student and examination details.
- Generating the timetable.
- Viewing the conflict graph.
- Exporting the seating plan.

### 3.4 Validation Testing

Generated results are checked against the project requirements.

The main checks include conflict-free scheduling, room capacity compliance, and complete student seating allocation.

## 4. Proposed Test Cases

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| TC01 | Add valid student and course details | Data should be accepted. |
| TC02 | Add examination details | Examination records should be stored. |
| TC03 | Two examinations share students | A conflict edge should be created. |
| TC04 | Two examinations have no shared students | No conflict edge should be created. |
| TC05 | Generate timetable using Greedy Coloring | Conflicting examinations should receive different colors. |
| TC06 | Generate timetable using DSATUR | Conflicting examinations should receive different colors. |
| TC07 | Compare both coloring algorithms | Number of colors used should be displayed. |
| TC08 | Allocate rooms with sufficient capacity | Students should be assigned without exceeding room capacity. |
| TC09 | Available room capacity is insufficient | System should report an allocation problem. |
| TC10 | Generate seating plan | Every student should receive a valid room and seat assignment. |
| TC11 | Change student enrollment information | Conflict graph and timetable should be regenerated. |
| TC12 | Export seating plan | A structured PDF should be generated. |

## 5. Validation Criteria

The system should satisfy the following conditions:

1. No two examinations connected by an edge should have the same time-slot color.
2. Every examination should receive a valid time slot.
3. Room allocation should not exceed the capacity of any room.
4. Every student should be assigned to an available seat.
5. Changes in input data should be reflected in regenerated outputs.
6. The generated seating-plan PDF should contain the required examination and student information.

## 6. Testing Data

Sample test data should include:

- Multiple students.
- Different courses and examinations.
- Students enrolled in overlapping courses.
- Examinations without shared students.
- Rooms with different seating capacities.
- Cases where room capacity is insufficient.

This data will help verify both normal and special scheduling conditions.

## 7. Issue Tracking

Issues found during development and testing should be recorded in GitHub Issues.

Each issue should include:

- Description of the problem.
- Steps to reproduce it.
- Expected result.
- Actual result.
- Current status.

## 8. Conclusion

Testing and validation help ensure that the generated timetable is conflict-free and that room allocation follows capacity restrictions.

The proposed test cases cover the main functions of the system and help identify errors before the final demonstration.
