# Definition of Ready (DoR)

Before a product backlog item or user story is pulled into a Sprint Backlog during Sprint Planning, it must satisfy the **Definition of Ready**:

## 1. User Story Clarity (INVEST Criteria)
- **Independent:** The story can be developed and delivered without hard blockages on unstarted features.
- **Negotiable:** The specific algorithmic parameters or UI layout details can be adapted during development.
- **Valuable:** The increment delivers clear academic or operational benefit (e.g., clash reduction, automated room filling).
- **Estimable:** The development team understands the scope sufficiently to estimate effort in story points.
- **Small:** The story fits comfortably within the duration of a single one-week sprint.
- **Testable:** Concrete acceptance criteria exist to verify completion.

## 2. Prerequisite Data & Specifications
- [x] Clear data schemas defined for students, courses, exams, and rooms.
- [x] Clear mathematical or logical formulation established (e.g., Graph representation, DSATUR tie-breaking rule).
- [x] Mock data or benchmark scenarios available for validation.
- [x] Dependencies on earlier modules identified and verified.

## 3. Acceptance Criteria Template
Every story pulled into a sprint must include explicit testable criteria:
- *Given* an input set of examinations and shared student enrollments,
- *When* the timetabling engine executes,
- *Then* zero conflicting examinations are scheduled in the same time slot, and rooms are allocated within capacity.
