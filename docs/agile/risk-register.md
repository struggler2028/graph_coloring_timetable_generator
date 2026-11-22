# Risk Register & Mitigation Strategy

## 1. Overview
The Risk Register documents technical, architectural, and operational risks identified throughout the development lifecycle of the examination timetabler and seating generator, alongside their evaluated impact and mitigation strategies.

## 2. Risk Matrix

| Risk ID | Description | Likelihood | Impact | Severity | Mitigation Strategy |
|---|---|---|---|---|---|
| **R01** | Suboptimal chromatic coloring resulting in excessive examination days | Medium | High | **High** | Implement the **DSATUR algorithm** with degree-of-saturation heuristic and highest-degree tie breaker to achieve optimal or near-optimal chromatic bounds. |
| **R02** | Room capacity overflow when multiple high-enrollment exams fall in same slot | High | High | **Critical** | Implement eager room allocation sorting rooms by capacity descending, enforce strict capacity checks, and trigger explicit warning banners. |
| **R03** | Inconsistent examination conflict detection due to course-code mismatch | Medium | Medium | **Medium** | Enforce unified Pydantic schemas validating enrollment course codes against the course catalog. |
| **R04** | Performance degradation on large-scale student conflict graphs | Low | Medium | **Medium** | Use adjacency sets and edge lookups with $O(1)$ amortized access time and fast bitwise or set intersection operations. |
| **R05** | Browser rendering bottleneck when rendering complex Cytoscape graphs | Low | Low | **Low** | Use the physics-based COSE layout with optimized iterations and node level of detail. |
| **R06** | Incomplete student seat assignments during multi-room exam splits | Medium | High | **High** | Implement coordinate-based tracking (`Row`, `Col`) maintaining state across split room allocations. |
