# Requirements Specification

## 1. Project

Dynamic Graph Coloring Based Exam Timetabling and Seating Plan Generator

## 2. Intended User

The primary user described in the synopsis is the administrator, who manages academic data and generates the timetable and seating plan.

## 3. Functional Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR01 | The administrator can add student, course, room, and examination details. | High |
| FR02 | The system identifies examination conflicts automatically using shared-student information. | High |
| FR03 | The system represents examinations and their conflicts as a graph. | High |
| FR04 | The system generates an examination timetable using graph-coloring logic. | High |
| FR05 | The system supports Greedy Coloring and DSATUR-based scheduling for comparison. | High |
| FR06 | The system assigns rooms according to room capacity and examination requirements. | High |
| FR07 | The system generates a seating plan for each examination session. | High |
| FR08 | The administrator can regenerate the timetable and seating plan when inputs or constraints change. | Medium |
| FR09 | The system allows the administrator to view and export the final timetable and seating plan. | Medium |
| FR10 | The system visualizes the examination conflict graph. | Medium |

## 4. Input Requirements

The system is expected to work with the following information:

- Student records.
- Course and subject details.
- Student-course enrollment information.
- Examination details.
- Room details and room capacities.
- Scheduling constraints and examination requirements.

## 5. Output Requirements

- Examination conflict graph.
- Generated examination timetable.
- Time-slot allocation produced by the coloring algorithms.
- Room allocation for each examination session.
- Student seating plan.
- Exportable seating-plan PDF.

## 6. Non-Functional Requirements

The synopsis does not specify formal non-functional acceptance criteria. The following are reasonable project-level quality expectations to validate during development:

- **Usability:** Administrators should be able to enter data and understand generated results.
- **Correctness:** Shared-student examinations must not be assigned to the same time slot.
- **Capacity compliance:** Room allocations must not exceed the available room capacity.
- **Maintainability:** The application should keep data handling, algorithm execution, and presentation in manageable modules.
- **Reliability:** The system should report when available room capacity is insufficient rather than silently producing an invalid allocation.

## 7. Proposed Technology

The detailed implementation section of the synopsis describes:

- Next.js and React for the web interface and API/server-side functionality.
- Supabase with PostgreSQL for relational data storage.
- Cytoscape.js or D3.js for graph visualization.
- TypeScript/Node.js for Greedy and DSATUR algorithm execution.
- An optional Python FastAPI and NetworkX service if advanced graph processing is required.
- @react-pdf/renderer or Playwright for PDF generation.
- Git and GitHub for version control, and Vercel for deployment.

**Note:** The earlier proposed-technology table in the synopsis lists HTML/CSS/JavaScript, Flask, and MySQL. The later detailed technology section describes the Next.js/Supabase architecture above. The team should confirm which stack is the final implementation choice before development.
