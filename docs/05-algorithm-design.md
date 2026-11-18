# Algorithm Design

## 1. Introduction

The main objective of the project is to generate an examination timetable without clashes and create an organized seating plan.

Graph coloring is used to represent examination conflicts and assign examinations to different time slots.

## 2. Graph Representation

The examination conflict graph is represented as:

G = (V, E)

Where:

- V represents the set of examinations.
- E represents the set of conflicts between examinations.

Each vertex represents one examination.

An edge connects two vertices if at least one student is enrolled in both examinations.

Therefore, two connected examinations cannot be scheduled in the same time slot.

## 3. Conflict Detection

Conflict detection identifies examinations that share students.

### Steps

1. Read student-course enrollment information.
2. Identify the examinations associated with each student.
3. Compare examinations taken by the same student.
4. Create an edge between every conflicting pair.
5. Store the resulting conflict graph.

### Example

Consider three examinations:

- E1: Mathematics
- E2: Physics
- E3: Chemistry

If some students have both Mathematics and Physics, an edge is created between E1 and E2.

If no student shares Chemistry with the other examinations, E3 has no conflict edge with them.

## 4. Greedy Graph Coloring

Greedy Coloring assigns colors to vertices one by one.

Each color represents an examination time slot.

### Steps

1. Select an examination vertex.
2. Check the colors assigned to its neighbouring examinations.
3. Assign the smallest available color that does not create a conflict.
4. Move to the next vertex.
5. Repeat until all examinations are assigned.

### Pseudocode

```text
GreedyColoring(Graph):
    For each vertex:
        Mark all colors as available

        For each already colored neighbour:
            Mark its color as unavailable

        Assign the smallest available color

    Return assigned colors
```

The algorithm is simple and depends on the order in which examinations are processed.

## 5. DSATUR Algorithm

DSATUR stands for Degree of Saturation.

It selects the next vertex based on the number of different colors already used by its neighbouring vertices.

### Steps

1. Calculate the degree of each vertex.
2. Select an uncolored vertex with the highest saturation degree.
3. If there is a tie, select the vertex with the highest degree.
4. Assign the smallest available color.
5. Update the saturation degrees of neighbouring vertices.
6. Repeat until all vertices are colored.

### Pseudocode

```text
DSATUR(Graph):
    While uncolored vertices exist:

        Select vertex with highest saturation degree

        If there is a tie:
            Select vertex with highest degree

        Assign the smallest available color

        Update neighbouring vertices

    Return assigned colors
```

DSATUR gives priority to examinations with more restrictive conflict conditions.

## 6. Algorithm Comparison

Both algorithms aim to assign examinations to time slots without conflicts.

| Feature | Greedy Coloring | DSATUR |
|---|---|---|
| Selection | Based on vertex order | Based on saturation degree |
| Complexity | Generally O(V + E) for a fixed ordering with adjacency lists | Depends on implementation; a simple implementation may take O(V² + E) |
| Implementation | Simple | More complex |
| Scheduling | Depends on ordering | Prioritizes highly constrained vertices |
| Comparison | Number of colors used | Number of colors used |

The number of colors represents the number of time slots required by the generated timetable.

## 7. Room Allocation Algorithm

After generating the timetable, students must be assigned to examination rooms.

### Steps

1. Identify all examinations scheduled in a time slot.
2. Calculate the number of students appearing for each examination.
3. Read the available room capacities.
4. Assign rooms without exceeding their capacities.
5. Check whether total available capacity is sufficient.
6. Report an allocation problem if sufficient capacity is unavailable.

## 8. Seating Plan Generation

The seating plan assigns students to available seats in their allocated rooms.

### Steps

1. Retrieve the student list for an examination.
2. Retrieve the rooms assigned to that examination.
3. Read the seating capacity of each room.
4. Assign students to available seats.
5. Store the room and seat details.
6. Generate the final seating arrangement.

## 9. Timetable Regeneration

When examination details, student enrollment, or scheduling constraints change, the system can reconstruct the conflict graph and generate an updated timetable.

Room allocation and seating plans can then be generated again using the updated schedule.

## 10. Conclusion

Greedy Coloring and DSATUR are the main algorithms used for examination scheduling.

Conflict detection ensures that examinations sharing students are not assigned to the same time slot. Room allocation and seating-plan generation are then performed using student counts and room capacities.
