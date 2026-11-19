# Sprint 3 – Testing and Validation

## 1. Objective
To verify that room allocation, seating plan generation, and backend integration work correctly.

## 2. Test Cases

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| TC-01 | Allocate a room to an examination | Suitable room is assigned |
| TC-02 | Allocate students within room capacity | Allocation is successful |
| TC-03 | Student count exceeds one room's capacity | Additional suitable room is considered, if available |
| TC-04 | Total available capacity is insufficient | System reports insufficient capacity |
| TC-05 | Generate seating plan | Students receive seat assignments |
| TC-06 | Check duplicate student allocation | No duplicate seat assignment |
| TC-07 | Check room capacity after seating | Capacity is not exceeded |
| TC-08 | Check all registered students | Every student is assigned a seat |
| TC-09 | Integrate timetable with room allocation | Correct examination details are retrieved |
| TC-10 | Integrate room allocation with seating plan | Seating plan uses the allocated room details |

## 3. Validation Criteria
- Room capacity must not be exceeded.
- All registered students must be considered.
- No duplicate seat allocation should occur.
- Room and seating details must match the examination timetable.
- Integration errors should be handled properly.

## 4. Test Results
The following validation checks are considered for Sprint 3:

- Suitable rooms are selected for examinations.
- The total assigned students do not exceed available room capacity.
- Insufficient room capacity is identified.
- Students are assigned seats in their allocated rooms.
- Duplicate seat assignments are avoided.
- All registered students are considered during seating allocation.
- Room and seating details match the generated examination timetable.

These checks help verify the correctness of room allocation and seating plan logic.
