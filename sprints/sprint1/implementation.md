# Sprint 1 – Implementation Details

## 1. Introduction

This document records the implementation and planning activities performed during Sprint 1 of the Dynamic Graph Coloring Based Exam Timetabling and Seating Plan Generator.

The objective of this sprint is to prepare the basic system requirements, database structure, and user interface design before starting the main development.

## 2. Technologies Considered

The proposed technology stack includes:

- Next.js and React for the web application.
- TypeScript and Node.js for application and algorithm logic.
- Supabase with PostgreSQL for database storage.
- Cytoscape.js or D3.js for graph visualization.
- @react-pdf/renderer or Playwright for PDF generation.
- Git and GitHub for version control.
- Vercel for deployment.

The final technology stack will be confirmed by the team before implementation.

## 3. Requirement Analysis

The main requirements identified during Sprint 1 include:

- Student information management.
- Course and examination management.
- Room information management.
- Automatic examination conflict detection.
- Graph-based timetable generation.
- Room allocation according to capacity.
- Student seating-plan generation.
- Timetable and seating-plan export.

## 4. Database Design

The initial database design identifies the following entities:

| Entity | Responsibility |
|---|---|
| Students | Stores student information. |
| Courses | Stores course and subject details. |
| Examinations | Stores examination information. |
| Rooms | Stores room details and seating capacity. |
| Enrollments | Connects students with their enrolled courses. |
| Timetables | Stores generated examination schedules. |
| Seating Plans | Stores student room and seat assignments. |

The relationships between these entities will support conflict detection, timetable generation, and seating allocation.

## 5. User Interface Planning

The initial interface design includes:

- Administrator dashboard.
- Student and course management.
- Examination management.
- Room management.
- Conflict graph visualization.
- Generated timetable display.
- Seating-plan display.
- PDF export option.

## 6. Implementation Evidence

The following evidence will be added after completion:

- Database schema or design screenshot.
- UI wireframe screenshots.
- Requirement documentation.
- GitHub commit references.
- Relevant planning outputs.

## 7. Implementation Status

Actual implementation progress and verified results will be updated as development progresses.

## 8. Conclusion

Sprint 1 establishes the planning and design foundation of the examination timetabling system.

The requirements, database structure, and interface design will support graph algorithm development and system integration in the upcoming sprints.
