# Kanban Workflow & Work-in-Progress (WIP) Limits

## 1. Overview
While timeboxing is managed through Scrum Sprints, day-to-day task flow is governed by a **Kanban Board** to maintain continuous flow, visualize bottlenecks, and minimize context switching.

## 2. Board Columns & WIP Limits
| Column | Description | WIP Limit |
|---|---|---|
| **Backlog** | Prioritized user stories satisfying Definition of Ready (DoR) | Unlimited |
| **Sprint Backlog** | Committed tasks for the active sprint | 8 |
| **In Progress** | Active coding, algorithm implementation, or documentation | **3** |
| **Code Review / Pair Check** | Peer review of logic, algorithm proofs, and edge cases | **2** |
| **Testing / QA** | Automated pytest execution and verification against constraints | **2** |
| **Done** | Fully completed, tested, documented, meeting Definition of Done | Unlimited |

## 3. Workflow Policies
1. **Pull System:** Developers pull new items into *In Progress* only when the active WIP limit has capacity.
2. **Stop-the-Line on Test Failure:** If a CI build or unit test fails in *Testing / QA*, all forward progress halts until the failure is diagnosed and repaired.
3. **Continuous Verification:** Every algorithm change is immediately benchmarked on standard conflict graphs to verify chromatic number efficiency.
