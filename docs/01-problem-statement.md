# Dynamic Graph Coloring Based Exam Timetabling and Seating Plan Generator

## 1. Project Overview

The Dynamic Graph Coloring Based Exam Timetabling and Seating Plan Generator is a web-based system designed to automate examination scheduling and seating allocation.

The system represents examinations as vertices in a graph. An edge connects two examinations when they share at least one student, indicating that they cannot be scheduled in the same time slot. Graph-coloring algorithms are used to assign examinations to time slots while avoiding clashes. Once a timetable is generated, the system allocates students to rooms according to room capacity and produces an organized seating plan.

## 2. Problem Statement

Manual examination scheduling is time-consuming and may lead to:
- Two examinations being scheduled at the same time for students who share courses.
- Uneven or inefficient use of examination rooms.
- Seating arrangements that are difficult to prepare and manage manually.
- Additional work when examination details or constraints change.

The project aims to provide an automated system that generates a valid examination timetable and a practical seating plan using graph coloring and constraint-based allocation.

## 3. Objectives

- Represent examination conflicts using a graph structure.
- Detect conflicts between examinations that share students.
- Generate a timetable with no overlapping examinations for shared students.
- Compare Greedy Coloring and DSATUR-based scheduling.
- Allocate rooms according to their available capacity.
- Generate an organized seating arrangement for each examination session.
- Allow the timetable and seating plan to be regenerated when inputs or constraints change.
- Provide clear outputs that administrators can view and export.

## 4. Proposed Approach

1. Collect student, course, examination, and room information.
2. Construct a conflict graph in which each vertex represents an examination and an edge represents a shared-student conflict.
3. Apply Greedy Coloring and DSATUR to assign examinations to time slots.
4. Compare the number of colors (time slots) used by the algorithms.
5. Allocate students to available rooms while respecting room capacities.
6. Display the generated graph, timetable, and seating arrangements.
7. Generate a structured PDF of the seating plan.

## 5. Expected Outcome

The expected result is a functional prototype that accepts academic and room information and generates a conflict-free examination timetable together with a practical seating plan. It demonstrates the application of graph coloring to an academic scheduling problem and aims to reduce the effort involved in manual timetable and seating preparation.
