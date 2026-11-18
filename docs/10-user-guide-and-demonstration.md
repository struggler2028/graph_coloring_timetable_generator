# User Guide and Demonstration

## 1. Introduction

This document explains the proposed workflow for using the Dynamic Graph Coloring Based Exam Timetabling and Seating Plan Generator.

The system is intended primarily for administrators who manage examination information, generate timetables, and prepare seating arrangements.

## 2. System Access

1. Open the application through the configured local or deployed application URL.
2. Access the main application interface.
3. Navigate to the examination management functionality.

## 3. Managing Input Data

The administrator provides the required information:

### Student Information
- Student details.
- Student identification.
- Course enrollment information.

### Examination Information
- Examination details.
- Subject information.
- Associated student records.
- Scheduling requirements.

### Room Information
- Room identification.
- Room capacity.
- Available examination rooms.

## 4. Generating the Conflict Graph

1. Retrieve student enrollment information.
2. Create a vertex for every examination.
3. Identify examinations sharing common students.
4. Connect conflicting examinations using graph edges.
5. Display the generated conflict graph.

The resulting graph represents the examination scheduling constraints.

## 5. Generating the Examination Timetable

The system uses two graph-coloring approaches:

### Greedy Coloring
- Processes examinations sequentially.
- Assigns the lowest available color.
- Converts colors into examination time slots.

### DSATUR Algorithm
- Selects examinations according to saturation degree.
- Prioritizes examinations with highly constrained neighboring vertices.
- Assigns available colors dynamically.

The generated schedules can be compared based on the number of time slots used.

## 6. Room Allocation

1. Retrieve examinations assigned to each time slot.
2. Obtain the corresponding student lists.
3. Check available room capacities.
4. Assign students to suitable rooms.
5. Verify that allocated students do not exceed room capacity.

If the available capacity is insufficient, the system should report the allocation problem.

## 7. Seating Plan Generation

After room allocation:

- Generate room-wise student lists.
- Organize student seating information.
- Associate seating arrangements with examination sessions.
- Prepare structured seating-plan output.

## 8. Viewing and Exporting Results

The administrator can review the generated results:

- Examination conflict graph.
- Examination timetable.
- Room allocation.
- Student seating arrangements.

The proposed system also supports generating PDF seating plans for distribution and record keeping.

## 9. Demonstration Workflow

The project demonstration can follow this sequence:

1. Introduce the examination scheduling problem.
2. Show the student, course, examination, and room inputs.
3. Demonstrate examination conflict graph construction.
4. Execute Greedy Coloring.
5. Execute DSATUR.
6. Compare the generated time slots.
7. Demonstrate room allocation.
8. Generate the seating plan.
9. Display and export the final results.

## 10. Conclusion

The proposed application demonstrates how graph coloring and constraint-based allocation can automate examination scheduling and seating arrangements.

It aims to minimize examination clashes, improve room utilization, and reduce the administrative effort required for manual examination planning.
