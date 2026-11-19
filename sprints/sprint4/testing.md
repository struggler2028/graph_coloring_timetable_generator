# Sprint 4 – System Testing and Validation

## 1. Objective
To test the complete examination timetabling system and verify that all integrated modules work correctly.

## 2. Test Cases

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| TC-01 | Enter student and course details | Data is accepted and stored correctly |
| TC-02 | Generate examination conflict graph | Correct graph is generated |
| TC-03 | Run Greedy Coloring | Clash-free timetable is generated |
| TC-04 | Run DSATUR algorithm | Clash-free timetable is generated |
| TC-05 | Compare Greedy and DSATUR | Number of time slots is displayed |
| TC-06 | Allocate examination rooms | Suitable rooms are assigned |
| TC-07 | Check room capacity | Capacity is not exceeded |
| TC-08 | Generate seating plan | Students receive seat assignments |
| TC-09 | Change examination or enrollment data | Timetable can be regenerated |
| TC-10 | Generate PDF report | Report contains correct information |
| TC-11 | Enter invalid or incomplete data | Appropriate validation message is displayed |
| TC-12 | Test with a larger dataset | System generates results and performance is recorded |

## 3. Performance Testing
The system will be tested with different dataset sizes to observe:
- Graph construction time.
- Conflict detection time.
- Greedy Coloring execution time.
- DSATUR execution time.
- Overall timetable generation time.

## 4. Validation Criteria
- No two conflicting examinations share the same time slot.
- Room capacity is never exceeded.
- Every registered student receives a seat.
- Generated reports match the system output.
- Invalid inputs are handled properly.
- All integrated modules work together.

## 5. Test Results

The following validation activities are considered for the complete system:

- Student, course, examination, and room data are checked.
- Conflict graph generation is verified.
- Greedy Coloring and DSATUR are evaluated for clash-free scheduling.
- Room allocation is checked against available capacity.
- Seating plans are checked for completeness and duplicate assignments.
- Timetable regeneration is considered after changes in examination or enrollment data.
- PDF reports are checked for correct timetable and seating information.
- Invalid inputs are checked for appropriate error handling.
- Different dataset sizes are considered for performance evaluation.

These checks provide an overall evaluation framework for the integrated system.
