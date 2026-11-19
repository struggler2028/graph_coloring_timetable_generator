# Sprint 2 – Testing and Validation

## 1. Testing Objective

The objective of Sprint 2 testing is to verify the correctness of examination conflict detection, graph construction, Greedy Coloring, DSATUR, and timetable generation.

## 2. Planned Test Cases

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| TC-01 | Create an examination vertex | Examination is added to the graph. |
| TC-02 | Two examinations share students | A conflict edge is created. |
| TC-03 | Two examinations have no shared students | No conflict edge is created. |
| TC-04 | One student has multiple examinations | All relevant examination conflicts are identified. |
| TC-05 | Generate the conflict graph | All identified vertices and edges are displayed. |
| TC-06 | Run Greedy Coloring | Every examination receives a valid color. |
| TC-07 | Run DSATUR | Every examination receives a valid color. |
| TC-08 | Check conflicting examinations | Connected examinations receive different colors. |
| TC-09 | Compare both algorithms | Number of colors used is displayed. |
| TC-10 | Generate the timetable | Examinations are grouped into time slots. |
| TC-11 | Use a graph with no conflicts | All examinations can be assigned the same color. |
| TC-12 | Use a graph with multiple conflicts | The generated timetable avoids examination clashes. |

## 3. Testing Approach

Testing will be performed using:

- Unit testing of graph operations.
- Conflict detection testing.
- Algorithm testing.
- Timetable generation testing.
- Manual verification using sample enrollment data.

## 4. Testing Results

Actual results and pass/fail status will be recorded after execution.

| Test ID | Actual Result | Status |
|---|---|---|
| TC-01 to TC-12 | Pending execution | Not Tested |

## 5. Validation Criteria

The generated timetable must satisfy the following conditions:

1. Every examination must receive a time slot.
2. Two examinations sharing students must not receive the same time slot.
3. The conflict graph must correctly represent shared-student conflicts.
4. Both algorithms must produce valid schedules.
5. The number of colors used by each algorithm must be recorded correctly.

## 6. Defect Tracking

Any incorrect conflict edges, invalid color assignments, algorithm errors, or timetable generation issues will be documented and resolved.

## 7. Conclusion

Sprint 2 testing will validate the graph representation and scheduling algorithms.

The results will help ensure that the generated timetable avoids examination clashes before room allocation begins in Sprint 3.
